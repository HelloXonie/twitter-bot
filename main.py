#!/bin/python3

import tweepy
from dotenv import load_dotenv
import os
load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")

print(CONSUMER_KEY)
print(tweepy.__version__)


#client = tweepy.Client(
#        consumer_key=,
#        consumer_secret=,
#        access_token=,
#        access_token_secret=,
#        )


