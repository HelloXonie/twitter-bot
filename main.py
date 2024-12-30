#!/bin/python3

import tweepy
from dotenv import load_dotenv
import os
import feedparser
from pprint import pprint

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
rss_url = ""

feed = feedparser.parse(rss_url)
pprint(feed)
