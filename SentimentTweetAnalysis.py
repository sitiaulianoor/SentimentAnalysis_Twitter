from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

def percentage (part, whole):
    return 100 * float(part)/float(whole)

accessToken = "972186198419456001-WVuR4sz1zDN0pdhQbtCMaowWzEgJXJ9"
accessTokenSecret = "dMzGbNN9vTtyo2IIrroJu5aL16VsHGbIiRERenS1Z5fLx"
consumerKey = "pYs4VxguClqhL3ub1plbc2ETr"
consumerSecret = "5M9TysAWGrVaMfWUJ2gZX7YPw9BiSSN9ympHP3vQSaRpJOno9r"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


searchTerm = input("enter your keyword : ")
noOfSearchTerms = int(input("how many tweet : "))

tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    if (analysis.sentiment.polarity == 0):
        neutral +=1
    elif (analysis.sentiment.polarity < 0):
        neutral +=1

    elif (analysis.sentiment.polarity > 0):
        neutral +=1


positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print("How People reacting on "+ searchTerm + " by analyzing"+ str(noOfSearchTerms) + " Tweets.")

if (polarity == 0):
    print("Neutral")
elif (polarity < 0):
    print("Negative")
elif (polarity > 0):
    print("Positive")

labels = ['Positive['+str(positive) + '%]', 'Neutral ['+str(neutral) +'%]', 'Negative ['+str(negative) + '%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen','blue','red']
patches, texts = plt.pie(sizes, colors=colors, startangle=98)
plt.legend(patches, loc="best")
plt.title("Sentiment Analysis "+ searchTerm + "by "+str(noOfSearchTerms)+" Tweets.")
plt.axis("equal")
plt.tight_layout()
plt.show()
