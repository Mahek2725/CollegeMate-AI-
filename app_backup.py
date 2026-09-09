import streamlit as st
import requests

st.set_page_config(
    page_title="CollegeMate AI",
    page_icon="🎓"
)

st.title("🎓 CollegeMate AI")
st.write("Ask me anything about your college!")

# Load knowledge base
with open("college_data.txt", "r", encoding="utf-8") as file:
    knowledge_base = file.read()

question = st.text_input("Ask your question:")

if question:
    prompt = f"""
You are CollegeMate, a college information assistant.

IMPORTANT RULES:
1. Answer ONLY using the information provided in the knowledge base.
2. Do NOT make up information.
3. If the answer is not present in the knowledge base, say:
   "Sorry, I don't have that information in my knowledge base."
4. Keep the answer clear and concise.

KNOWLEDGE BASE:
{knowledge_base}

STUDENT QUESTION:
{question}

ANSWER:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:latest",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        answer = response.json()["response"]
        st.success(answer)
    else:
        st.error("Could not connect to Ollama.")