import datetime
from twython import Twython # pip install twython

CONSUMER_KEY = '20ysHnnnb82HXkT1rckKkbFB3'
CONSUMER_SECRET = 'dJMuUHZl7PwKies3Q0IdwwxDRrJg0tZ897F1xNrBu22bIwJGEI'
ACCESS_KEY = '834777543328808961-4Jxmdxhn3rDLrwDq6UuO4sXHo284e2T'
ACCESS_SECRET = 'V8fdxkZXaYYRmymshBTQMkJnEqMkOZwJuowT6usB1C01o'

def PrintHeaderInfo():
    print(datetime.datetime.now())
    print("Hlias Tsiggelis")
    print("------------------------------------")
    print("Project7 gets two user names of Twitter(R) and returns which ")
    print("of these two users has in his last 10 tweets as much as more words")
    print("------------------------------------")
    print("Using python 2.7")
    print("and thwython package, -- python -m pip install twython --")
    print("------------------------------------")
    print("Prerequisite: Go to https://apps.twitter.com/ to register your app to get your api keys")
    print("------------------------------------")

def Count_the_words(user_name):
    number_of_tweets = 10
    twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
    lis = [467020906049835008] ## this is the latest starting tweet id
    user_timeline = twitter.get_user_timeline(screen_name=user_name,count=200, include_retweets=False)
    tweet_count = 0
    total_word_counts = 0
    for tweet in user_timeline:
        tweet_count = tweet_count + 1
        #print tweet_count, ".", tweet['text']  ## print the tweet
        temp = tweet['text']
        word_counts_on_tweet = len(temp.split())
        total_word_counts = total_word_counts + word_counts_on_tweet
        if tweet_count == number_of_tweets:
            return total_word_counts
            break
        else:
            lis.append(tweet['id']) ## append tweet id's

if __name__ == '__main__':
        PrintHeaderInfo()
        username_a = raw_input('User, please give me the 1st username from Twitter(R)...')
        username_b = raw_input("User, please give me the 2nd username from Twitter(R)...")
        if ( Count_the_words(username_a) > Count_the_words(username_b) ):
            print "User A :",username_a, "has more words in his/her last 10 tweets than User B :", username_b
        elif ( Count_the_words(username_a) < Count_the_words(username_b) ):
            print "User B :", username_b, "has more words in his/her last 10 tweets than User A :", username_a
        else:
            print "User A :", username_a, "and User B :", username_b, "have the same number of words in their last 10 tweets!!"

