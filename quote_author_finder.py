# quote_author_finder.py
import requests

def guess_author_by_web(sentence):
    """
    Uses quotable.io public API to find the author of a known philosophical or famous quote.
    If the quote is not found, returns "Unknown".
    """
    url = f"https://api.quotable.io/search/quotes?query={sentence}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["count"] > 0:
                return data["results"][0]["author"]
        return "Unknown"
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage:
if __name__ == "__main__":
    sentence = input("Enter a philosophical sentence: ")
    author = guess_author_by_web(sentence)
    print(f"Possible Author: {author}")
