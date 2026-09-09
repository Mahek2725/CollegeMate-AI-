import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="CollegeMate AI",
    page_icon="🎓",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .info-box {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-bottom: 20px;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown(
    '<div class="main-title">🎓 CollegeMate AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your AI-powered college information assistant</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-box">
💡 <b>How it works:</b> Ask a question about your college.
CollegeMate checks its knowledge base before generating an answer.
</div>
""", unsafe_allow_html=True)


# ---------------- LOAD KNOWLEDGE BASE ----------------
with open("college_data.txt", "r", encoding="utf-8") as file:
    knowledge_base = file.read()


# ---------------- WHAT CAN I ASK? ----------------
with st.expander("💡 What can I ask?"):

    st.markdown("### 📌 CollegeMate can help with:")

    st.markdown("""
    - 📝 **Admissions** — admission requirements and required documents
    - 📋 **Examinations** — examination rules and procedures
    - 💰 **Fees** — fee and payment-related guidance
    - 📚 **Academics** — course registration, subjects and attendance
    - 📞 **Department Contacts** — Accounts, Examination, Academic and Admission departments
    - 🏠 **Hostel** — hostel-related queries
    - 📖 **Library** — library-related queries
    """)

    st.markdown("### 💬 Example questions:")

    st.markdown("""
    - What documents are required for admission?
    - What are the examination rules?
    - Who should I contact for fee-related issues?
    - How can I contact the Academic Department?
    - Who should I contact for hostel queries?
    - Who should I contact for library-related queries?
    """)


# ---------------- OLLAMA FUNCTION ----------------
def ask_ollama(prompt):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:latest",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return None


# ---------------- USER INPUT ----------------
question = st.text_input(
    "💬 Ask your question",
    placeholder="Example: What documents are required for admission?"
)


# ---------------- AGENT ----------------
if question:

    with st.spinner("🤖 CollegeMate is thinking..."):

        # STEP 1: Decision-making
        decision_prompt = f"""
You are the decision-making agent for a college assistant.

Read the knowledge base and the student's question.

Knowledge Base:
{knowledge_base}

Student Question:
{question}

Decide whether the knowledge base contains information that can answer
the student's question.

Reply with ONLY one word:
YES
or
NO
"""

        decision = ask_ollama(decision_prompt)


    # ---------------- AGENT DECISION ----------------

    if decision and "YES" in decision.upper():

        st.caption("🤖 Agent decision: Knowledge Base → YES")

        answer_prompt = f"""
You are CollegeMate, a college information assistant.

Answer the student's question ONLY using the knowledge base below.

Rules:
1. Do not use outside knowledge.
2. Do not make up information.
3. Give a clear and concise answer.
4. If the information is not sufficient, say:
"Sorry, I don't have that information in my knowledge base."

Knowledge Base:
{knowledge_base}

Student Question:
{question}

Answer:
"""

        with st.spinner("📚 Finding the answer..."):
            answer = ask_ollama(answer_prompt)

        if answer:
            st.success("✅ Answer")
            st.write(answer)
        else:
            st.error("Could not get a response from Ollama.")

    else:

        st.caption("🤖 Agent decision: Knowledge Base → NO")

        st.warning(
            "Sorry, I can only answer questions related to "
            "the information available in my college knowledge base."
        )


# ---------------- FOOTER ----------------
st.markdown(
    '<div class="footer">Built with ❤️ using Streamlit + Ollama + Llama 3.2</div>',
    unsafe_allow_html=True
)

