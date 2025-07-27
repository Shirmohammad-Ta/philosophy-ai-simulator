
import csv

def load_quote_database(csv_file='quotes.csv'):
    quote_db = {}
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                quote = row.get("quote", "").strip()
                author = row.get("author", "").strip()
                if quote and author:
                    quote_db[quote] = author
    except Exception as e:
        print(f"Error loading quote database: {e}")
    return quote_db

if __name__ == '__main__':
    db = load_quote_database()
    print(f"✅ Loaded {len(db)} quotes.")
