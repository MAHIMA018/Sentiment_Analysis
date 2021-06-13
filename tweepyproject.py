import tweepy
import re
from textblob import TextBlob

import pandas as pd

import matplotlib.pyplot as plt

c_token='################'
cs_key='###########################'

a_token='##########################'
a_token_secret='#############################'

auth=tweepy.OAuthHandler(c_token,cs_key)
auth.set_access_token(a_token,a_token_secret)
api=tweepy.API(auth)

print(api)

search=input("Enter keyword to search:")
search_count=int(input("How many tweets you want to analyse?:"))

def percentage(part,whole):
    return 100* float(part)/float(whole)

tweets=tweepy.Cursor(api.search,q=search,language="English").items(search_count)

positive=0
negative=0
neutral=0
polarity=0


for tweet in tweets:
    analyse=TextBlob(tweet.text)
    #print(analyse)
    polarity += analyse.sentiment.polarity
    if (analyse.sentiment.polarity)==0:
        neutral +=1
    elif  (analyse.sentiment.polarity)>0:
        positive +=1
    elif  (analyse.sentiment.polarity)<0:
        negative +=1    

neutral=percentage(neutral,search_count)
neutral=format(neutral,'.2f')
print(neutral)
negative=percentage(negative,search_count)
negative=format(negative,'.2f')
print(negative)
positive=percentage(positive,search_count)
positive=format(positive,'.2f')
print(positive)




#######plot/graphical representation



o = pd.DataFrame(data={'score':[float(neutral),float(negative),float(positive)]})
print(o.info())

o.plot(kind='bar')
plt.show()


    
