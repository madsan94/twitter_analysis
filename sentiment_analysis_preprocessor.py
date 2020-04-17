import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import re
from nltk.tokenize import WordPunctTokenizer

columns=['sentiment','id','date','query_string','user','text']
address='/home/sanket/Desktop/ML/snt.csv'
data_df = pd.read_csv(address,encoding="ISO-8859-1")
data_df.columns=columns



#Cleaning the DataSource.
data_df.drop(['id','date','query_string','user'],axis=1,inplace=True)
#Cheking for pre-cleaning length
data_df['pre_clean_len']=[len(t) for t in data_df.text]
#Checking for outliers using boxplot
fig,ax=plt.subplots(figsize=(5,5))
plt.boxplot(data_df.pre_clean_len)
#plt.show()
#print(data_df[data_df.pre_clean_len>140].head(10))
#print(data_df[data_df.pre_clean_len>140].head(20))
#Cleaning HTML Tags/@Mentions/URL Links/UTF-8 BOM/Hashtags/Numbers
#Defining Data Cleaning Function

from nltk.tokenize import WordPunctTokenizer
tok = WordPunctTokenizer()
pat1 = r'@[A-Za-z0-9]+'
pat2 = r'https?://[A-Za-z0-9./]+'
combined_pat = r'|'.join((pat1,pat2))

def tweet_cleaner(text):
    soup = BeautifulSoup(text,'lxml')
    souped = soup.get_text()
    stripped = re.sub(combined_pat,'',souped)
    try:
        clean = stripped.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        clean = stripped
    letters_only = re.sub("[^a-zA-Z]", " ", clean)
    lower_case = letters_only.lower()
    words = tok.tokenize(lower_case)
    return (" ".join(words)).strip()

#Cleaning each text from the data frame
nums = [0,1599999]
print("Cleaning and parsing the tweets...\n")
clean_tweet_texts = []
for i in range(nums[0],nums[1]):
    if( (i+1)%10000 == 0 ):
        print("Tweets %d of %d has been processed" % ( i+1, nums[1]))
    clean_tweet_texts.append(tweet_cleaner(data_df['text'][i]))


clean_df = pd.DataFrame(clean_tweet_texts,columns=['text'])
clean_df['target'] = data_df.sentiment

clean_df.to_csv('sentiment_analysis_clean_tweet.csv',encoding='utf-8')
