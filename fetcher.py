import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

HEADERS = {"User-Agent": "ai-page-analyzer/1.0 (+https://github.com/your-username)"}

def fetch_url(url: str, timeout: int = 10) -> str:
    """Fetch URL and return cleaned text content."""
    resp = requests.get(url, headers=HEADERS, timeout=timeout)
    resp.raise_for_status()
    html = resp.text
    return extract_text_from_html(html, base_url=url)

def extract_text_from_html(html: str, base_url: str = "") -> str:
    soup = BeautifulSoup(html, "html.parser")

    # remove scripts, styles, nav, footer, aside
    for tag in soup(["script", "style", "nav", "footer", "aside", "header", "noscript", "iframe"]):
        tag.decompose()

    # try to find article/main content
    main = soup.find("article") or soup.find("main")
    if main:
        text = main.get_text(separator="\n")
    else:
        # fallback: collect large <p> blocks
        paragraphs = soup.find_all("p")
        if paragraphs:
            text = "\n\n".join(p.get_text() for p in paragraphs)
        else:
            text = soup.get_text(separator="\n")

    # basic cleaning
    text = re.sub(r'\n\s+\n', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()
