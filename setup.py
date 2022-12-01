from setuptools import find_packages, setup

NAME = 'Twitter Sentimenatal Analysis'
DESCRIPTION = 'Sentiment Analysis is a technique used in text mining. Twitter Sentiment Analysis may, therefore, be described as a text mining technique for analyzing the underlying sentiment of a text message, i.e., a tweet.'
URL = 'https://github.com/elaishane/TwitterSentimentalAnalysis'
EMAIL = 'yash151099@gmail.com'
AUTHOR = 'Elai Shane'

classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
    
install_requires=['tweepy','matplotlib','textblob']
