import json
import pandas as pd
import re
from datetime import datetime

def top_retweet():
    tweets = [None] * 10
    with open("data/farmers-protest-tweets-2021-03-5.json", "r") as f:
        for l in f:
            linea = json.loads(l)
            for i in range(len(tweets)):
                if (tweets[i] == None) or (linea['retweetCount'] > tweets[i]['retweetCount']):
                    tweets[i] = linea
                    break
    return tweets

if __name__ == "__main__":
    top_retweet()
