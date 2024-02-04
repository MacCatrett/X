import tweepy
import json

# Load your credentials from the config file
with open('config.json', 'r') as file:
    config = json.load(file)
    bearer_token = config['twitter_api']['bearer_token']  # API v2 uses bearer token

# Initialize Tweepy with Bearer Token
client = tweepy.Client(bearer_token=bearer_token)

# Specify the user ID or username
username = 'twitter'  # Replace with the actual username

# Fetch recent tweets from the user
# Note: Replace 'user_id' with the actual user ID if necessary
tweets = client.get_users_tweets(id=username, max_results=10)

for tweet in tweets.data:
    print(tweet.text)
