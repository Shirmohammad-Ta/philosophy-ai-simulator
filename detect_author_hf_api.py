# detect_author_hf_api.py
import requests
import os
from dotenv import load_dotenv

# Load HuggingFace token from .env file
load_dotenv()
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"
}

def detect_author(quote):
    prompt = f"""The following quote is attributed to one of the most well-known philosophers.
Your task is to identify the most likely author of this quote, based on their known philosophical ideas and writing style.

Quote: "{quote}"

Respond only with the name of the philosopher (e.g., Nietzsche, Sartre, Kant). If unsure, say "Unknown".
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
