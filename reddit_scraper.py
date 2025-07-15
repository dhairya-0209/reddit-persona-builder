import praw
import os

class RedditScraper:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT"),
            check_for_async=False  # ✅ Add this line
        )

    def fetch_user_data(self, username, limit=100):
        user = self.reddit.redditor(username)
        posts = []
        comments = []

        for submission in user.submissions.new(limit=limit):
            posts.append({
                "title": submission.title,
                "selftext": submission.selftext,
                "url": f"https://www.reddit.com{submission.permalink}"
            })

        for comment in user.comments.new(limit=limit):
            comments.append({
                "body": comment.body,
                "url": f"https://www.reddit.com{comment.permalink}"
            })

        return posts, comments
