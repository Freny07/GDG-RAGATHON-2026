from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_explanation(profile, score, interviews):
    prompt = f"""
Profile: {profile}
Score: {score}
Interviews: {interviews}

Explain:
- Why this score
- Weak areas
- Improvement roadmap
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content