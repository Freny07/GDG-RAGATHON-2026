import re

def extract_profile(text):
    text_lower = text.lower()

    profile = {
        "academic_score": 7,
        "dsa": 5,
        "projects": 0,
        "experience": 0,
        "opensource": 0,
        "soft_skills": 5,
        "tech_stack": 0,
        "skills": []
    }

    # ------------------------
    # 🎓 ACADEMICS (MULTI SIGNAL)
    # ------------------------
    cgpa = re.findall(r'(\d\.\d{1,2})\s*(cgpa|gpa)', text_lower)
    percent = re.findall(r'(\d{2,3})\s*%', text_lower)
    percentile = re.findall(r'(\d{2,3})\s*percentile', text_lower)

    if cgpa:
        val = float(cgpa[0][0])
        profile["academic_score"] = val

    elif percentile:
        val = int(percentile[0])
        profile["academic_score"] = min(10, val / 10)

    elif percent:
        val = int(percent[0])
        profile["academic_score"] = min(10, val / 10)

    # Bonus academic signals
    if any(x in text_lower for x in ["iit", "nit", "iiit"]):
        profile["academic_score"] = max(profile["academic_score"], 8.5)

    # ------------------------
    # 💻 SKILLS ENGINE (RICH DETECTION)
    # ------------------------
    SKILLS_DB = {
        "languages": ["python", "java", "c++", "c", "go", "javascript", "typescript"],
        "frontend": ["react", "next", "html", "css"],
        "backend": ["node", "express", "django", "flask"],
        "database": ["sql", "mysql", "mongodb"],
        "cloud": ["aws", "azure", "gcp"],
        "ml": ["ml", "ai", "nlp", "tensorflow", "pytorch"],
        "tools": ["docker", "kubernetes", "linux", "git"]
    }

    found_skills = set()
    domain_score = 0

    for category, skills in SKILLS_DB.items():
        for skill in skills:
            if re.search(rf'\b{skill}\b', text_lower):
                domain_score += 1

                if skill in ["ml", "ai", "nlp", "sql"]:
                    found_skills.add(skill.upper())
                elif skill == "c++":
                    found_skills.add("C++")
                elif skill == "go":
                    found_skills.add("Go")
                else:
                    found_skills.add(skill.capitalize())

    profile["skills"] = list(found_skills) if found_skills else ["General Programming"]

    # ------------------------
    # ⚙️ TECH STACK DEPTH (IMPORTANT)
    # ------------------------
    profile["tech_stack"] = min(10, domain_score)

    # ------------------------
    # 🧠 DSA INTELLIGENCE
    # ------------------------
    if re.search(r'(dsa|data structures|algorithms)', text_lower):
        profile["dsa"] = 7

    if re.search(r'(competitive programming|codeforces|leetcode)', text_lower):
        profile["dsa"] = 9

    # ------------------------
    # 📦 PROJECT ANALYSIS (SMART)
    # ------------------------
    proj_num = re.search(r'projects?\s*[:\-]?\s*(\d+)', text_lower)

    if proj_num:
        profile["projects"] = min(5, int(proj_num.group(1)))
    else:
        verbs = len(re.findall(r'(built|developed|created|designed)', text_lower))
        profile["projects"] = min(5, max(1, verbs))

    # Boost if complex words exist
    if re.search(r'(scalable|architecture|system design)', text_lower):
        profile["projects"] += 1

    profile["projects"] = min(5, profile["projects"])

    # ------------------------
    # 💼 EXPERIENCE (DEPTH-AWARE)
    # ------------------------
    exp_num = re.search(r'(internships?|experience)\s*[:\-]?\s*(\d+)', text_lower)

    if exp_num:
        profile["experience"] = min(3, int(exp_num.group(2)))
    else:
        exp_hits = len(re.findall(r'(intern|worked|engineer)', text_lower))
        profile["experience"] = min(3, exp_hits)

    # ------------------------
    # 🌍 OPENSOURCE SIGNAL
    # ------------------------
    if re.search(r'(open source|github|contribution)', text_lower):
        profile["opensource"] = 1

    # ------------------------
    # 🗣 SOFT SKILLS (REAL SIGNAL)
    # ------------------------
    soft_hits = len(re.findall(r'(leadership|communication|teamwork|management)', text_lower))
    profile["soft_skills"] = min(10, 5 + soft_hits)

    # ------------------------
    # 🚀 FINAL NORMALIZATION
    # ------------------------
    profile["projects"] = max(1, profile["projects"])
    profile["experience"] = max(0, profile["experience"])

    return profile