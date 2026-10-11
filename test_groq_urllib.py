import urllib.request
import os
import urllib.error
import json

url = "https://api.groq.com/openai/v1/chat/completions"
data = json.dumps({
    "model": "llama3-8b-8192",
    "messages": [{"role": "user", "content": "Hello"}]
}).encode('utf-8')

headers = {
    "Authorization": f"Bearer {os.getenv("GROQ_API_KEY", "")}",
    "Content-Type": "application/json"
}

req = urllib.request.Request(url, data=data, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=30) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.read().decode('utf-8')}")
except Exception as e:
    print(f"Error: {e}")
