#!/usr/bin/python3
"""Module to query Reddit API for top 10 hot posts"""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/didier_alu)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
