from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/tweets', methods=['GET'])
def get_tweets():
    # Load tweets from the JSON file
    with open('favTweets.json', 'r') as file:
        data = json.load(file)

    # Create list of tweets
    tweets = []

    # Parse through json data for create time, id, and tweet text
    for tweet in data:
        tweet_info = {
            'created_at': tweet.get('created_at', None),
            'id': tweet.get('id', None),
            'text': tweet.get('text', None)
        }
        # Add tweet info to list
        tweets.append(tweet_info)

    # Return information
    return jsonify(tweets)

if __name__ == '__main__':
    app.run(debug=True)




