from textblob import TextBlob

# User comment (only 1 comment was found on the article so i hardcoded it)
comment = "One of the best articles ever written on the topic. It clearly reflects the differences without any unnecessary details and is really to the point. Great job, Shweta!"

blob = TextBlob(comment)
sentiment_score = blob.sentiment.polarity

#evaluating the sentiment
if sentiment_score > 0:
    sentiment = "positive"
elif sentiment_score < 0:
    sentiment = "negative"
else:
    sentiment = "neutral"


print(f"Sentiment Score: {sentiment_score:.2f}")
print(f"The comment is classified as: {sentiment}")