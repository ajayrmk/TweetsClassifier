# Importing libraries
import pandas as pd

# Reading Data
slurs = pd.read_csv('slurs.csv')
tweets = pd.read_csv('tweets.csv')

tweets["profane word count"] = ""
tweets["degree of profanity"] = ""
tweets = tweets[["tweet", "profane word count", "degree of profanity"]]

# Detection of Profane words(racial slurs)
for i in range(tweets.shape[0]):
    tweet = tweets.at[i, 'tweet']
    profaneWordCount = (sum(tweet.lower().count(str(i)) for i in slurs.Slur))
    rawScore = (profaneWordCount / len(tweet))
    tweets.at[i, 'profane word count'] = profaneWordCount
        
        
    # Determining the Degree of Profanity of each tweet
    '''Degree was determined on the basis of ratio of Profane Words 
    to the Total Number of Words in the tweet.'''
    if rawScore == 0.0:
        tweets.at[i, 'degree of profanity'] = "NOT PROFANE"
    elif rawScore > 0.0 and rawScore < 0.025:
        tweets.at[i, 'degree of profanity'] = "PROFANE"
    elif rawScore > 0.025 and rawScore < 0.05:
        tweets.at[i, 'degree of profanity'] = "VERY PROFANE"
    else:
        tweets.at[i, 'degree of profanity'] = "EXTREMELY PROFANE"


# Update the tweets dataset with the Profanity values
tweets.to_csv("tweets.csv")