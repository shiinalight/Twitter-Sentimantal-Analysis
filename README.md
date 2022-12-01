# Twitter Sentimental Analysis
Sentiment Analysis as a technique used in text mining. Twitter sentiment or opinion expressed through it may be positive, negative or neutral.

## Setup


[tweepy](http://www.tweepy.org/)
you can install it using this command

````
pip3 install tweepy
``````


[textblob](https://textblob.readthedocs.io/en/dev/#)
you can install it using this command
````
pip3 install textblob
``````


[NLTK dataset](https://www.nltk.org/) can be downloaded by using the following command
````
python3 -m textblob.download_corpora
``````

You also need to have the consumer keys and access tokens from the Twitter Dev Application Management site, a new app must to be created using your Twitter account.
Open apps.twitter.com and use the  `Create New App`  button.
Complete the form with the necessary application details, and choose a unique application name.
Navitgate to the  `Keys and Access Tokens`  tab.
Copy `Consumer Key`, `Consumer Secret`, `Access Token` and `Access Token Secret` and update the variables `consumer_key` , `consumer_secret`, `access_token`, and `access_token_secret` in the  `sentiment_analysis.py` file accordingly.




## Steps


1.Go to Administrative Command Prompt and install Tweepy:
		pip install tweepy


2.Next Install textblob:
 		pip install textblob


3.Then Run main.py on command Prompt:
		python main.py
			

## Running the program
Download the `sentimental_analysis.py` file from the repository
Update the consumer keys and access token values with the appropriate data in the file
Run the file using

```
python3 sentimental_analysis.py
````

### Note: 
Here I have included two versions to execute the concept. The main idea is the summary of our theme, while the other one executes analytical calculations of your results as well.
