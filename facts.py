import praw
import random
import time
import os
from dotenv import load_dotenv


load_dotenv()

reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
reddit_username = os.getenv("REDDIT_USERNAME")
reddit_password = os.getenv("REDDIT_PASSWORD")
reddit_user_agent = os.getenv("REDDIT_USER_AGENT")


reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    username=reddit_username,
    password=reddit_password,
    user_agent=reddit_user_agent
)

def obter_facto_aleatorio_do_reddit():
    try:
        subreddits = ["Awwducational", "DailyFacts", "interestingfacts"]
        subreddit = random.choice(subreddits)
        posts = list(reddit.subreddit(subreddit).hot(limit=50))
        post = random.choice(posts)
        return post.title
    except Exception as e:
        print(f"Error: {e}")
        return None

facto = obter_facto_aleatorio_do_reddit()
if facto:
    print(f"Facto de bosta: {facto}")
else:
    print("O facto perdeu-se no caminho.")
time.sleep(2)
