#!/usr/bin/python3
""" Queries the Reddit API, parses the title of all hot articles, and prints a
    sorted count of given keywords recursively. """
import re
import requests


def count_words(subreddit, word_list, hot_list=[], after="null"):
    """ Gets all the elements in hot. """
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
        results(word_list, hot_list)
    else:
        count_words(subreddit, word_list, hot_list, after)


def results(word_list, hot_list):
    """ Prints the results of the search. """
    count = {}
    for word in word_list:
        count[word] = 0
    for element in hot_list:
        for word in word_list:
            count[word] += len(re.findall(r"(?=(?:^| ){}(?: |$))".format(word),
                                          element.get('data').get('title'),
                                          re.I))
    count = {key: val for key, val in count.items() if val != 0}
    by_key = sorted(list(count.keys()))
    by_val = sorted(by_key, key=lambda k: count[k], reverse=True)
    for word in by_val:
        print("{}: {}".format(word, count[word]))
    