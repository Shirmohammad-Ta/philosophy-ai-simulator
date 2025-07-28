# detect_author.py
from transformers import pipeline

# Load the model
pipe = pipeline("text2text-generation", model="google/flan-t5-base")

def detect_author(quote):
    prompt = f"""
You are a philosophy expert. Your task is to detect the author of the philosophical quote below.

If you don't know the exact author, say "Unknown".

Quote: "{quote}"

Respond only with the name of the philosopher.
"""
    result = pipe(prompt, max_new_tokens=20)[0]['generated_text']
    return result.strip()

# Example usage:
if __name__ == "__main__":
    sample_quote = "He who has a why to live can bear almost any how."
    author = detect_author(sample_quote)
    print("Detected author:", author)
