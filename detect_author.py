# detect_author.py
from transformers import pipeline

# Load the model (only once, can be cached)
pipe = pipeline("text2text-generation", model="google/flan-t5-base")

def detect_author(quote):
    prompt = f"Who is the author of the following philosophical quote?\nQuote: {quote}"
    result = pipe(prompt, max_new_tokens=20)[0]['generated_text']
    return result.strip()

# Example usage:
if __name__ == "__main__":
    sample_quote = "He who has a why to live can bear almost any how."
    author = detect_author(sample_quote)
    print("Detected author:", author)
