import tweepy
from textblob import TextBlob

consumer_key=''
consumer_secret=''

access_token = ''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api= tweepy.API(auth)

public_tweets= api.search('Messi')

for tweet in public_tweets:
	print(tweet.text)
	
 def clean_tweet(self, tweet):
        return '\n '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
