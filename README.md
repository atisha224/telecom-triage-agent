# 📡 TeleQuiz AI — Telecom Support Triage Agent

An AI-powered telecom support system that classifies user issues, extracts key information, and generates intelligent responses using a combination of Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

* 🔍 Intent Classification (Network, SIM, Billing, etc.)
* ⚡ Urgency Detection (Low / Medium / High)
* 🧠 Named Entity Recognition (ID, Issue, Date)
* 📚 RAG (Retrieval-Augmented Generation using FAISS)
* 🤖 LLM Integration (Groq - LLaMA 3.1)
* 🧩 Agent-Based Decision System (Action + Tool Execution)
* 💬 Chat-style UI (Streamlit)
* 🎯 Automated actions (Ticket creation, routing)

---

## 🏗️ Architecture

User → Streamlit UI → FastAPI → FAISS (Vector DB) → LLM → Agent Logic → Response

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Streamlit
* LangChain
* FAISS (Vector Database)
* Groq (LLM API)
* HuggingFace Embeddings

---

## 📂 Project Structure

```
telecom-triage-agent/
│
├── src/
│   ├── main.py
│   ├── triage_agent.py
│   ├── llm_service.py
│   ├── vector_store.py
│   ├── prompts.py
│   ├── data.py
│   ├── ui.py
│
├── requirements.txt
├── .gitignore
├── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/atisha224/telecom-triage-agent.git
cd telecom-triage-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

⚠️ Do NOT upload `.env` to GitHub

---

### 4. Run Backend (FastAPI)

```bash
python -m uvicorn src.main:app --reload
```

---

### 5. Run Frontend (Streamlit UI)

```bash
python -m streamlit run src/ui.py
```

---

## 🎯 Example Output

```
Intent: Network Issue  
Urgency: High  
Action: create_ticket  

Response:
Restart your router and check your network connection.

Entities:
{id: "", issue: "internet not working", date: ""}
```

---

## 🧠 How It Works

1. User enters a telecom query
2. FAISS retrieves relevant telecom knowledge
3. LLM analyzes query (intent, urgency, entities)
4. Agent logic decides action
5. System generates structured response

---

## 🔐 Security

* API keys stored in `.env`
* `.env` excluded using `.gitignore`
* No sensitive data stored in repository

---

## 📌 Future Improvements

* Add database (PostgreSQL / MongoDB)
* Deploy on cloud (Render / AWS)
* Add authentication (Admin / Staff roles)
* Integrate real telecom datasets
* Improve agent workflow with LangChain tools

---

## 👩‍💻 Author

**Atisha Jain**

---

## ⭐ If you found this project useful, consider giving it a star!
