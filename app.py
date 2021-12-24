# Importing libraries
import pandas as pd

# Reading Data
slurs = pd.read_csv('slurs.csv')
tweets = pd.read_csv('tweets.csv')

tweets["profane word count"] = ""
tweets["degree of profanity"] = ""
tweets = tweets[["tweet", "profane word count", "degree of profanity"]]

# Detection of Profane words(racial slurs)
# Iterate through each rows of the tweets dataset
for i in range(tweets.shape[0]):
    # Each tweet is taken seperately
    tweet = tweets.at[i, 'tweet']
    # profaneWordCount holds the number of profane words in each tweet
    profaneWordCount = (sum(tweet.lower().count(str(i)) for i in slurs.Slur)) 
    tweets.at[i, 'profane word count'] = profaneWordCount
        
    # Determining the Degree of Profanity of each tweet
    '''Degree is determined on the basis of ratio of Profane Words 
    to the Total Number of Words in the tweet.'''
    rawScore = (profaneWordCount / len(tweet))
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