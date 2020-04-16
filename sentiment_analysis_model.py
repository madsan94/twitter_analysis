import pandas as pd

csv = 'sentiment_analysis_clean_tweet.csv'
my_df = pd.read_csv(csv)
my_df.columns=['id','text','sentiment']
my_df.drop(['id'],inplace=True,axis=1)
print(my_df.head())