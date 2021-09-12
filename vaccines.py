import sys

from twython import Twython

import requests

non_bmp_map=dict.fromkeys(range(0x10000, sys.maxunicode+1), 0xfffd)

 

n = 10

query = 'vaccine'

positive = 0
negative = 0
neutral = 0
unknown = 0 

CONSUMER_KEY = ''

CONSUMER_SECRET = ''

ACCESS_TOKEN = ''

ACCESS_SECRET = ''

 

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

 

tweets = twitter.search(q=query, count=n)

 

u = 0

for tweet in tweets['statuses']:
    
        u += 1

print('\n\nTweets retrieved:', u, 'of the total:', n)



for tweet in tweets['statuses']:

    

    #print(tweet['id'])

    print("\n\n" + tweet['user']['screen_name'].translate(non_bmp_map))
    
    print(tweet['text'].translate(non_bmp_map))

    teststring=tweet['text'].translate(non_bmp_map)

    #print(tweet['created_at'])

    #print(tweet['user']['screen_name'].translate(non_bmp_map))

    print("language: " + tweet['lang'])

    url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

 

    querystring = {"text":teststring}

 

    headers = {

        'x-rapidapi-host': "",

        'x-rapidapi-key': ""

    }

 

    response = requests.request("GET", url, headers=headers, params=querystring)

    if tweet['lang'] == "en":

        print("\n" + response.text[1:response.text.index("keywords")])

 
        if "positive" in response.text:
            positive +=1
        
        elif "negative" in response.text:
            negative +=1
        
        elif "neutral" in response.text:
            neutral +=1

    else:
        print("unknown language")
        unknown += 1 


print("\n\nPositive views: " + str(positive))
print("Negative views: " + str(negative))
print("Neutral stance: " + str(neutral))
print("Not in English: " + str(unknown))



