#!/usr/bin/python3
"""
Recurse it!
"""
import json
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    This recursive function queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
    """
    URL = 'https://www.reddit.com/r/{}/hot/.json?after={}'.format(
        subreddit, after)
    headers = {'User-agent': 'URL'}
    req = requests.get(URL, headers=headers, allow_redirects=False).json()
    try:
        lists = req.get('data').get('children')
        for i in lists:
            hot_list.append(i.get('data').get('title'))
    except:
        return(None)

    after_data = req.get('data').get('after')
    if after_data is None:
        return hot_list
    return recurse(subreddit, hot_list, after_data)
