#!/usr/bin/python3
""" Queries Reddit API and returns number of subscribers for a subreddit. """
import requests


def number_of_subscribers(subreddit):
    URL = "https://www.reddit.com/r/{}/about.json"
    Headers = {"User-Agent": "Custom"}
    response = requests.get(URL.format(subreddit), headers=Headers)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers', 0)
