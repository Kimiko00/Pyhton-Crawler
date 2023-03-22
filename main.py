from flask import Flask, jsonify
from api.twitter import TwitterAPI

app = Flask(__name__)

# twitter api credentials
consumer_key = "W1rPR8gBhwQrlRemfXxzeXt61"
consumer_secret = "UBBpLajtaffCOfLUAY04PDDQMaw2e4jYNazSnTflIsN0fKn1pE"
access_token = "968560301464461312-z9AfFyMs4tNaomy5V5dPSv2zqxXawVA"
access_token_secret = "S6Jx76oxiQi8bFgEICZ8JP276vlmwiCrEHKZDTcJb8Pkg"

# create a TwitterAPI Object
twitter_api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

#insert routing class
@app.route('/api/tweets')
def get_tweets():
    #do something here
    topic = "gundam"
    count = 10
    tweets = twitter_api.search_tweets(topic=topic, count=count)
    return jsonify(tweets)

if __name__ == '__main__':
    app.run(debug=True)