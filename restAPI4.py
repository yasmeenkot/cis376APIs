from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/tweets/<string:screen_name>', methods=['GET'])
def get_profile(screen_name):
    # Load tweets from the JSON file
    with open('favTweets.json', 'r') as file:
        data = json.load(file)

    # Parse through json data for location, description, followers and friends count given screen name
    for tweet in data:
        user = tweet.get('user', {})
        # Get screen name from user object
        if user.get('screen_name') == screen_name:                                                                       
            profile_details = {
                'location': user.get('location', None),
                'description': user.get('description', None),
                'followers_count': user.get('followers_count', None),
                'friends_count': user.get('friends_count', None)
            }
            # Stop searching once the tweet is found
            break

    # Check if profile details were found and return them, else print error
    if profile_details:
        return jsonify(profile_details)
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)       
