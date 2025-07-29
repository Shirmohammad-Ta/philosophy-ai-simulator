# quote_attributor.py
import requests

def guess_author(sentence):
    try:
        response = requests.get(f"https://api.quotable.io/search/quotes?query={sentence}")
        data = response.json()
        if data and data.get("count", 0) > 0:
            return data["results"][0]["author"]
        else:
            return "Unknown or Not Attributed"
    except Exception as e:
        return f"Error: {e}"
