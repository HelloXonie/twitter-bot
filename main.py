#!/bin/python3

import tweepy
from dotenv import load_dotenv
import os
import feedparser
from pprint import pprint
from post import Posts

print(tweepy.__version__)

def get_client():
    load_dotenv()

    client = tweepy.Client(
        consumer_key=os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
        )
    return client

#URL of RSS feed
rss_url = "https://www.elitefourum.com/latest.rss"

feed = feedparser.parse(rss_url)
pprint(feed['entries'][0])




