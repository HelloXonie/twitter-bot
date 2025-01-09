#!/bin/python3

import feedparser
from pprint import pprint
from posts import Posts
from twitter import get_client, create_tweet

print(tweepy.__version__)

#URL of RSS feed
rss_url = "https://www.elitefourum.com/latest.rss"

feed = feedparser.parse(rss_url)
first_posts = (feed['entries'][0])

posts = Posts(
        first_posts['author'],
        first_posts['link'],
        first_posts['title'],
        )

client = get_client()
create_tweet(client, posts)

#print(posts)


