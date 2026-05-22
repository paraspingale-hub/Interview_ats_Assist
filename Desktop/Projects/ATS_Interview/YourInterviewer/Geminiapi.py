import requests
import os

# Function 1: Generate Questions
def ask_llm(domain: str, difficulty: str) -> str:
    prompt = f"""Generate 5 actual interview questions for {domain} at {difficulty} level.
Output them strictly as a numbered list where each question is on a new line, like this:
1. What is...
2. Explain...
Do not include conversational filler or titles."""

    return call_gemini(prompt)

# Function 2: Evaluate Answers (For the MockInterviewAgent)
def evaluate_with_gemini(prompt: str) -> str:
    return call_gemini(prompt)

# Core API call logic
def call_gemini(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY", "AIzaSyAF4f1IRy-FxaBHgzRhPWPfNFPkbewhnkI")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120) 
        response.raise_for_status()
        result = response.json()
        answer = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text")
        return answer if answer else "❌ Error: No response."
    except Exception as e:
        return f"❌ Error: {e}"