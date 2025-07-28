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
    prompt = f"""You are a philosophy expert. 
Which philosopher is most likely to have said the following quote?
Quote: "{quote}"
Answer only with the name of the philosopher (e.g., Nietzsche, Sartre, Kant, etc.). If you're unsure, say "Unknown".
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
    quote = "He who has a why to live can bear almost any how."
    author = detect_author(quote)
    print("Detected author:", author)
