from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/tweets/<int:id>', methods=['GET'])
def get_details(id):
    # Load tweets from the JSON file
    with open('favTweets.json', 'r') as file:
        data = json.load(file)

    # Parse through json data for create time, text, and screen name given id
    for tweet in data:
        if tweet['id'] == id:
            tweet_details = {
                'created_at': tweet.get('created_at', None),
                'text': tweet.get('text', None),
                'screen_name': tweet.get('screen_name', None)
            }
            # Stop searching once the tweet is found
            break 
        
    # Check if tweet details were found
    if tweet_details:
        return jsonify(tweet_details)
    else:
        return jsonify({'error': 'Tweet not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
