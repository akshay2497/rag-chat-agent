import requests
import os

GEMINI_API_KEY = 'XXX'

def generate_response_with_history(conversation_history):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": conversation_history
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        try:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return "No answer could be generated from Gemini API."
    else:
        return f"Gemini API Error: {response.status_code}, {response.text}"
