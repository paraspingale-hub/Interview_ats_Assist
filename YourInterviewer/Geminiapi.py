import requests
import os

# Function 1: Generate Questions
def ask_llm(domain: str, difficulty: str) -> str:
    prompt = f"""Generate 15 actual interview questions for {domain} at {difficulty} level.
Output them strictly as a numbered list where each question is on a new line, like this:
1. What is...
2. Explain...
Do not include conversational filler or titles."""

    return call_llm_with_fallback(prompt)

# Function 2: Evaluate Answers (For the MockInterviewAgent)
def evaluate_with_gemini(prompt: str) -> str:
    return call_llm_with_fallback(prompt)

# Core API call logic with fallbacks
def call_llm_with_fallback(prompt: str) -> str:
    errors = []
    
    # 1. Try Gemini first
    print("Attempting to call Gemini API...")
    gemini_response = call_gemini(prompt)
    if not gemini_response.startswith("❌ Error:"):
        return gemini_response
    print(f"Gemini API failed: {gemini_response}")
    errors.append(f"Gemini: {gemini_response}")

    # 2. If Gemini fails, try Groq
    print("Attempting to call Groq API...")
    groq_response = call_groq(prompt)
    if not groq_response.startswith("❌ Error:"):
        return groq_response
    print(f"Groq API failed: {groq_response}")
    errors.append(f"Groq: {groq_response}")

    # 3. If Groq fails, try Local LLM (Ollama)
    print("Attempting to call Local LLM (Ollama)...")
    local_response = call_ollama(prompt)
    if not local_response.startswith("❌ Error:"):
        return local_response
    print(f"Ollama failed: {local_response}")
    errors.append(f"Ollama: {local_response}")

    # If all 3 fail, return a combined error message
    combined_errors = "\n\n".join(errors)
    return f"❌ All AI models failed.\n\n{combined_errors}"

def call_gemini(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY", "REDACTED_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30) 
        if response.status_code != 200:
            return f"❌ Error: {response.status_code} - {response.text}"
        result = response.json()
        answer = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text")
        return answer if answer else "❌ Error: No response."
    except Exception as e:
        return f"❌ Error: {e}"

def call_groq(prompt: str) -> str:
    api_key = os.getenv("GROQ_API_KEY", "REDACTED_API_KEY")
    if not api_key:
        return "❌ Error: GROQ_API_KEY not set."
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-8b-8192",  # Reverted to default to see exact 400 error
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        if response.status_code != 200:
            return f"❌ Error: {response.status_code} - {response.text}"
        result = response.json()
        answer = result.get("choices", [{}])[0].get("message", {}).get("content")
        return answer if answer else "❌ Error: No response from Groq."
    except Exception as e:
        return f"❌ Error: {e}"

def call_ollama(prompt: str) -> str:
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "qwen3.5",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=120)
        if response.status_code != 200:
            return f"❌ Error: {response.status_code} - {response.text}"
        result = response.json()
        answer = result.get("response")
        return answer if answer else "❌ Error: No response from local LLM."
    except Exception as e:
        return f"❌ Error: {e}"
