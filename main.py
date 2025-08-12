import os
import json
from scripts.discover_topic import get_trending_topic
from scripts.generate_script import generate
from scripts.text_to_speech import tts
from scripts.create_video import make
from scripts.upload_youtube import upload

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

def main():
    print("🔍 Loading config...")
    config = load_config()
    
    print("🔍 Discovering trending AI topic...")
    topic = get_trending_topic()
    print(f"🎯 Topic: {topic}")

    print("✍️ Generating script...")
    script = generate(topic, config)
    with open("assets/script.txt", "w") as f:
        f.write(script)
    print("📄 Script saved.")

    print("🎙️ Generating voiceover...")
    tts(script, config)
    
    print("🎥 Creating video...")
    make(config, topic)
    
    print("📤 Uploading to YouTube...")
    title = f"Today in AI: {topic}"
    description = f"{script}\n\nFollow for daily AI updates! #TechNews #ArtificialIntelligence"
    tags = ["AI", "Artificial Intelligence", "Tech News", "Machine Learning", "Daily AI"]
    upload("assets/final_video.mp4", title, description, tags, config)
    
    print("✅ Done! Video uploaded.")

if __name__ == "__main__":
    main()
