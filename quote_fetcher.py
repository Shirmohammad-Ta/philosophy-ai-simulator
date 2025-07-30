# quote_fetcher.py — Smart semantic mapping version

import requests
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer, util

load_dotenv()

HUGGINGFACE_TOKEN = os.getenv("HF_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {HUGGINGFACE_TOKEN}",
    "Content-Type": "application/json"
}

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Cached dataset (limited for performance)
CACHED_QUOTES = []
CACHED_AUTHORS = []

def load_sample_quotes(limit=1000):
    global CACHED_QUOTES, CACHED_AUTHORS
    if not CACHED_QUOTES:
        url = f"https://datasets-server.huggingface.co/rows?dataset=vicgalle/philosophy_quotes&config=default&split=train&limit={limit}"
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            for row in data["rows"]:
                CACHED_QUOTES.append(row["row"]["quote"])
                CACHED_AUTHORS.append(row["row"].get("author", "Unknown"))

# Semantic mapper
def search_quote_in_dataset(quote):
    load_sample_quotes()
    if not CACHED_QUOTES:
        return False, None, None

    # Embed input quote
    input_emb = model.encode(quote, convert_to_tensor=True)
    quote_embs = model.encode(CACHED_QUOTES, convert_to_tensor=True)

    similarities = util.cos_sim(input_emb, quote_embs)[0]
    best_idx = int(similarities.argmax())
    best_score = float(similarities[best_idx])

    # Dynamic thresholding
    if best_score > 0.60:
        matched_quote = CACHED_QUOTES[best_idx]
        matched_author = CACHED_AUTHORS[best_idx]
        return True, matched_quote, matched_author
    else:
        # Try rough mapping: manually map known popular quote patterns
        if "i think" in quote.lower() and "i am" in quote.lower():
            return True, "Cogito, ergo sum", "René Descartes"
        return False, None, None
