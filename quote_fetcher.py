# quote_fetcher.py

import requests
import os
from dotenv import load_dotenv

# برای لوکال اجرا می‌کنیم تا توکن HuggingFace رو بخونه
load_dotenv()

# توکن باید در فایل .env یا st.secrets تنظیم بشه
HUGGINGFACE_TOKEN = os.getenv("HF_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {HUGGINGFACE_TOKEN}"
}

# URL اصلی برای بررسی دسترسی به دیتاست
API_URL = "https://huggingface.co/api/datasets/vicgalle/philosophy_quotes"

def verify_quote_access():
    """بررسی می‌کنه آیا توکن اجازه دسترسی به دیتاست رو داره یا نه"""
    try:
        response = requests.get(API_URL, headers=HEADERS)
        return response.status_code == 200
    except Exception as e:
        print("❌ Error:", e)
        return False
