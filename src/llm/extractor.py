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
        "tech_stack": 5,
        "skills": []
    }

    # ------------------------
    # 🎓 ACADEMICS (GENERAL)
    # ------------------------
    cgpa = re.findall(r'(\d\.\d{1,2})\s*(cgpa|gpa)', text_lower)
    percent = re.findall(r'(\d{2,3})\s*%', text_lower)
    percentile = re.findall(r'(\d{2,3})\s*percentile', text_lower)

    if cgpa:
        profile["academic_score"] = float(cgpa[0][0])

    elif percentile:
        val = int(percentile[0])
        profile["academic_score"] = min(10, val / 10)

    elif percent:
        val = int(percent[0])
        profile["academic_score"] = min(10, val / 10)

    # ------------------------
    # 💻 SKILLS (GENERAL + SECTION AWARE)
    # ------------------------
    SKILLS_DB = [
        "python", "java", "c++", "c", "javascript", "typescript",
        "react", "node", "express", "mongodb", "sql", "mysql",
        "html", "css", "bash", "linux", "docker", "kubernetes",
        "aws", "azure", "gcp", "tensorflow", "pytorch", "ml",
        "ai", "nlp", "data science", "go", "golang"
    ]

    # Try extracting skills section
    skills_section_match = re.search(
        r'(skills|technical skills)(.*?)(experience|projects|education)',
        text_lower,
        re.S
    )

    skills_text = skills_section_match.group(2) if skills_section_match else text_lower

    found_skills = []

    for skill in SKILLS_DB:
        if re.search(rf'\b{skill}\b', skills_text):
            if skill in ["ml", "ai", "nlp", "sql"]:
                found_skills.append(skill.upper())
            elif skill == "c++":
                found_skills.append("C++")
            elif skill in ["go", "golang"]:
                found_skills.append("Go")
            else:
                found_skills.append(skill.capitalize())

    profile["skills"] = list(set(found_skills)) if found_skills else ["General Programming"]

    # ------------------------
    # 🧠 DSA DETECTION
    # ------------------------
    if re.search(r'(dsa|data structures|algorithms|problem solving)', text_lower):
        profile["dsa"] = 7

    # ------------------------
    # 📦 PROJECTS (NUMBER-AWARE + FALLBACK)
    # ------------------------
    proj_num = re.search(r'projects?\s*[:\-]?\s*(\d+)', text_lower)

    if proj_num:
        profile["projects"] = min(5, int(proj_num.group(1)))

    else:
        project_section = re.search(
            r'(projects)(.*?)(experience|education|skills)',
            text_lower,
            re.S
        )

        if project_section:
            projects_text = project_section.group(2)
            project_count = len(re.findall(r'•|\-|\*', projects_text))
            profile["projects"] = max(1, min(5, project_count))
        else:
            # infer from verbs
            if re.search(r'(built|developed|created)', text_lower):
                profile["projects"] = 1

    # ------------------------
    # 💼 EXPERIENCE (NUMBER-AWARE)
    # ------------------------
    exp_num = re.search(r'(internships?|experience)\s*[:\-]?\s*(\d+)', text_lower)

    if exp_num:
        profile["experience"] = min(3, int(exp_num.group(2)))

    else:
        exp_section = re.search(
            r'(experience)(.*?)(projects|education|skills)',
            text_lower,
            re.S
        )

        if exp_section:
            exp_text = exp_section.group(2)
            exp_count = len(re.findall(r'•|\-|\*', exp_text))
            profile["experience"] = min(3, exp_count)
        else:
            if re.search(r'(intern|worked|experience)', text_lower):
                profile["experience"] = 1

    # ------------------------
    # 🌍 OPENSOURCE
    # ------------------------
    if re.search(r'(open source|github)', text_lower):
        profile["opensource"] = 1

    # ------------------------
    # 🗣 SOFT SKILLS
    # ------------------------
    if re.search(r'(leadership|communication|teamwork)', text_lower):
        profile["soft_skills"] = 7

    # ------------------------
    # ⚙️ TECH STACK DEPTH
    # ------------------------
    profile["tech_stack"] = min(10, len(profile["skills"]))

    return profile