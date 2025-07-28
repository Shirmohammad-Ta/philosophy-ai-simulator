# scrape_philosophy_quotes.py

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://1000wordphilosophy.com"

def get_article_links():
    """Scrape the main archive page to get links to philosophy articles."""
    archive_url = f"{BASE_URL}/archive/"
    res = requests.get(archive_url)
    soup = BeautifulSoup(res.text, "html.parser")

    links = []
    for li in soup.select("li > a"):
        href = li.get("href")
        if href and href.startswith("https://1000wordphilosophy.com/20"):
            links.append(href)
    return links

def extract_summary_and_title(url):
    """Extract title and main paragraph from article page."""
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.find("h1").text.strip()
    paras = soup.find_all("p")
    text = " ".join([p.text.strip() for p in paras[:3]])  # first 3 paragraphs
    return {
        "title": title,
        "url": url,
        "summary": text
    }

if __name__ == "__main__":
    print("Fetching article links...")
    article_urls = get_article_links()
    print(f"Found {len(article_urls)} articles. Extracting samples...")

    for i, url in enumerate(article_urls[:10]):  # just a sample
        data = extract_summary_and_title(url)
        print(f"📝 {data['title']}")
        print(data["summary"][:300] + "...")
        print("------")
