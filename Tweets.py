import tweepy
import json

# Load API keys and tokens from the config file
with open('config.json', 'r') as file:
    config = json.load(file)
    bearer_token = config['twitter_api']['bearer_token']

# Initialize Tweepy Client with Bearer Token
client = tweepy.Client(bearer_token=bearer_token)

# Define the search query (keyword or hashtag)
query = '#technology'  # Replace this with your keyword or hashtag

# Search for recent tweets containing the query
tweets = client.search_recent_tweets(query=query, max_results=10)

# Print the text of each tweet found
for tweet in tweets.data:
    print(tweet.text)
