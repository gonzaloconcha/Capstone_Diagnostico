import json
import pandas as pd
import re
from datetime import datetime
from collections import defaultdict

def top_retweet():
    tweets = [None] * 10
    with open("data/farmers-protest-tweets-2021-03-5.json", "r") as f:
        for l in f:
            linea = json.loads(l)
            for i in range(len(tweets)):
                if (tweets[i] == None) or (linea['retweetCount'] > tweets[i][1]):
                    tweets[i] = (linea['url'], linea['retweetCount'])
                    break
    #tweets = sorted(tweets, key=lambda item: item[1], reverse=True)
    return tweets

def top_active_user():
    tweets = defaultdict(int)
    with open("data/farmers-protest-tweets-2021-03-5.json", "r") as f:
        for l in f:
            linea = json.loads(l)['user']
            tweets[linea['username']] += 1
    tweets = sorted(tweets.items(), key=lambda item: item[1], reverse=True)
    return tweets[0:10]

def top_days():
    tweets = defaultdict(int)
    with open("data/farmers-protest-tweets-2021-03-5.json", "r") as f:
        for l in f:
            linea = datetime.strptime(json.loads(l)['date'].replace('T', ' ')[:-6], '%Y-%m-%d %H:%M:%S')
            fecha = str(linea.date())
            tweets[fecha] += 1
    print(tweets)
    tweets = sorted(tweets.items(), key=lambda item: item[1], reverse=True)
    return tweets[0:10]


if __name__ == "__main__":
    print(top_days())
