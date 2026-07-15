#!/usr/bin/python3
"""Module to count keywords in Reddit hot posts recursively"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """Recursively count keywords in hot post titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/didier_alu)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)
    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            word_lower = word.lower()
            for t in title:
                if t == word_lower:
                    counts[word_lower] = counts.get(word_lower, 0) + 1

    if after is None:
        if not counts:
            return
        sorted_counts = sorted(counts.items(),
                               key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
        return

    return count_words(subreddit, word_list, after, counts)
