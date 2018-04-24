import tweepy, time, random
import config as cfg

# Change this keyword to what 
keyword = 'toronto raptors'

# Reading Configuration File
consumer_key = cfg.test_twitter_consumer_key
consumer_secret = cfg.test_twitter_consumer_secret
access_token = cfg.test_twitter_access_key
access_token_secret = cfg.test_twitter_access_secret

# Configuring Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

def _post_status(num):
    status_str = "Status {0} about {1}!".format(str(num), keyword)
    twitter_api.update_status(status_str)

def post_random_const_statuses():
    print 'Posting statuses between 6-10 seconds apart forever'
    num = 0
    while(True):
        _post_status(num)
        num += 1
        time.sleep(5 + random.randint(1, 5))


def post_const_statuses():
    print "Posting statuses every 15 seconds forever"
    num = 0
    while(True):
        _post_status(num)
        num += 1
        time.sleep(15)
        print num

def post_linear_statuses():
    print "Posting statuses slowly initially and faster over time"
    for num in range(60, 2, -1):
        _post_status(num)
        time.sleep(num/12 + 1)

if __name__ == "__main__":
    print "Type '1' to post statuses between 6-10 seconds apart forever"
    print "Type '2' to post statuses every 15 seconds forever"
    print "Type '3' to post statuses slowly initially and faster over time."
    user_input= raw_input("> ")
    if user_input == '1':
        post_random_const_statuses()
    elif user_input == '2':
        post_const_statuses()
    elif user_input == '3':
        post_linear_statuses()
