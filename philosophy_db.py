# philosophy_db.py

from datasets import load_dataset
import random

# بارگذاری دیتاست فلسفی (اولین بار از اینترنت می‌گیره، بعد کش می‌شه)
dataset = load_dataset("vicgalle/philosophy_quotes", split="train")

# استخراج جمله‌ها
quotes = [item["quote"] for item in dataset]

# بررسی اینکه آیا جمله کاربر توی دیتاست وجود داره یا نه
def is_in_database(user_input):
    return any(user_input.lower() in quote.lower() for quote in quotes)

# گرفتن یک جمله فلسفی تصادفی
def get_random_quote():
    return random.choice(quotes)

# فقط برای تست مستقیم
if __name__ == "__main__":
    print("✅ Sample quote:", get_random_quote())
