import requests

def tts(text, config):
    api_key = config["elevenlabs"]["api_key"]
    voice_id = config["elevenlabs"]["voice_id"]
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {"stability": 0.7, "similarity_boost": 0.8}
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        with open("assets/voiceover.mp3", "wb") as f:
            f.write(response.content)
        print("✅ Voiceover saved.")
    except Exception as e:
        print(f"❌ ElevenLabs error: {e}")
        # Fallback: create silent audio or use gTTS
        with open("assets/voiceover.mp3", "w") as f:
            f.write("")
