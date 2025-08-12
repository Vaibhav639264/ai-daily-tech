# scripts/download_background.py
import requests
import os
import json
import random
from urllib.parse import urlparse

PEXELS_API_KEY = None

def download_background(config, query_hint=""):
    global PEXELS_API_KEY
    PEXELS_API_KEY = config["pexels_api_key"]
    
    # Build search query
    base_query = config.get("video_search_query", "technology")
    query = f"{base_query} {query_hint}".strip()

    headers = {"Authorization": PEXELS_API_KEY}
    url = "https://api.pexels.com/videos/search"
    params = {
        "query": query,
        "per_page": 5,
        "orientation": "portrait",  # 9:16 for Reels
        "size": "medium"
    }

    print(f"🔍 Searching Pexels for: {query}")
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("❌ Pexels API error:", response.text)
        return None

    data = response.json()
    videos = data.get("videos", [])

    if not videos:
        print("❌ No videos found. Trying generic 'ai loop'")
        if query != "ai loop":
            return download_background(config, "ai loop")
        return None

    # Pick a random video (avoid always using #1)
    video = random.choice(videos)
    video_url = None

    # Get the best-quality video link
    for vid in video['video_files']:
        if vid['quality'] == 'hd' or vid['quality'] == 'sd':
            video_url = vid['link']
            break

    if not video_url:
        video_url = video['video_files'][0]['link']

    # Download
    filename = "assets/background.mp4"
    print(f"📥 Downloading video: {video_url}")
    
    try:
        video_data = requests.get(video_url)
        with open(filename, 'wb') as f:
            f.write(video_data.content)
        print(f"✅ Background saved: {filename}")
        return filename
    except Exception as e:
        print("❌ Download failed:", e)
        return None
