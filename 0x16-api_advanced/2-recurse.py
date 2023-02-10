#!/usr/bin/python3
""" Queries the Reddit API and returns a list containing the titles of all hot
    articles for a given subreddit using recursion. """
import requests


def recurse(subreddit, hot_list=[], after="null"):
    URL = "https://www.reddit.com/r/{}/hot.json?after={};limit=100"
    Headers = {"User-Agent": "Custom"}
    response = requests.get(URL.format(subreddit, after), headers=Headers)
    if response.status_code != 200:
        return None
    hot = response.json().get('data').get('children')
    if not hot:
        return None
    hot_list = hot_list + hot
    after = response.json().get('data').get('after')
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
