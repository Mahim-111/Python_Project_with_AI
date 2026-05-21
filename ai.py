from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_resume(resume_text, user_goal):

    prompt = f"""
You are a senior hiring manager.

Analyze the resume for the role: {user_goal}

Return JSON only.

{{
    "skills": [],
    "missing_skills": [],
    "roadmap": [],
    "interview_questions": []
}}

Resume:
{resume_text}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            response_format={"type": "json_object"},
            temperature=0.3,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert career assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return json.loads(
            response.choices[0].message.content
        )

    except Exception as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e)
        }