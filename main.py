import os
from dotenv import load_dotenv
from reddit_scraper import RedditScraper
from persona_builder import build_user_persona

load_dotenv()


usernames = ["kojied", "Hungry-Move-6603", "spez", "example_user",]


scraper = RedditScraper()

for username in usernames:
    print(f"\n🔍 Scraping Reddit user: {username}")
    posts, comments = scraper.fetch_user_data(username)
    print(f"✅ Fetched {len(posts)} posts and {len(comments)} comments.")

    print(f"🧠 Generating persona for: {username}")
    build_user_persona(username, posts, comments)
