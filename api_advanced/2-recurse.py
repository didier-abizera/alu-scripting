#!/usr/bin/python3
"""Module to recursively get all hot posts from Reddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively return list of hot post titles for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/didier_alu)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)
    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")

    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            hot_list.append(title)

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
