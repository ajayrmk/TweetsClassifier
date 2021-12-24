# TweetsClassifier
This program that can identify the degree of profanity for each sentence in a file full of Twitter tweets. Here degree is determined on the basis of ratio of Profane words to the total tumber of words in the tweet.

The tweets dataset and slurs dataset are set as .csv files. Tweets being taken from Kaggle(https://www.kaggle.com/ashwiniyer176/toxic-tweets-dataset) and Slurs being web-scrapped from The Racial Slur Database(http://www.rsdb.org/full).

Run 'app.py' to access the tweets from 'tweets.csv' and slurs from 'slurs.csv' and update profanity words count and the degree of profanity in 'tweets.csv'.

Python script to webscrap the racial slur words to slurs.csv are added in 'slur.py'.