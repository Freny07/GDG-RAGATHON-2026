from fastapi import FastAPI, UploadFile, File
from src.llm.extractor import extract_profile
from src.ml.model import predict_score
from src.rag.retriever import get_interviews
from src.llm.explainer import generate_explanation
from src.utils.parser import extract_text_from_pdf

app = FastAPI()

# -----------------------------
# Helper Functions
# -----------------------------

def get_level(score):
    if score < 50:
        return "Low readiness"
    elif score < 75:
        return "Moderate readiness"
    else:
        return "High readiness"

def suggest_companies(score):
    if score > 80:
        return ["Google", "Amazon", "Microsoft"]
    elif score > 60:
        return ["Flipkart", "Goldman Sachs", "Adobe"]
    else:
        return ["TCS", "Infosys", "Wipro"]

def get_weaknesses(profile):
    weaknesses = []

    if profile["projects"] < 2:
        weaknesses.append("Low project count")

    if profile["experience"] < 1:
        weaknesses.append("No internships")

    if profile["dsa"] < 5:
        weaknesses.append("Weak DSA")

    if not weaknesses:
        weaknesses.append("Need stronger DSA consistency")

    return weaknesses

# -----------------------------
# Routes
# -----------------------------

@app.get("/")
def home():
    return {"message": "Placement Predictor running 🚀"}

@app.post("/predict")
def predict(data: dict):
    text = data["text"]

    # Step 1: Extract profile
    profile = extract_profile(text)

    # Step 2: Predict score
    score = predict_score(profile)

    # ------------------------
    # 🚀 SMART ADJUSTMENT LAYER
    # ------------------------
    boost = 0

    if profile["academic_score"] >= 8.5:
        boost += 10

    if profile["projects"] >= 3:
        boost += 8

    if profile["experience"] >= 2:
        boost += 10

    if len(profile["skills"]) >= 5:
        boost += 7

    if profile["dsa"] >= 7:
        boost += 8

    score = min(100, score + boost)

    # Step 3: RAG retrieval
    interviews = get_interviews(profile)

    # Step 4: Explanation
    explanation = generate_explanation(profile, score, interviews)

    # Step 5: Extra insights
    level = get_level(score)
    companies = suggest_companies(score)
    weaknesses = get_weaknesses(profile)

    return {
        "profile": profile,
        "score": score,
        "level": level,
        "recommended_companies": companies,
        "weaknesses": weaknesses,
        "interviews": interviews,
        "analysis": explanation
    }

# -----------------------------
# Resume Upload Endpoint
# -----------------------------

@app.post("/upload-resume")
def upload_resume(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    # Save uploaded file
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # Extract text
    text = extract_text_from_pdf(file_path)

    # Same pipeline
    profile = extract_profile(text)
    score = predict_score(profile)

    # ------------------------
    # 🚀 SMART ADJUSTMENT LAYER
    # ------------------------
    boost = 0

    if profile["academic_score"] >= 8.5:
        boost += 10

    if profile["projects"] >= 3:
        boost += 8

    if profile["experience"] >= 2:
        boost += 10

    if len(profile["skills"]) >= 5:
        boost += 7

    if profile["dsa"] >= 7:
        boost += 8

    score = min(100, score + boost)

    interviews = get_interviews(profile)
    explanation = generate_explanation(profile, score, interviews)

    level = get_level(score)
    companies = suggest_companies(score)
    weaknesses = get_weaknesses(profile)

    return {
        "profile": profile,
        "score": score,
        "level": level,
        "recommended_companies": companies,
        "weaknesses": weaknesses,
        "interviews": interviews,
        "analysis": explanation
    }