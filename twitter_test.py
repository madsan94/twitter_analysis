import tweepy 
import sys
import os
import jsonpickle

consumer_key='K9gyhpKJWbjOVk3qkdd61i0ro'
consumer_secret='51qLCu92F5MV9RzsLkh0rPXscR4SkZsBHeNNtMo33XLvOXbfG2'
access_token_key='1690297922-06CjYESyGyRotaADWtcCzsU5QJrTpTdsYATbNI5'
access_token_secret='dpXLR4tmjfsksVdYgsHNRpaz3Nr6nt97sqrX8LUa8RFSU'
auth = tweepy.AppAuthHandler(consumer_key,consumer_secret)
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

if(not api):
    print("Cannot Authenticate")
    sys.exit(-1)

searchQuery = '#NDTV OR #AajTak OR #news18ind OR #indiatvnews OR #indiatoday'
maxTweets = 5000 
tweetsperQry = 100
fname='tweets_news.txt'

sinceId = None
max_id = -1

tweetCount = 0
with open(fname,'w') as f:
    while(tweetCount<maxTweets):
        try:
            if(max_id<=0):
                if(not sinceId):
                    new_tweets=api.search(q=searchQuery,count=tweetsperQry)
                else:
                    new_tweets=api.search(q=searchQuery,count=tweetsperQry,since_id=sinceId)
            else:
                if(not sinceId):
                    new_tweets=api.search(q=searchQuery,count=tweetsperQry,max_id=str(max_id-1))
                else:
                    new_tweets=api.search(q=searchQuery,count=tweetsperQry,max_id=str(max_id-1),since_id=sinceId)
            
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        '\n')
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break
print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fname))