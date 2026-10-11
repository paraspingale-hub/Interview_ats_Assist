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

    # Keep the provider order explicit: cloud provider first, then the
    # secondary cloud provider, then the local model that does not require a key.
    providers = [
        ("Groq", call_groq),
        ("Gemini", call_gemini),
        ("Ollama", call_ollama),
    ]

    for provider_name, provider_call in providers:
        print(f"Attempting to call {provider_name}...")
        try:
            response = provider_call(prompt)
        except Exception as exc:
            response = f"❌ Error: {exc}"

        if not isinstance(response, str) or not response.strip():
            response = "❌ Error: Empty response."
        elif not response.strip().startswith("❌ Error:"):
            return response
        print(f"{provider_name} failed: {response}")
        errors.append(f"{provider_name}: {response}")

    # If all 3 fail, return a combined error message
    combined_errors = "\n\n".join(errors)
    return f"❌ All AI models failed.\n\n{combined_errors}"

def call_gemini(prompt: str) -> str:
    api_key = os.getenv("REDACTED_API_KEY")
    if not api_key:
        return "❌ Error: GEMINI_API_KEY is not set."
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
    api_key = os.getenv("REDACTED_API_KEY")
    if not api_key:
        return "❌ Error: GROQ_API_KEY not set."
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
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
        "model": os.getenv("OLLAMA_MODEL", "llama3:latest"),
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
