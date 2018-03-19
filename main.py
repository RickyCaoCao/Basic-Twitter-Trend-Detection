import tweepy
import config as cfg
from datadog import initialize as datadog_initialize
from datadog import api as datadog_api
from datadog import statsd

# Put keywords that you want to filter in an array.
# NOTE: It filters multiple words using OR boolean logic
keywords = ['pagerduty', 'devops', 'victorops', 'march madness']

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
        print(status.text)
        for word in keywords:
            if word.lower() in status.text.lower():
                statsd.increment( word + " tweet_count")
                # Extra - Check if RT
                # self.add_to_retweet_board(status)
                # Extra - Use sentiment analysis
                print(word)

    def add_to_retweet_board(self, status):
        if status.retweeted_status:
            statsd.increment('keyword_and_retweet_count')

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = twitter_api.auth, listener = myStreamListener)

myStream.filter(track=keywords)
