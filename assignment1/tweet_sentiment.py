import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():

    # open first file
    afinnfile = open(sys.argv[1])
    # initialize an empty dictionary
    scores = {} 
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # print scores.items() # Print every (term, score) pair in the dictionary

    # open second file
    tweets = open(sys.argv[2])

    once = 1
    # for each tweet in file
    for tweet in tweets:
        # parse each tweet
        dict1 = json.loads(tweet)
        # initialize sentiment score to 0
        sentiment = 0
        # check if tweet is indeed a tweet.
        # a tweet will have "u'text'" as a key in its dictionary
        if u'text' in dict1.keys():
            # get contents of the field, format is unicode
            unicode_string = dict1[u'text']
            # convert unicode into a string of utf-8 encoded words
            encoded_string = unicode_string.encode('utf-8')
            # convert to small caps
            encoded_string = encoded_string.lower()
            # convert str into list of words
            words = encoded_string.split(" ")
            # for each word in the tweeted text    
            for word in words:
                # check if the word is one of the key in scores
                if word in scores.keys():
                    # compute the sentiment
                    sentiment = scores[word] + sentiment
        print sentiment


if __name__ == '__main__':
    main()