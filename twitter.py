import tweepy
from textblob import TextBlob

consumer_key = 'Your key'
consumer_secret = 'your secret'
access_token = 'your token'
access_token_secret = 'your secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('ShutdownStories')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)