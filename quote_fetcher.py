import requests
from sentence_transformers import SentenceTransformer, util

# Load transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample fallback quotes
known_quotes = [
    {"quote": "Cogito, ergo sum", "author": "René Descartes"},
    {"quote": "The unexamined life is not worth living.", "author": "Socrates"},
    {"quote": "To be is to be perceived.", "author": "George Berkeley"},
    {"quote": "Man is condemned to be free.", "author": "Jean-Paul Sartre"},
    {"quote": "God is dead.", "author": "Friedrich Nietzsche"},
]

# Encode fallback quotes
quote_texts = [q["quote"] for q in known_quotes]
quote_embeddings = model.encode(quote_texts, convert_to_tensor=True)

def search_quote_in_dataset(user_quote):
    try:
        # 1. Try online Philosophy API
        response = requests.get("https://philosophyapi.pythonanywhere.com/api/ideas/")
        if response.status_code == 200:
            data = response.json().get("results", [])
            for item in data:
                if user_quote.strip().lower() == item["quote"].strip().lower():
                    return True, item["quote"], item["author"]
    except Exception as e:
        print("API failed, fallback activated:", e)

    # 2. Semantic fallback
    user_emb = model.encode(user_quote, convert_to_tensor=True)
    similarities = util.cos_sim(user_emb, quote_embeddings)[0]
    idx = int(similarities.argmax())
    if float(similarities[idx]) > 0.6:
        match = known_quotes[idx]
        return True, match["quote"], match["author"]

    # 3. Rule-based backup
    if "i think" in user_quote.lower() and "i am" in user_quote.lower():
        return True, "Cogito, ergo sum", "René Descartes"

    return False, None, None
