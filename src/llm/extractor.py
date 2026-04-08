def extract_profile(text):
    text = text.lower()

    profile = {
        "academic_score": 7,
        "dsa": 5,
        "projects": 2,
        "experience": 1,
        "opensource": 0,
        "soft_skills": 5,
        "tech_stack": 5,
        "skills": []
    }

    # simple parsing
    if "cgpa" in text:
        try:
            words = text.split()
            for i, w in enumerate(words):
                if "cgpa" in w:
                    profile["academic_score"] = float(words[i-1])
        except:
            pass

    if "dsa" in text:
        profile["dsa"] = 7

    if "project" in text:
        profile["projects"] = 3

    if "internship" in text:
        profile["experience"] = 2

    if "python" in text:
        profile["skills"].append("Python")

    if "ml" in text:
        profile["skills"].append("ML")

    if "react" in text:
        profile["skills"].append("React")

    if not profile["skills"]:
        profile["skills"] = ["DSA"]

    return profile