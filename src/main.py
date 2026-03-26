from fastapi import FastAPI
from src.triage_agent import TriageAgent
from pydantic import BaseModel
from typing import List, Dict

class QueryRequest(BaseModel):
    message: str
    history: List[Dict] = []

app = FastAPI()
agent = TriageAgent()

@app.get("/")
def home():
    return {"message": "Telecom Triage Agent Running"}

@app.post("/triage")
def triage(request: QueryRequest):
    try:
        return agent.process_message(request.message, request.history)
    except Exception as e:
        return {"error": str(e)}
    