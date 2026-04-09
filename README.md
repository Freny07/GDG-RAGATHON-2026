🎓 Placement Predictor & Mentor (Statement 3)
🎯 Overview

The Placement Predictor & Mentor is a hybrid AI system that evaluates a student’s placement readiness and provides personalized guidance.

It combines LLM-based profile extraction, regression modeling, and RAG-based retrieval to deliver:

A Readiness Score (0–100)
Personalized improvement feedback
Relevant senior interview experiences

The system is designed to simulate real-world placement preparation using data-driven insights and contextual recommendations.

✨ Key Features
📊 Readiness Score Prediction

Uses a trained regression model to evaluate placement readiness based on:

CGPA
Skills
Projects
Internships
Communication
Open-source experience
🤖 Structured Profile Extraction

Automatically converts user input or resume content into structured JSON using an LLM.

📄 Resume Parser

Supports PDF/DOCX uploads and extracts:

CGPA
Skills
Experience
🔍 Smart Experience Matcher

Uses cosine similarity to match user profiles with interview experiences and returns the top 3 most relevant results.

🧠 RAG-Based Retrieval

Implements a Retrieval-Augmented Generation pipeline:

Interview data → embeddings
Stored in vector database
Retrieved based on profile similarity
🎨 Personalized Feedback

Generates actionable suggestions to improve placement readiness.

🛠️ Tech Stack
LLM: HuggingFace Transformers (FLAN-T5)
Embeddings: Sentence Transformers
Regression: Scikit-learn
Vector DB: ChromaDB / FAISS
Backend: Python (FastAPI / Flask)
Frontend: React.js
Data Processing: Pandas, NumPy
🚀 Getting Started
1. Setup Environment
python -m venv venv

# Activate
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
2. Environment Variables

Create a .env file:

HF_TOKEN=your_huggingface_token
3. Run the Project
Backend
cd Statement-3-Placement-Predictor/src
python app.py
Frontend
cd frontend
npm install
npm run dev
📂 Project Structure
Statement-3-Placement-Predictor/
├── data/          # Dataset (placement records)
├── src/           # Core logic (LLM + Regression + RAG)
├── models/        # Trained regression model
├── utils/         # Parsing and helper functions
└── README.md
🏆 Advanced Capabilities
Resume-based automatic profile extraction
Cosine similarity-based experience matching
Hybrid AI system (LLM + ML + RAG)
Modular and scalable architecture
