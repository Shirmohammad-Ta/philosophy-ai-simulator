# quote_fetcher.py

import requests
import os
from dotenv import load_dotenv

# برای لوکال اجرا می‌کنیم تا توکن HuggingFace رو بخونه
load_dotenv()

# توکن Hugging Face باید در فایل .env یا st.secrets قرار گیرد
HUGGINGFACE_TOKEN = os.getenv("HF_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {HUGGINGFACE_TOKEN}",
    "Content-Type": "application/json"
}

# 🔍 تابع برای جست‌وجوی یک جمله خاص در دیتاست vicgalle/philosophy_quotes
def search_quote_in_dataset(quote):
    url = "https://datasets-server.huggingface.co/search"
    payload = {
        "dataset": "vicgalle/philosophy_quotes",
        "query": quote
    }

    try:
        response = requests.post(url, json=payload, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            hits = data.get("hits", [])
            if hits:
                matched_quote = hits[0]["row"]["quote"]
                author = hits[0]["row"].get("author", "Unknown")
                return True, matched_quote, author
            else:
                return False, None, None
        else:
            return False, None, None
    except Exception as e:
        print("❌ Error in API search:", e)
        return False, None, None
