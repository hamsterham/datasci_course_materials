import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():

    # open files
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # initialize an empty dictionary
    scores = {} 
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # initialize new empty dictionary, for new terms
    new_scores = {}

    # for each tweet in file
    for tweet in tweet_file:
        # parse each tweet
        dict1 = json.loads(tweet)
        # initialize sentiment score to 0 for each tweet/line
        sentiment = 0
        # check if tweet is indeed a tweet.
        # a tweet will have "u'text'" as a key in its dictionary
        if u'text' in dict1:
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
                if word in scores:
                    # compute the sentiment
                    sentiment = scores[word] + sentiment
                # else create new key in the new_scores dictionary                
                elif word not in new_scores:
                    new_scores[word] = 0

            # for each word in the tweeted text
            for word in words:
                # update the scores for each word in dictionary 
                # new_scores
                if word in new_scores:
                    new_scores[word] = new_scores[word] + sentiment

    # output
    for key, word in new_scores.items():
        print key, word


if __name__ == '__main__':
    main()