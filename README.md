# 🚀 Resume Matcher AI — Multi-Job Comparison, ATS Scoring & Resume Review using RAG + LangChain

An end-to-end **AI-powered Resume Review and Job Matching System** that evaluates resumes against multiple job descriptions using **Retrieval-Augmented Generation (RAG), LangChain, HuggingFace LLMs, and semantic embeddings**.

Built with a **production-grade FastAPI backend and Streamlit frontend**, designed to simulate real-world ATS and recruiter workflows.

---

# 🌐 Live Demo

Frontend:  
https://resume-matcher-ai-multi-job-comparison-my09.onrender.com  

# 🧠 Key Features

## 📄 Resume Parsing
- Supports **PDF and DOCX**
- Extracts clean structured text
- Handles real-world resume formats

## 🎯 Multi-Job Comparison
- Compare resume against **multiple job descriptions**
- Semantic similarity ranking
- Identifies best matching job automatically

## 📊 ATS Scoring Engine
- Skill-based ATS scoring
- Calculates:
  - ATS Match Score (%)
  - Missing Skills
  - Skill Coverage

## 🤖 AI Resume Review using RAG
Uses:

- LangChain
- HuggingFace LLMs
- ChromaDB Vector Database
- Embedding Models

Provides:

- Resume feedback
- Improvement suggestions
- Skill gap analysis

## 🔍 Skill Extraction Engine
Detects:

- Programming languages
- ML frameworks
- Cloud tools
- GenAI tools
- Backend technologies

---

# 🏗️ System Architecture

```
User
 ↓
Streamlit Frontend
 ↓
FastAPI Backend
 ↓
Resume Parser
 ↓
Skill Extractor
 ↓
Embedding Model
 ↓
ChromaDB Vector Store
 ↓
Retriever
 ↓
HuggingFace LLM
 ↓
ATS Score + Resume Feedback
```

---

# 🛠️ Tech Stack

## Backend
- FastAPI
- LangChain
- HuggingFace Transformers
- ChromaDB
- Sentence Transformers
- PyMuPDF
- Python-docx

## Frontend
- Streamlit
- Requests

## AI / ML
- Retrieval-Augmented Generation (RAG)
- Semantic embeddings
- Vector search
- LLM-based resume feedback

## Deployment
- Render
- HuggingFace Models

---

# 📂 Project Structure

```
Resume-Matcher-AI/
│
├── main.py
├── app.py
│
├── rag/
│   ├── chain.py
│   ├── vector_store.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── ats.py
│   ├── parser.py
│   └── prompts.py
│
├── engine/
│   ├── skill_extractor.py
│   └── job_matcher.py
│
├── chroma_db/
│
├── requirements.txt
├── runtime.txt
└── README.md
```

---



# 📈 Production-Level Design Features

- Retrieval-Augmented Generation (RAG)
- Vector database retrieval
- Semantic similarity matching
- FastAPI production backend
- Modular architecture
- Frontend-backend separation
- Environment-based configuration
- Deployable on cloud platforms

---

# 🎯 Real-World Applications

- Resume screening platforms
- ATS systems
- AI recruiting tools
- Job recommendation engines
- Career coaching tools

---

# 👨‍💻 Author

Manish Mohapatra

AI Engineer / Data Scientist  
Specializing in:

- GenAI
- LangChain
- RAG systems
- Machine Learning Systems

GitHub:  
https://github.com/Manish-2005-glitch

---

# ⭐ Star this repository if you found it useful!
