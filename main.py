from flask import Flask, jsonify
from api.twitter import TwitterAPI
from api.stack import StackOverflowAPI
from api.nist import NvdAPI

app = Flask(__name__)

# create stack api object
api = StackOverflowAPI()

# create a TwitterAPI Object
twitter_api = TwitterAPI()

#create nist api object
nist = NvdAPI()

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

@app.route('/api/nist', methods=['GET'])
def get_nist():
    cve = nist.fetch_cves()
    return jsonify(cve)

if __name__ == '__main__':
    app.run(debug=True)