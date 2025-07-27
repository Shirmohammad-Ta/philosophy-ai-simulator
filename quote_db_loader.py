
import csv

def load_quote_database(csv_file='quotes.csv'):
    quotes = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'quote' in row:
                    quotes.append(row['quote'].strip())
    except Exception as e:
        print(f"Error loading quotes: {e}")
    return quotes

if __name__ == '__main__':
    db = load_quote_database()
    print(f"✅ Loaded {len(db)} quotes.")
