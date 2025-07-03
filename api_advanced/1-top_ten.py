#!/usr/bin/python3
"""
1-top_ten.py

Fetches and prints the titles of the top 10 hot posts from a given subreddit
using the Reddit API. If the subreddit is invalid, it prints None.

Author: Nzabinesha Merci
Date: June 2025
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None: Prints each title or None if subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'SubredditTopTenViewer/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)
