#!/usr/bin/python3
""" A script that has a method that prints
    the title of the first 10 hot posts
"""
import requests
import sys


def top_ten(subreddit):
    """ a method that prints the titles
        of the first 10 posts
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "chrome 5.8"}
    limit = {"limit": 10}
    response = requests.get(url,headers=headers,allow_redirects=False,
                            params=limit)

    if response.status_code == 200:
        titles = response.json().get('data').get('children')
        for title in titles:
            print(title.get('data').get('title'))
    else:
        print(None)