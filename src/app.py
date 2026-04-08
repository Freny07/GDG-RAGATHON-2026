from fastapi import FastAPI
from src.llm.extractor import extract_profile
from src.ml.model import predict_score
from src.rag.retriever import get_interviews
from src.llm.explainer import generate_explanation

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Placement Predictor API running 🚀"}

@app.post("/predict")
def predict(data: dict):
    profile = extract_profile(data["text"])
    score = predict_score(profile)
    interviews = get_interviews(profile)
    explanation = generate_explanation(profile, score, interviews)

    return {
        "profile": profile,
        "score": score,
        "interviews": interviews,
        "analysis": explanation
    }