from app.config import GEMINI_API_KEY, MODEL_NAME

try:
    import google.generativeai as genai
    genai.configure(api_key=GEMINI_API_KEY)
    _HAS_GENAI = True
except Exception:
    _HAS_GENAI = False

def analyze_text_with_gemini(text: str, max_output_tokens: int = 500) -> dict:
    """
    Send text to Gemini and request: summary, key-points, tone, suggested title.
    Returns dict: {summary, key_points, title, tone}
    """
    if not _HAS_GENAI:
        return {"error": "Gemini client not installed or GEMINI_API_KEY missing."}

    system = "You are an expert web content analyzer. Provide concise outputs."
    user_prompt = (
        "Analyze the following page content and return JSON with keys: title, summary, key_points (list of 5 short points), "
        "tone (one-word), suggested_tags (comma-separated). Respond only with JSON.\n\n"
        f"Content:\n\n{text[:4000]}"  # limit input size; for long pages chunking would be needed
    )

    resp = genai.chat.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2,
        max_output_tokens=max_output_tokens
    )

    # different library versions return in different fields:
    result_text = ""
    try:
        result_text = resp.last or resp.get("candidates", [{}])[0].get("content", "")
    except Exception:
        result_text = str(resp)

    # try to parse JSON from result_text
    import json
    try:
        data = json.loads(result_text)
        return data
    except Exception:
        # fallback: return raw text
        return {"raw": result_text}
