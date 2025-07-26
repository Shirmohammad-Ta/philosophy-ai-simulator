# quote_db_loader.py

import csv

def load_quote_database(csv_file="quotes.csv"):
    quote_db = {}
    try:
        with open(csv_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                quote = row["quote"].strip()
                author = row["author"].strip()
                quote_db[quote] = author
    except Exception as e:
        print(f"Error loading quote database: {e}")
    return quote_db
