from fastapi import FastAPI, UploadFile, File
from src.llm.extractor import extract_profile
from src.ml.model import predict_score
from src.rag.retriever import get_interviews
from src.llm.explainer import generate_explanation
from src.utils.parser import extract_text_from_pdf

app = FastAPI()

# =====================================================
# 🧠 HELPER FUNCTIONS (CORE LOGIC LAYER)
# =====================================================

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


# =====================================================
# 🚀 ADVANCED INTELLIGENCE LAYER
# =====================================================

def adjust_for_role(profile, role):
    if role == "ML":
        if "ML" in profile["skills"]:
            profile["tech_stack"] += 2

    if role == "SDE":
        if profile["dsa"] >= 7:
            profile["dsa"] += 1

    return profile


def get_confidence(profile):
    return min(100, (
        profile["projects"] * 10 +
        profile["experience"] * 15 +
        len(profile["skills"]) * 5
    ))


def classify_user(profile):
    if profile["projects"] <= 1:
        return "Beginner"
    elif profile["experience"] >= 2:
        return "Advanced"
    else:
        return "Intermediate"


def skill_gap(profile):
    gaps = []

    if "SQL" not in profile["skills"]:
        gaps.append("SQL")

    if profile["dsa"] < 7:
        gaps.append("DSA")

    if profile["projects"] < 3:
        gaps.append("Real-world Projects")

    return gaps


def roadmap(profile):
    steps = []

    if profile["dsa"] < 7:
        steps.append("Solve 300+ DSA problems")

    if profile["projects"] < 3:
        steps.append("Build 2 advanced projects")

    if profile["experience"] < 2:
        steps.append("Get internship or open-source experience")

    steps.append("Prepare system design")

    return steps


# =====================================================
# 🌐 ROUTES
# =====================================================

@app.get("/")
def home():
    return {"message": "Placement Predictor running 🚀"}


@app.post("/predict")
def predict(data: dict):
    text = data["text"]
    role = data.get("role", "SDE")

    # Step 1: Extract
    profile = extract_profile(text)

    # Step 2: Role adjustment
    profile = adjust_for_role(profile, role)

    # Step 3: Base ML score
    score = predict_score(profile)

    # Step 4: Smart boost layer
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

    # Step 5: RAG
    interviews = get_interviews(profile)

    # Step 6: Explanation
    explanation = generate_explanation(profile, score, interviews)

    # Step 7: Intelligence layer
    level = get_level(score)
    companies = suggest_companies(score)
    weaknesses = get_weaknesses(profile)

    confidence = get_confidence(profile)
    user_type = classify_user(profile)
    gaps = skill_gap(profile)
    plan = roadmap(profile)

    return {
        "profile": profile,
        "score": score,
        "level": level,
        "profile_type": user_type,
        "confidence": confidence,
        "skill_gaps": gaps,
        "roadmap": plan,
        "recommended_companies": companies,
        "weaknesses": weaknesses,
        "interviews": interviews,
        "analysis": explanation
    }


@app.post("/upload-resume")
def upload_resume(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    text = extract_text_from_pdf(file_path)

    profile = extract_profile(text)
    profile = adjust_for_role(profile, "SDE")

    score = predict_score(profile)

    # Smart boost layer
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

    confidence = get_confidence(profile)
    user_type = classify_user(profile)
    gaps = skill_gap(profile)
    plan = roadmap(profile)

    return {
        "profile": profile,
        "score": score,
        "level": level,
        "profile_type": user_type,
        "confidence": confidence,
        "skill_gaps": gaps,
        "roadmap": plan,
        "recommended_companies": companies,
        "weaknesses": weaknesses,
        "interviews": interviews,
        "analysis": explanation
    }