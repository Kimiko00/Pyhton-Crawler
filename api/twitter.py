from dotenv import load_dotenv
import tweepy, os

class TwitterAPI:
    def config():
        load_dotenv()
    
    def __init__ (self):
        self.consumer_key = os.getenv('consumer_key')
        self.consumer_secret = os.getenv('consumer_secret')
        self.access_token = os.getenv('access_token')
        self.access_token_secret = os.getenv('access_token_secret')
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)
        
    def search_tweets(self, topic, count):
        tweets = self.api.search_tweets(q=topic, count=count)
        
        tweet_list = []
        for tweet in tweets:
            tweet_dict = {
                'img': tweet.user.profile_image_url_https,
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