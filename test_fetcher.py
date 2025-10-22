from app.fetcher import extract_text_from_html

def test_extract_basic():
    html = "<html><body><article><p>Hello world</p><p>Second para</p></article></body></html>"
    text = extract_text_from_html(html)
    assert "Hello world" in text
    assert "Second para" in text
