#!/usr/bin/python3
<<<<<<< HEAD
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
=======
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, limiting the number of posts to 10
    params = {
        "limit": 10
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        print("None")
        return

    # Parse the JSON response and extract the 'data' section
    results = response.json().get("data")

    # Print the titles of the top 10 hottest posts
    [print(c.get("data").get("title")) for
>>>>>>> caf1dea366fff0eb253a0f59109a4ea646b482d3
