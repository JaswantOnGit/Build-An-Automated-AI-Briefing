"""
Automated AI Briefing Agent
Author: Jaswant Singh
Delivers personalized daily AI/tech summaries to Telegram via scheduled cron jobs.
"""

import os
import requests
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
SEARCH_TOPICS = [
    "generative AI tools",
    "AI automation",
    "AWS machine learning",
    "project management AI"
]


def send_telegram_message(message: str) -> None:
    """Send a formatted message to Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        logger.info("Briefing delivered successfully.")
    else:
        logger.error(f"Failed to send message: {response.text}")


def fetch_search_results(topic: str) -> list:
    """
    Placeholder for web search integration.
    Replace with actual API call (Serper, Brave Search, DuckDuckGo API).
    """
    logger.info(f"Searching for: {topic}")
    return [
        {
            "title": f"Sample result for '{topic}'",
            "url": "https://example.com",
            "snippet": "Latest developments in this area..."
        }
    ]


def generate_briefing_summary(results: list, topic: str) -> str:
    """Format search results into a readable briefing section."""
    lines = [f"*{topic}*"]
    for r in results[:3]:
        lines.append(f"- [{r['title']}]({r['url']})")
        lines.append(f"  _{r['snippet']}_")
    return "\n".join(lines)


def run_daily_briefing() -> None:
    """Main entry point: fetch, summarize, and deliver the daily briefing."""
    date_str = datetime.now().strftime("%A, %B %d %Y")
    briefing_parts = [f"*Daily AI Briefing - {date_str}*\n"]

    for topic in SEARCH_TOPICS:
        results = fetch_search_results(topic)
        summary = generate_briefing_summary(results, topic)
        briefing_parts.append(summary)

    full_briefing = "\n\n".join(briefing_parts)
    send_telegram_message(full_briefing)
    logger.info("Daily briefing complete.")


if __name__ == "__main__":
    run_daily_briefing()
