import tweepy
from dotenv import load_dotenv
import os
import pyshorteners

shortener = pyshorteners.Shortener()

def get_client():
    load_dotenv()

    client = tweepy.Client(
        consumer_key=os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
        )
    return client

def create_tweet(client, article):
    title = posts.title
    author = posts.author
    link = shortener.tinyurl.short(posts.link)

    tweet_text = f"Title: {title}\nAuthor: {author}\n\n{link}"
    print(tweet_text)
    #client.create_tweet(text=tweet_text)
