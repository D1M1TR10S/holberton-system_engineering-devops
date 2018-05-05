#!/usr/bin/python3
'''
    A function that makes an API call to the
    Reddit API and returns the first 10 hot
    posts for a given subreddit.
'''
import requests


def top_ten(subreddit):
    headers = {'User-Agent': 'CatLord'}
    subred = requests.get(
        'https://api.reddit.com/r/{}/hot'.format(subreddit),
        headers=headers, allow_redirects=False)
    dct = subred.json()
    top_ten = []
    try:
        for i in range(10):
            top_ten += dct['data']['children'][i]['data']['title']
            print(dct['data']['children'][i]['data']['title'])
        return top_ten
    except:
        print(None)
        return None
