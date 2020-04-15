twitter_test.py ===============>

Put the following values:
consumer_key=
consumer_secret=
access_token_key=
access_token_secret=
#Make sure to empty these values before you push the code
put the searchQuery as input to fetch the tweets and file name is 'fname' 
where the raw tweets will be saved

preprocessdata.py =================> 

cleans the data

sentiment_analysis_preprocessor.py ===============>

Reads 1.6 million tweets from snt.csv for sentiment analysis, this file cleans the data
and store it in sentiment_analysis_clean_tweet.csv

sentiment_analysis_model.py ===============>
LSTM Model which trains the 1.6 million tweet data.