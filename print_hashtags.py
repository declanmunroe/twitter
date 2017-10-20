import json

results = []

tweets_file = open('tweet_mining.json', "r")
for tweet_line in tweets_file:
    try:
        status = json.loads(tweet_line)
        results.append(status)
    except:
        continue

new_ht = []

for tweet in results:
    hashtags = tweet['entities']['hashtags']
    for ht in hashtags:
        new_ht.append(ht["text"])
        # print(type(new_ht))
        print(new_ht)
        


# count = 0 
# for tweet in results:
#     hashtags = tweet['entities']['hashtags']
#     if not hashtags == []:
#         count += 1
#         print(type(hashtags))
#         print(count)     