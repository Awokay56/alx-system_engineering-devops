#!/usr/bin/python3
<<<<<<< HEAD
""" a script that has a method that returns the 
    number of subscribers
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ a method that returns the number of a subscribers """
    headers = {"User-Agent": "xica369"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url,headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get('data').get('subscribers'))
    else:
        return (0)
=======
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
>>>>>>> caf1dea366fff0eb253a0f59109a4ea646b482d3
