from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

from api.nist import NvdAPI
from api.twitter import TwitterAPI
from api.stack import StackOverflowAPI

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# create stack api object
api = StackOverflowAPI()

# create a TwitterAPI Object
twitter_api = TwitterAPI()

#create nist api object
nist = NvdAPI()

#insert routing class
@app.route('/', methods=['GET'])
def home():
    return f"this route is for log in user"

@app.route('/api/tweets', methods=['GET'])
@cross_origin()
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