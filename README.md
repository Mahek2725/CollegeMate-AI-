# College Mate AI 🎓

## Overview

**College Mate AI** is an AI-powered student assistance system designed to help college students access information and get answers to common academic and campus-related queries through an intelligent conversational interface.

The project uses **Artificial Intelligence and Large Language Model (LLM)** capabilities to provide students with a simple and interactive way to obtain relevant information.

## Key Features

* 🤖 AI-powered conversational assistant
* 🎓 Designed specifically for college students
* 💬 Natural language interaction
* 📚 Answers academic and college-related queries
* 🔎 Provides relevant information based on the available knowledge base
* 🌐 Interactive web interface using Streamlit
* ⚡ Simple and user-friendly interface

## Technologies Used

* **Python**
* **Streamlit**
* **Ollama**
* **Llama 3.2**
* **Large Language Models (LLMs)**
* **Prompt Engineering**
* **Knowledge Base**

## Project Structure

```text
College-Mate-AI/
│
├── app.py
├── backup_app.py
├── requirements.txt
├── README.md
│
├── knowledge_base/
│   └── ...
│
└── other project files/
```

## How It Works

The system follows a simple workflow:

1. The user enters a query through the Streamlit interface.
2. The query is processed by the application.
3. Relevant information is retrieved from the available knowledge base.
4. The query and relevant context are provided to the AI model.
5. The LLM generates an appropriate response.
6. The response is displayed to the user through the Streamlit interface.

## AI Model

The project uses **Llama 3.2** through **Ollama** to process user queries and generate responses.

## Running the Project Locally

### 1. Clone the Repository

```bash
git clone <your-github-repository-link>
```

### 2. Navigate to the Project Folder

```bash
cd College-Mate-AI
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Ollama

Make sure Ollama is installed and the required model is available:

```bash
ollama run llama3.2
```

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in the browser.

## Project Purpose

The primary objective of **College Mate AI** is to provide students with an accessible AI-based assistant that can simplify information retrieval and support students in their day-to-day academic and college-related activities.

## Future Scope

* Integration with real-time college information
* Student timetable and academic schedule assistance
* Integration with college notices and announcements
* Personalized student assistance
* Voice-based interaction
* Integration with additional AI models and services

## Author

**Mahek Karwat**

Department of Artificial Intelligence
St. Vincent Pallotti College of Engineering and Technology, Nagpur
