import tweepy, time, random
import config as cfg

# Put the same keyword as main.py to see if it reflects in Datadog
keyword = ['pdt-rcao']

# Reading Configuration File
consumer_key = cfg.test_twitter_consumer_key
consumer_secret = cfg.test_twitter_consumer_secret
access_token = cfg.test_twitter_access_key
access_token_secret = cfg.test_twitter_access_secret

# Configuring Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

# ----- Manual Tests ------------------------------------------------
# ----- Test Twitter API Connection ---------------------------------
# public_tweets = twitter_api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

def post_random_statuses():
    num = 0
    while(True):
        status_str = 'Pagerduty! ' + str(num)
        print(status_str)
        twitter_api.update_status(status_str)
        num += 1
        time.sleep(15 + random.randint(1, 5))


# --- Starting Alert Base ------------------------------------------
# --- Constant Updates ----------------------------------------------
def post_linear_statuses():
    print '----------- posting statuses in linear time --------------------'
    num = 0
    while(True):
        twitter_api.update_status('pdt-rcao ' + str(num))
        num += 1
        time.sleep(15)
        print num
def post_controversial_statuses():
    print '-------- posting controversial statuses -----------------------'
    # --- Controversial Status Update ------------------------------------------
    # twitter_api.update_status('iminoso sucks at FIFA 18')
    # time.sleep(10)

    # --- Blowing UP ------------------------------------------------------
    for i in range(60, 2, -1):
        twitter_api.update_status(str(i) + ' pdt-rcao ' + str(i))
        print i
        # if not (i % 5):
        #     recent_status = twitter_api.home_timeline(count=1)
        #     twitter_api.update_status(recent_status)
        time.sleep(i/12 + 1)

if __name__ == "__main__":
    print "Type '1' for randomly-spaced status posts"
    print "Type '2' for linear status posts"
    print "Type '3' for pseudo-quadratic status posts"
    user_input= raw_input("> ")
    if user_input == '1':
        post_random_statuses()
    elif user_input == '2':
        post_linear_statuses()
    elif user_input == '3':
        post_controversial_statuses()
