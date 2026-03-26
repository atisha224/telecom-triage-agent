def build_prompt(user_query, history=[], context=""):

    # ---------------- FORMAT CHAT HISTORY ---------------- #
    history_text = ""
    for msg in history:
        role = msg.get("role", "")
        content = msg.get("content", "")
        history_text += f"{role}: {content}\n"

    # ---------------- MAIN PROMPT ---------------- #
    prompt = f"""
You are a telecom support triage agent.

Your job is to:
1. Classify the user's intent
2. Detect urgency (Low / Medium / High)
3. Extract entities (id, issue, date if present)
4. Provide a helpful and accurate response

-------------------------
Conversation History:
{history_text}

-------------------------
Relevant Knowledge:
{context}

-------------------------
Current User Query:
{user_query}

-------------------------

IMPORTANT INSTRUCTIONS:
- You MUST return ONLY valid JSON
- DO NOT add explanations outside JSON
- DO NOT add text before or after JSON
- Ensure keys are always present
- If something is missing, use empty string ""

-------------------------

Return JSON in this exact format:

{{
  "intent": "",
  "urgency": "",
  "entities": {{
    "id": "",
    "issue": "",
    "date": ""
  }},
  "response": ""
}}
"""
    return prompt