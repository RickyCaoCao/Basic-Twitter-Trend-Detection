import tweepy
import config as cfg
from datadog import initialize as datadog_initialize
from datadog import api as datadog_api
from datadog import statsd

# Put keywords that you want to filter in an array.
# QUESTION: Is this AND or OR?
keywords = ['march madness']

# Reading Configuration File
consumer_key = cfg.twitter_consumer_key
consumer_secret = cfg.twitter_consumer_secret
access_token = cfg.twitter_access_key
access_token_secret = cfg.twitter_access_secret
datadog_api_key = cfg.datadog_api_key

# Configuring Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

# Configuring DataDog API
datadog_options = {
    'api_key': datadog_api_key
}
datadog_initialize(**datadog_options)

# Tweepy Stream
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        statsd.increment('mention_count')
        # check RT only incrementation
        # increment positive + negative
        print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = twitter_api.auth, listener = myStreamListener)

myStream.filter(track=keywords)

# ----- Simple Tests ----------------------------------------
#
# ----- Test Python API ---------------------------------
# public_tweets = twitter_api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text
