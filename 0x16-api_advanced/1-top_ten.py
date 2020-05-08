#!/usr/bin/python3
"""
Top Ten
"""
import json
import requests


def top_ten(subreddit):
    """
    This function queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit
    """
    URL = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    headers = {'User-agent': 'URL'}
    req = requests.get(URL, headers=headers, allow_redirects=False).json()
    try:
        lists = req.get('data').get('children')
        for i in lists:
            print(i.get('data').get('title'))
    except:
        print(None)
