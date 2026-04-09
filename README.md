Statement 3: Placement Predictor & Mentor
🚀 Overview

The Placement Predictor & Mentor is a hybrid AI-powered system designed to evaluate a student’s placement readiness and provide personalized guidance.

It combines:

🤖 LLM-based profile extraction
📊 Regression modeling for score prediction
🔍 RAG-based interview experience retrieval

Users can enter their details manually or upload their resume, and receive:

🎯 A Readiness Score (0–100)
📈 Personalized feedback
💼 Relevant senior interview experiences
🧠 System Workflow
1️⃣ User Input

The system supports two modes:

📝 Manual input (CGPA, skills, projects, etc.)
📄 Resume upload (PDF/DOCX)
2️⃣ LLM-Based Structured Extraction

User input is processed using an LLM to extract structured data in JSON format:

{
  "cgpa": 8.5,
  "skills": ["Python", "React", "AWS"],
  "projects": 3,
  "internships": 1,
  "communication": 7,
  "opensource": 2
}
3️⃣ Feature Engineering

Extracted data is converted into numerical features:

CGPA
Number of skills
Number of projects
Internship count
Communication score
Open-source contributions
4️⃣ Regression Model

The processed features are passed into a trained regression model.

📊 Output:

Placement Readiness Score (0–100)

📈 Model Details:

Algorithm: Regression (Linear Regression / Random Forest)
Dataset: Senior placement dataset

📉 Performance Metrics:

R² Score: 0.xx
Mean Squared Error: xx.xx
5️⃣ RAG-Based Experience Retrieval

We implemented a Retrieval-Augmented Generation (RAG) pipeline:

Interview experiences are converted into embeddings
Stored in a vector database (ChromaDB / FAISS)
Retrieved based on user profile similarity
🏆 Bonus Features
📄 Resume Parser
Supports PDF/DOCX uploads
Automatically extracts:
CGPA
Skills
Experience

Tech Used:

PyPDF / python-docx
Regex + LLM fallback
🧠 Smart Experience Matcher
Uses Cosine Similarity
Matches user profile with interview database
Returns Top 3 relevant experiences

🎯 Example:

Java + AWS → Amazon / Goldman Sachs experiences
🎨 Creative Features
📊 Score Visualization
Displays strengths vs weaknesses
🧠 AI Mentor Suggestions
Personalized improvement tips
⚡ Flexible Input System
Manual entry + Resume support

These features improve usability and provide a more personalized experience.

🏗️ System Architecture
User Input (Manual / Resume)
        ↓
LLM Extraction (JSON)
        ↓
Feature Engineering
        ↓
Regression Model → Readiness Score
        ↓
Embedding Generation
        ↓
Vector DB (Chroma / FAISS)
        ↓
Top 3 Interview Matches
        ↓
Final Output (Score + Feedback)
🛠️ Tech Stack
AI / ML
HuggingFace Transformers (FLAN-T5)
Scikit-learn
Sentence Transformers
RAG
ChromaDB / FAISS
Cosine Similarity
Backend
Python (FastAPI / Flask)
Frontend
React.js
Data Processing
Pandas, NumPy
⚙️ Setup Instructions
# Clone repository
git clone https://github.com/[YOUR_USERNAME]/GDG-RAGATHON-2026.git
cd GDG-RAGATHON-2026

# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
🔐 Environment Variables

Create a .env file:

HF_TOKEN=your_huggingface_token
▶️ Run the Project
Backend
cd Statement-3-Placement-Predictor/src
python app.py
Frontend
cd frontend
npm install
npm run dev
📂 Folder Structure
Statement-3-Placement-Predictor/
├── data/              # Dataset (CSV)
├── src/               # Core logic (LLM + Regression + RAG)
├── models/            # Trained models
├── utils/             # Helper functions
└── README.md
📌 Key Highlights
✅ Hybrid AI system (LLM + Regression + RAG)
✅ Manual input + Resume upload
✅ Smart interview recommendation system
✅ Modular and scalable architecture
✅ Real-world placement use case
👥 Team Details

Team Name: Ceres

Members:

- Freny Kansagra — LCS2025032
- Anshuma — LCI2025059
- Nayan Gupta — LIT2025045
