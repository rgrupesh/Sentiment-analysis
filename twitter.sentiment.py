import tweepy
from textblob import TextBlob

consumer_key='wx0hpYjn5q6Bo6v80RfoyiNiC'
consumer_secret='p0A5Z1d7H8xesN0EEDw355EfMoR7MroMLDW97ij9cjNc0ujNmr'

access_token = '710194439-1z5STIpU66r9Jko9eUf19p4NkGfqGSBkF9PbTbfO'
access_token_secret='9jBklUl43osrN0WxouHzF0azHT5dM75RW2qQ70csMwFiH'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api= tweepy.API(auth)

public_tweets= api.search('Messi')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)