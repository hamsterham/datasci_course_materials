import sys
import json

# dictionary of states
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


def main():

    # open first file
    afinnfile = open(sys.argv[1])
    # initialize an empty dictionary
    scores = {} 
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # open second file
    tweets = open(sys.argv[2])

    # initialize an empty dictionary, 
    # { two-letter-state : sentiment-score, 
    #   two-letter-state : sentiment-score, ... }
    state_score = {}

    # for each tweet in file
    for tweet in tweets:
        # parse tweet
        dict1 = json.loads(tweet)   
 
        # initialize sentiment score to 0
        sentiment = 0

        # get 'place' and 'text' from tweet
        unicode_string = dict1.get("text", False)
        place = dict1.get("place", False)
        # get country code and full_name
        country_code = place.get("country_code", False)
        name = place.get("name", False)
        full_name = place.get("full_name", False)        

        # process if place and tweet is not None
        if all((unicode_string, place, full_name)) and country_code == "US":
            # process if state is recognizable in the tweet
            if full_name[-2:] in states:
                state = full_name[-2:]
            elif name in states.values():
                state = [key for key, value in states.iteritems() if value == name][0]                
            else:
                continue
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
            # update the sentiment state of the state
            state_score[state] = state_score.get(state, 0) + sentiment

    # output
#    print state_score
    print max(state_score, key=state_score.get)
        
if __name__ == '__main__':
    main()