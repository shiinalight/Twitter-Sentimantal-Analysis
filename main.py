import tweepy
from textblob import TextBlob

CONSUMER_KEY = 'CONSUMER KEY HERE'
CONSUMER_SECRET = 'CONUSMER SECRET KEY HERE'
ACCESS_TOKEN = 'ACCESS TOKEN KEY HERE'
ACESS_TOKEN_SECRET = 'ACCESS TOKEN SECRET KEY HERE'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

tweepy.API(auth)

tweets = api.search('Machine Learning')

for tweet in tweets:
  print(tweet.text)
  
  analysis  = TextBlob(tweet.text)
  a = analysis.sentiment.polarity
  if(a>0):
    print("Positive")
  elif(a == 0):
    print("Neutral")
  else:
     print("Negative")
  print("\n")
