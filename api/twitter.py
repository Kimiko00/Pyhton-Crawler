import tweepy

class TwitterAPI:
    def __init__ (self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.secret_key = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)
        
    def search_tweets(self, topic, count):
        tweets = self.api.search_tweets(q=topic, count=count)
        
        tweet_list = []
        for tweet in tweets:
            tweet_dict = {
                'user': tweet.user.screen_name,
                'text': tweet.text,
                'created_at': str(tweet.created_at),
                'retweet_count': tweet.retweet_count,
                'favorite_count': tweet.favorite_count,
                'hashtags': [h['text'] for h in tweet.entities['hashtags']],
                'user_mentions': [u['screen_name'] for u in tweet.entities['user_mentions']]
            }
            tweet_list.append(tweet_dict)
        return tweet_list