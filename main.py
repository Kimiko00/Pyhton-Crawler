from flask import Flask

app = Flask(__name__)

#insert routing class
@app.route('/api/tweets')
def twit_data():
    #do something here
    return

if __name__ == '__main__':
    app.run(debug=True)