from pytrends.request import TrendReq
import feedparser

def get_trending_topic():
    # Try Google Trends
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        trending = pytrends.trending_searches(pn="united_states")
        for topic in trending[:10]:
            topic_str = str(topic)
            if any(kw in topic_str.lower() for kw in ['ai', 'chatgpt', 'openai', 'tech', 'robot', 'deep learning']):
                return topic_str
    except Exception as e:
        print(f"Google Trends failed: {e}")

    # Fallback: RSS Feed (TechCrunch AI)
    try:
        feed = feedparser.parse("https://techcrunch.com/tag/artificial-intelligence/feed/")
        return feed.entries[0].title
    except Exception as e:
        print(f"RSS failed: {e}")
        return "Latest AI Breakthrough"
