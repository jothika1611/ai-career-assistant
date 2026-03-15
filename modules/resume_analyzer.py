from modules.generator import generate

def analyze_resume(resume_text: str) -> str:

    prompt = f"""
You are an AI career assistant.

Analyze the following resume and generate a professional structured report.

The report MUST include these sections:

1. Resume Score (0–100)
   - Give an overall score for the resume.
   - Briefly explain why this score was given.

2. Candidate Summary
   - Brief overview of the candidate profile.

3. Skills Analysis
   Strengths:
   Weaknesses:

4. Experience Evaluation
   - Evaluate the candidate's experience level.

5. Improvement Suggestions
   - Specific actionable suggestions to improve the resume.

6. Recommended Additions
   - Sections the resume should include (projects, certifications, achievements, etc.).

IMPORTANT RULES:
- Do NOT ask the user any questions.
- Do NOT request more information.
- Only generate the report.

Resume:
{resume_text}
"""

    return generate(prompt)