import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'l4hgbhH3UtFzwUfW6ZIw5OM4F'
CONSUMER_SECRET = 'ZFexuXt0JL5e9Mkx7N21ihLBDh33kcTODEKkuYc0dSfoPicYl0'
OAUTH_TOKEN = '544426332-HSwONottMnM69TMFgx9jWNNCgUP7lk1Th6rRneL4'
OAUTH_TOKEN_SECRET = '2wVUGiPcgxhOYzwpdktudNwwgd0Xz2ICWqyq7DUzNtH66'

def get_auth():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return auth

def get_api():
    auth = get_auth()
    return tweepy.API(auth)