```
# 💼 AI Career Assistant
---
An AI-powered Resume Analyzer and PDF Chatbot built with Streamlit, LangChain, Ollama, and OpenAI.

This project allows users to analyze resumes and interact with PDF documents using AI.

## 🚀 Features

### 📄 Resume Analyzer

Upload a resume and get:

* Resume score

* Candidate summary

* Skills analysis

* Experience evaluation

* Improvement suggestions

### 📚 PDF Chatbot

Upload a PDF and ask questions about the document using RAG (Retrieval Augmented Generation).
---
## 🧠 AI Model Support

The application supports two AI providers.

### 🖥️ Ollama (Local AI)

- gemma3:4b
- llama3
- mistral
### ☁️ OpenAI API
- gpt-4o-mini
---
# 🏗 Project Structure

ai_career_assistant/

│
├── app.py
├── config.py
├── requirements.txt
│
├── models
│   ├── openai_model.py
│   └── ollama_model.py
│
├── modules
│   ├── pdf_loader.py
│   ├── resume_analyzer.py
│   ├── vector_store.py
│   └── rag_pipeline.py
│
└── utils
---
## ⚙️ Installation

Clone the repository
```bash
git clone https://github.com/yourusername/ai-career-assistant.git
cd ai-career-assistant
```
Install dependencies
```bash
pip install -r requirements.txt
```
▶️ Run the Application
streamlit run app.py
 
Open in browser:

http://localhost:8501

# 🛠 Technologies
---
- Python
- Streamlit
- LangChain
- FAISS
- Ollama
- OpenAI API
- PyPDF2
```
