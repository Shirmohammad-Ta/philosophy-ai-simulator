# detect_author_api.py
import requests

def detect_author(quote):
    """
    Detects the philosopher who said the given quote using a free online philosophy API.
    Returns the author's name if found, otherwise returns "Unknown".
    """
    try:
        params = {"search": quote}
        res = requests.get("https://philosophyapi.pythonanywhere.com/api/ideas/", params=params, timeout=10)
        data = res.json()
        results = data.get("results", [])
        if results:
            return results[0]["author"]
        return "Unknown"
    except Exception as e:
        return "Error or Unknown"

# Example usage
if __name__ == "__main__":
    quote = "I think, therefore I am."
    author = detect_author(quote)
    print("Detected author:", author)
