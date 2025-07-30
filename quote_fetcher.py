from sentence_transformers import SentenceTransformer, util

# ✅ Load the pre-trained model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ Mini database of famous philosophy quotes (can be expanded or loaded from a real dataset)
known_quotes = [
    {"quote": "Cogito, ergo sum", "author": "René Descartes"},
    {"quote": "The unexamined life is not worth living.", "author": "Socrates"},
    {"quote": "To be is to be perceived.", "author": "George Berkeley"},
    {"quote": "Man is condemned to be free.", "author": "Jean-Paul Sartre"},
    {"quote": "Happiness is not an ideal of reason but of imagination.", "author": "Immanuel Kant"},
    {"quote": "One cannot step twice in the same river.", "author": "Heraclitus"},
    {"quote": "God is dead.", "author": "Friedrich Nietzsche"},
    {"quote": "Liberty consists in doing what one desires.", "author": "John Stuart Mill"},
    {"quote": "I can control my passions and emotions if I can understand their nature.", "author": "Spinoza"},
    {"quote": "Hell is other people.", "author": "Jean-Paul Sartre"},
]

# ✅ Pre-compute embeddings
quote_texts = [q["quote"] for q in known_quotes]
quote_embeddings = model.encode(quote_texts, convert_to_tensor=True)

def search_quote_in_dataset(user_quote):
    user_embedding = model.encode(user_quote, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(user_embedding, quote_embeddings)[0]
    best_score = float(similarities.max())
    best_idx = int(similarities.argmax())

    if best_score >= 0.60:
        best_quote = known_quotes[best_idx]
        return True, best_quote["quote"], best_quote["author"]

    # Fallback: Rule-based match for known paraphrases
    quote_lower = user_quote.lower()
    if "i think" in quote_lower and "i am" in quote_lower:
        return True, "Cogito, ergo sum", "René Descartes"

    return False, None, None
