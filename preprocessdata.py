import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import string
import nltk
import warnings
import json
from nltk.stem.porter import *

warnings.filterwarnings("ignore",category=DeprecationWarning)
#%matplotlib inline

#Create a Data Frame 
f=open('tweets_news.txt','r')
list=[]
#Creating Data Frame
for i in f:
    json_text=json.loads(i)
    text=json_text['text']
    text.replace('\n','').replace('\r','')
    list.append(text)

tweets = pd.DataFrame(list)
tweets.columns=['tweets']

#Preprocessing the data
def remove_pattern(inp_txt,pattern):
    r=re.findall(pattern,inp_txt)
    for i in r:
        inp_txt=re.sub(i,'',inp_txt)
    return(inp_txt)
tweets['tidy_tweet']=np.vectorize(remove_pattern(tweets['tweets'],"@[\\w]*"))
tweets['tidy_tweet']=np.vectorize(remove_pattern(tweets['tweets'],"#[\\w]*"))
#Remove Punctuation and special characters
tweets['tidy_tweet']=tweets['tidy_tweet'].str.replace("[^a-zA-Z#]"," ")
#Remove short words
tweets['tidy_tweet']=tweets['tidy_tweet'].apply(lambda x : ' '.join([w for w in x.split() if len(w)>3] ))

#Tokeniation
tokenized_tweet = tweets['tidy_tweet'].apply(lambda x:x.split())
#Stemming to remove suffixes like ('es,'ly','ing)
stemmer = PorterStemmer()
tokenized_tweet=tokenized_tweet.apply(lambda x: [stemmer.stem(i) for i in x])
for i in range(len(tokenized_tweet)):
    tokenized_tweet[i] = ' '.join(tokenized_tweet[i])

tweets['tidy_tweet'] = tokenized_tweet
#Plots
# all_words = ' '.join([text for text in tweets['tidy_tweet']])
# from wordcloud import WordCloud
# wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(all_words)

# plt.figure(figsize=(10, 7))
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis('off')
# plt.show()
# print(all_words)

#Remove line breaks and tabs
text.replace('\n','').replace('\r','')
#Remove Twitter handles
