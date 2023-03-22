from json import jsonify
import tweepy


# Twitter API credentials
consumer_key = "W1rPR8gBhwQrlRemfXxzeXt61"
consumer_secret = "UBBpLajtaffCOfLUAY04PDDQMaw2e4jYNazSnTflIsN0fKn1pE"
access_token = "968560301464461312-z9AfFyMs4tNaomy5V5dPSv2zqxXawVA"
access_token_secret = "S6Jx76oxiQi8bFgEICZ8JP276vlmwiCrEHKZDTcJb8Pkg"

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define a route to fetch tweets by a specific user
def get_tweets():
    topic = "gundam"
    # Fetch the latest tweets by the user
    # tweets = api.user_timeline(q=topic, count=10)
    tweets = api.search_tweets(q=topic, count=10)

    # Convert the tweets to a list of dictionaries
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

    # Return the list of tweets as JSON
    return jsonify(tweet_list)