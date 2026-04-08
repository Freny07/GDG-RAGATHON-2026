from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def extract_profile(text):
    prompt = f"""
Extract student profile into JSON:

{{
  "academic_score": float,
  "dsa": int,
  "projects": int,
  "experience": int,
  "opensource": int,
  "soft_skills": int,
  "tech_stack": int,
  "skills": list
}}

Text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return eval(response.choices[0].message.content)