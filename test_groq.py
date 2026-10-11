import requests
import os

api_key = os.getenv("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
payload = {
    "model": "llama3-8b-8192",
    "messages": [{"role": "user", "content": "Hello"}]
}

try:
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
except Exception as e:
    print(f"Exception: {e}")
