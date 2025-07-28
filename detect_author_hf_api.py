# detect_author_hf_api.py
import requests
import os
from dotenv import load_dotenv

# Load HuggingFace token from .env file
load_dotenv()
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"
}

def detect_author(quote):
    prompt = f"""You are an expert in philosophy and historical literature.
Determine which philosopher most likely said the following quote, based on its language, themes, and style.

Quote: "{quote}"

Respond with only the philosopher's name (e.g., Nietzsche, Sartre, Kant). If unsure, respond "Unknown".
"""
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 20}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    try:
        return result[0]["generated_text"].strip()
    except:
        return "Error or Unknown"

# Example usage
if __name__ == "__main__":
    quote = "What does not kill me makes me stronger."
    author = detect_author(quote)
    print("Detected author:", author)
