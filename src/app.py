from fastapi import FastAPI
from src.llm.extractor import extract_profile
from src.ml.model import predict_score
from src.rag.retriever import get_interviews
from src.llm.explainer import generate_explanation

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Placement Predictor running 🚀"}

@app.post("/predict")
def predict(data: dict):
    text = data["text"]

    # Step 1: Extract profile using LLM
    profile = extract_profile(text)

    # Step 2: Predict score using ML
    score = predict_score(profile)

    # Step 3: Get interview matches using RAG
    interviews = get_interviews(profile)

    # Step 4: Generate explanation using LLM
    explanation = generate_explanation(profile, score, interviews)

    return {
        "profile": profile,
        "score": score,
        "interviews": interviews,
        "analysis": explanation
    }