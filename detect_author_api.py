# detect_author_api.py
import requests

def detect_author(quote):
    """
    Detects the philosopher who said the given quote using a free online philosophy API.
    Returns the author's name if found, otherwise returns "Unknown".
    """
    try:
        response = requests.get(
            "https://philosophyapi.pythonanywhere.com/api/ideas/",
            params={"search": quote},
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            if results:
                return results[0]["author"]
            else:
                return "Unknown"
        else:
            return f"Error: HTTP {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    quote = "I think, therefore I am"
    author = detect_author(quote)
    print("Detected author:", author)
