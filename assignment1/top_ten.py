import sys
import json

def main():

    # open file
    tweets = open(sys.argv[1])

    # create empty dictionary
    all_tags_dict = {}

    # for each tweet
    for tweet in tweets:
        # parse tweet
        dict1 = json.loads(tweet)
        # get the entities
        entities = dict1['entities']
        # get the hashtags inside entities, hashtags is a list
        hashtags = entities['hashtags']
        # if it has nothing
        if len(hashtags) == 0:
            continue

        for hashtag in hashtags:
            # get the text
            hashtag_text = hashtag['text']
            # convert unicode into a string of utf-8 encoded words
            hashtag_text = hashtag_text.encode('utf-8')
            all_tags_dict[hashtag_text] = all_tags_dict.get(hashtag_text, 0) + 1
    
    # sort the dictionary keys by values in descending
    sorted_list = sorted(all_tags_dict, key=all_tags_dict.get, reverse=True)

    num_outputs = 10

    if len(sorted_list) < num_outputs:
        num_outputs = len(sorted_list)

    # output top ten
    for i in range(num_outputs):
        print sorted_list[i], all_tags_dict[sorted_list[i]]
    


if __name__ == '__main__':
    main()