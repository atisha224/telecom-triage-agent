from src.llm_service import LLMService
from src.prompts import build_prompt
from src.vector_store import VectorStore
from src.data import documents

import json
import re
import logging

# LOGGING 
logging.basicConfig(level=logging.INFO)


class TriageAgent:
    def __init__(self):
        self.llm = LLMService()

        # Initialize FAISS vector store
        self.vector_store = VectorStore()
        self.vector_store.create_store(documents)

    
    # MAIN PIPELINE
    
    def process_message(self, message, history=[]):

        logging.info(f"Incoming query: {message}")

        # Retrieve relevant context (RAG)
        docs = self.vector_store.search(message)
        context = "\n".join([doc.page_content for doc in docs])

        # Build prompt
        prompt = build_prompt(message, history, context)

        # Call LLM
        result = self.llm.call_llm(prompt)
        logging.info(f"LLM raw output: {result}")

        # Parse JSON safely
        try:
            json_text = re.search(r"\{.*\}", result, re.DOTALL).group()
            data = json.loads(json_text)
        except Exception as e:
            return {
                "error": "Invalid LLM output",
                "raw_output": result
            }

        # Validation
        required_fields = ["intent", "urgency", "response"]
        for field in required_fields:
            if field not in data:
                data[field] = "Unknown"

        # Agent Decision
        action = self.decide_action(data)

        # Execute Tool
        tool_result = self.execute_action(action, data)

        # Attach results
        data["action"] = action
        data["tool_result"] = tool_result

        return data

    
    # DECISION ENGINE (AGENT LOGIC)
    
    def decide_action(self, data):

        urgency = data.get("urgency", "").lower()
        intent = data.get("intent", "").lower()

        if urgency == "high":
            return "create_ticket"

        elif "billing" in intent:
            return "billing_support"

        else:
            return "general_response"

    
    # TOOL EXECUTION
    
    def execute_action(self, action, data):

        urgency = data.get("urgency", "Medium")

        if action == "create_ticket":
            return {
                "status": "Ticket Created",
                "priority": "High"
            }

        elif action == "billing_support":
            return {
                "status": "Redirected to Billing Department",
                "priority": urgency
            }

        else:
            return {
                "status": "Handled Automatically",
                "priority": urgency
            }
        