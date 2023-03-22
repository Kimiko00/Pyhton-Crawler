from flask import Flask, jsonify
from api.twitter import TwitterAPI
from api.stack import StackOverflowAPI

app = Flask(__name__)
api = StackOverflowAPI()

# twitter api credentials
consumer_key = "W1rPR8gBhwQrlRemfXxzeXt61"
consumer_secret = "UBBpLajtaffCOfLUAY04PDDQMaw2e4jYNazSnTflIsN0fKn1pE"
access_token = "968560301464461312-z9AfFyMs4tNaomy5V5dPSv2zqxXawVA"
access_token_secret = "S6Jx76oxiQi8bFgEICZ8JP276vlmwiCrEHKZDTcJb8Pkg"

# create a TwitterAPI Object
twitter_api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

#insert routing class
@app.route('/api/tweets', methods=['GET'])
def get_tweets():
    topic = "gundam"
    count = 10
    tweets = twitter_api.search_tweets(topic=topic, count=count)
    return jsonify(tweets)

@app.route('/api/stack', methods=['GET'])
def get_stack():
    data = api.fetch_questions()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)