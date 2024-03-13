from flask import Flask, jsonify
import json
import re

app = Flask(__name__)

@app.route('/tweets', methods=['GET'])
def get_links():
    # Load tweets from the JSON file
    with open('favTweets.json', 'r') as file:
        data = json.load(file)

    # Create dictionary of tweet links
    tweet_links = {}

    # Parse through json data for external links
    for tweet in data:
        tweet_id = tweet['id']
        text = tweet['text']
        # Regular expression to look for link within tweet text
        link = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

        # If the link is the first one for the id, create a new entry for the id and link, else append it to the existing list
        # Group links by tweet ids
        if tweet_id not in tweet_links:
            tweet_links[tweet_id] = link
        else:
            tweet_links[tweet_id].extend(link)

    # Return information
    return jsonify(tweet_links)

if __name__ == '__main__':
    app.run(debug=True)


