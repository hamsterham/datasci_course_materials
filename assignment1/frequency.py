import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():

    # open files
    tweet_file = open(sys.argv[1])

    # initialize an empty dictionary
    freq = {} 
    
    # for each tweet in file
    for tweet in tweet_file:
        # parse each tweet
        dict1 = json.loads(tweet)
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
            # count the occurance     
            for word in words:
                # strip away white space characters at the 
                # front and end of the word
                # some word has more than 1 white space 
                # character, thus split may not work so well, 
                # thus need to do a strip
                word = word.strip()
                freq[word] = freq.get(word, 0) + 1

    total_words = sum(freq.values())

    # output
    for key, value in freq.items():
        print key, float(value)/total_words



if __name__ == '__main__':
    main()