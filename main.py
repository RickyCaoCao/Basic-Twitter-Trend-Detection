import tweepy
import config as cfg

consumer_key = cfg.twitter_consumer_key
consumer_secret = cfg.twitter_consumer_secret
access_token = cfg.twitter_access_key
access_token_secret = cfg.twitter_access_secret
datadog_api_key = cfg.datadog_api_keypip

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitter_api = tweepy.API(auth)

keywords = ['march madness']

# public_tweets = twitter_api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = twitter_api.auth, listener = myStreamListener)

myStream.filter(track=keywords)
