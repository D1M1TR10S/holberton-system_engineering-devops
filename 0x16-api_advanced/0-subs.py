#!/usr/bin/python3
'''
    A function that makes an API call to the
    Reddit API and returns the number of
    subscribers for a given subreddit.
'''
import requests


def number_of_subscribers(subreddit):
    headers = {
    'User-Agent': 'The Lord of Cats'
}
    subred = requests.get(
        'https://api.reddit.com/r/{}/about'.format(subreddit), headers=headers)
    dct = subred.json()
    try:
        subscribers = dct['data']['subscribers']
        return subscribers
    except KeyError:
        return 0
