# quote_fetcher.py

import requests
import os
import difflib
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer, util

load_dotenv()

HUGGINGFACE_TOKEN = os.getenv("HF_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {HUGGINGFACE_TOKEN}",
    "Content-Type": "application/json"
}

# Load model for semantic similarity
model = SentenceTransformer("all-MiniLM-L6-v2")

# Cache a sample of the dataset for local fuzzy matching (sampled version)
CACHED_QUOTES = []
CACHED_AUTHORS = []

def load_sample_quotes():
    global CACHED_QUOTES, CACHED_AUTHORS
    if not CACHED_QUOTES:
        # Try loading small sample from Hugging Face API
        url = "https://datasets-server.huggingface.co/rows?dataset=vicgalle/philosophy_quotes&config=default&split=train&limit=500"
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            for row in data["rows"]:
                CACHED_QUOTES.append(row["row"]["quote"])
                CACHED_AUTHORS.append(row["row"].get("author", "Unknown"))

# Semantic + fuzzy search
def search_quote_in_dataset(quote):
    load_sample_quotes()
    if not CACHED_QUOTES:
        return False, None, None

    # Encode input
    input_emb = model.encode(quote, convert_to_tensor=True)
    quote_embs = model.encode(CACHED_QUOTES, convert_to_tensor=True)

    # Compute similarities
    similarities = util.cos_sim(input_emb, quote_embs)[0]
    best_idx = int(similarities.argmax())
    best_score = float(similarities[best_idx])

    # Threshold
    if best_score > 0.6:
        return True, CACHED_QUOTES[best_idx], CACHED_AUTHORS[best_idx]
    else:
        return False, None, None
