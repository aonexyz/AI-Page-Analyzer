from flask import Flask, request, jsonify, render_template
from app.fetcher import fetch_url
from app.ai_client import analyze_text_with_gemini
from app.config import HOST, PORT

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.json or {}
    url = data.get("url")
    text = data.get("text")
    if not url and not text:
        return jsonify({"error": "Provide 'url' or 'text' in JSON body."}), 400

    try:
        if url:
            content = fetch_url(url)
        else:
            content = text
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # For large content, production code should chunk -> map-reduce; here we pass truncated content
    try:
        result = analyze_text_with_gemini(content)
    except Exception as e:
        return jsonify({"error": f"AI analysis failed: {e}"}), 500

    return jsonify({"result": result, "preview": content[:2000]})

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
