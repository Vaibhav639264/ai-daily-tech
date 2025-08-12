import requests

def generate(topic, config):
    prompt = f"""
    Write a 90-second YouTube/Instagram script about '{topic}'.
    - Start with a hook like 'You won't believe what happened in AI today!'
    - Explain simply in 120 words
    - Add one surprising fact
    - End with 'Follow for more AI news!'
    - No markdown, no asterisks.
    """
    try:
        res = requests.post(
            f"{config['ollama']['host']}/api/generate",
            json={"model": config['ollama']['model'], "prompt": prompt},
            timeout=60
        )
        return res.json()["response"].strip()
    except Exception as e:
        print(f"Ollama error: {e}")
        return f"Today in AI: {topic}. Scientists made progress. Stay tuned for more!"
