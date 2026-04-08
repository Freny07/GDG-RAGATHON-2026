def generate_explanation(profile, score, interviews):
    explanation = f"""
Your predicted placement readiness score is {round(score, 2)}.

Strengths:
- Skills: {profile['skills']}
- Projects: {profile['projects']}

Areas to improve:
- Increase internships
- Improve DSA and system design

Suggestions:
- Practice LeetCode regularly
- Build 1–2 strong projects
- Prepare using interview experiences

Relevant Interviews:
"""

    for i, interview in enumerate(interviews[:2]):
        explanation += f"\n---\n{interview[:200]}...\n"

    return explanation