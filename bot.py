import tweepy
import time
#REAL KEY AND SECRET ARE ELSEWHERE FOR SECURITY REASONS
#Api Key: 
consumerKey= 'nice_key'
#API Key Secret:
consumerSecret='secret'

# Bearer Token:
bearer= 'nice bearer'

# Access Token:
key= 'another cool key'

# Access Token Secret:
secret= 'cool secret'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(key, secret)
#Account has a limit on post rate. Too many requests fails it.
api = tweepy.API(auth, wait_on_rate_limit=True) #if a hold exists, wait instead of failing.


#client takes care of Oauth handler automatically
# client = tweepy.Client(bearer_token=bearer,
#     consumer_key=consumerKey,
#     consumer_secret=consumerSecret,
#     access_token=key, access_token_secret=secret)

FILE_NAME= 'last.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


#returns tweets mentioning @MelakSenay and #melbot hashtag

def reply():
    tweets= api.mentions_timeline(count=1,since_id= read_last_seen(FILE_NAME),tweet_mode='extended')
    for tweet in reversed(tweets):
        if "#melbot" in tweet.full_text.lower():
            print(str(tweet.id)+' - '+ tweet.full_text)
            #concatenate to reply to user who mentioned us.
            api.update_status(status="@"+tweet.user.screen_name+ " This is definitely not smash hit artist Drake's burner account! Please carry on and have a nice day- not Drake. <3",in_reply_to_status_id= tweet.id)
            api.create_favorite(id=tweet.id)
            # api.retweet(id=tweet.id) if I wanna retweet I can.
            store_last_seen(FILE_NAME,tweet.id)
while True:
    reply()
    time.sleep(10)



