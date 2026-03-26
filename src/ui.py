import streamlit as st
import requests

# ---------------- CONFIG ---------------- #
st.set_page_config(page_title="Telecom AI Chat", layout="centered")

st.title("📡 Telecom AI Assistant")

# ---------------- SESSION STATE ---------------- #
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- DISPLAY CHAT HISTORY ---------------- #
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- INPUT BOX ---------------- #
user_input = st.chat_input("Describe your issue...")

if user_input:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call backend
    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/triage",
                    json={
                        "message": user_input,
                        "history": st.session_state.messages
                    }
                )

                result = response.json()

                # Format response nicely
                reply = f"""
**Intent:** {result.get("intent", "N/A")}  
**Urgency:** {result.get("urgency", "N/A")}  
**Ticket:** {result.get("tool_result", {}).get("status", "N/A")}  
**Priority:** {result.get("tool_result", {}).get("priority", "")}

**Response:**  
{result.get("response", "N/A")}

**Entities:**  
{result.get("entities", {})}
"""

                st.markdown(reply)

                # Save assistant reply
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": reply
                })

            except Exception as e:
                error_msg = f"Error: {e}"
                st.error(error_msg)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg
                })
