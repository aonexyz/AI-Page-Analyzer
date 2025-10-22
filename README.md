# 🧠 AI Page Analyzer — Gemini-powered Web Insight Tool

A lightweight web app built with **Flask + JavaScript** that lets you analyze any webpage or pasted text using **Google Gemini API**.  
It fetches the page, extracts readable content, and summarizes it into **title, summary, key points, tone, and tags** — perfect for quick content analysis or inspiration.

---

## ✨ Features

- 🌐 **URL or Text Input** – Analyze any public webpage or paste content manually.  
- 🤖 **Gemini-powered Summaries** – Uses Gemini AI to generate clean, context-aware insights.  
- 🧩 **Side Panel View** – Interactive UI to show results instantly.  
- 🧱 **Flask Backend + Vanilla JS Frontend** – Lightweight, simple to deploy.  
- 🐳 **Docker Support** – Ready for containerized deployment.  
- 🧪 **Pytest Unit Tests** – Basic tests for fetcher and analyzer.

---

## 🚀 Quickstart

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/ai-page-analyzer.git
cd ai-page-analyzer
```
### 2. Create the .env file
Duplicate the example environment file and add your Gemini API key:
```bash
cp .env.example .env
```
Then open .env and set your real Gemini API key:
```bash
GEMINI_API_KEY=your_real_gemini_api_key_here
MODEL_NAME=gemini-pro
HOST=0.0.0.0
PORT=7860
```
### 3. Install dependencies
```bash
python -m venv .venv
source .venv/bin/activate       # (On Windows: .venv\Scripts\activate)
pip install -r requirements.txt
```
### 4. Run the app
```bash
python -m venv .venv
source .venv/bin/activate       # (On Windows: .venv\Scripts\activate)
pip install -r requirements.txt
```
### 🧠 Example Use
1. Paste a URL like
2. Click Analyze
3. The app will:
 . Fetch the webpage text
 . Send it to Gemini
 . Display the summary, key points, and suggested tags in the side panel

### 🧪 Running tests
```bash
pytest -q
```
### 🐳 Docker setup
Build and run with Docker:
```bash
docker build -t ai-page-analyzer .
docker run -p 7860:7860 --env-file .env ai-page-analyzer
```
### ⚙️ Tech Stack
1. Backend: Python (Flask)
2. Frontend: HTML, CSS, JavaScript
3. AI Model: Google Gemini
4. Database: None (stateless)
5. Testing: Pytest
6. Deployment: Docker / GitHub Actions

### 🧠 Notes
1. The current version processes up to ~4000 characters per request (simple truncation).
For long articles, consider implementing chunked summarization.
2. Works best with Gemini-pro or any model that supports long text input.
3. You can replace google.generativeai with any Gemini REST API client if needed.

## Author

- **A 1** – [GitHub: aonexyz](https://github.com/aonexyzl)

---

## Buy me a coffee ☕
Love the bot? Wanna fuel more WAGMI vibes? Drop some crypto love to keep the charts lit! 🙌
- **SUI**: `0x6e20d8f6c15aeb42887608eec65b29385f21fa21cfd23302c54fabd813d8cd38`
- **USDT (TRC20)**: `TMoPwVpeC8A2yTc5qotKj8gVXaGTqQwc3L`
- **BNB (BEP20)**: `0x068ff5934e0c30d8763012a6faa0033e7fdcc455`
- **Binance UID**:`899350787`

Every bit helps me grind harder and keep this bot stacking bags! 😎

## 🪪 License
MIT License © 2025 
