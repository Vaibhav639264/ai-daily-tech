# 🤖 AI Daily Tech

Automated YouTube & Instagram channel for daily AI and tech news.

## 🔧 How It Works
1. Finds trending AI news (Google Trends + RSS)
2. Writes script using **Llama3** (via Ollama)
3. Generates voiceover with **ElevenLabs**
4. Creates video with subtitles
5. Uploads to **YouTube**
6. Runs daily via GitHub Actions

## 🚀 Setup

### 1. Clone repo
```bash
git clone https://github.com/your-username/ai-daily-tech.git
cd ai-daily-tech

1. Install Ollama
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3

2. Install Python package
pip install -r requirements.txt

3. Set up YouTube API
Go to Google Cloud Console
Create project → Enable YouTube Data API v3
Download credentials.json → place in root

4. Create Config.json
cp config.json.example config.json
Edit with your keys.

5. Add stock video
Download a 9:16 video from Pexels → save as assets/stock.mp4

6. Run
python main.py

7. Automate Daily
Enable GitHub Actions and add CONFIG_JSON as a secret.

Made with ❤️ by me!
