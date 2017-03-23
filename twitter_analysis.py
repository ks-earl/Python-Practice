import tweepy
from textblob import TextBlob

consumer_secret = "1QZyzdhKgjeMydf4YlNJoFtXOlDs3t73uJAcB2RgK96pl65wy6"
consumer_key = 'qkCu8l7BH0NKXg9zioddmayJp'

access_token = '2522656190-qsRADRQb0HXKgXgHPKRxk7gZcItJ0RJe1R5UAFE'
access_secret_token = 'snCACWcrSyNq7GNIUDqw4UiwGblSW05mjaBMWsNH6eQdc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret_token)

api = tweepy.API(auth)

positive_sentiment = 0
total_tweets = 0

public_tweets = api.search('Trump')
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    total_tweets = total_tweets + 1
    if analysis.sentiment.polarity > 0:
        positive_sentiment = positive_sentiment + 1

print("Total tweets found: " + str(total_tweets))
print("Tweets with positive sentiments: " + str(positive_sentiment))
print("Tweets with negative sentiment: " + str(total_tweets-positive_sentiment))
