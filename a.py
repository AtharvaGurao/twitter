import pandas as pd
import random

# Sample good and bad words
good_words = ["love", "beautiful", "great", "amazing", "grateful", "fantastic", "happy", "excited", "optimistic", "enjoying"]
bad_words = ["hate", "terrible", "worst", "tired", "frustrated", "overwhelmed", "disappointed", "stressed", "anxious", "upset"]

# Sample positive, neutral, and negative tweets
positive_tweets = [
    "I love this movie!",
    "The weather is beautiful today.",
    "I had a great day.",
    "Today was amazing!",
    "I'm so grateful for everything.",
    "The food at that restaurant was fantastic.",
    "I got promoted at work!",
    "This vacation was exactly what I needed.",
    "I'm feeling so happy right now.",
    "Spending time with friends always makes me smile.",
    "Life is good!",
    "I accomplished my goals today.",
    "I'm surrounded by wonderful people.",
    "Every day is a blessing.",
    "I'm so proud of myself.",
    "The sun is shining!",
    "I'm in a great mood today.",
    "I'm so excited about the future.",
    "I'm feeling optimistic about everything.",
    "I'm enjoying every moment."
]

neutral_tweets = [
    "I'm going to the grocery store.",
    "This book is okay.",
    "It's raining outside.",
    "I have some errands to run.",
    "Just finished my homework.",
    "The movie I watched was alright.",
    "Nothing special happened today.",
    "I need to do some laundry.",
    "I'm thinking about what to have for dinner.",
    "It's just another typical day.",
    "Today is neither good nor bad.",
    "I'm feeling indifferent about everything.",
    "I'm neutral about this situation.",
    "I don't have strong feelings either way.",
    "I'm not particularly excited or upset.",
    "Just going through the motions.",
    "It's a standard day.",
    "I'm feeling neither happy nor sad.",
    "Nothing out of the ordinary happened.",
    "Just another regular day."
]

negative_tweets = [
    "I'm feeling sick.",
    "I hate Mondays.",
    "The traffic is terrible.",
    "I had a terrible day.",
    "This is the worst day ever.",
    "I'm so tired of this.",
    "My car broke down.",
    "I lost my wallet.",
    "I'm not feeling well.",
    "Everything is going wrong.",
    "I can't stand this anymore.",
    "I'm so frustrated right now.",
    "I'm feeling overwhelmed.",
    "I'm disappointed with the results.",
    "I'm feeling really down today.",
    "Nothing is going my way.",
    "I'm in a bad mood.",
    "I'm so stressed out.",
    "I'm feeling really anxious.",
    "I'm upset about what happened."
]

# Generate the dataset
data = {'Name': [], 'Tweet': [], 'Sentiment': []}

# Add minimum 20 tweets for each sentiment category
for _ in range(20):
    for tweet in positive_tweets:
        name = random.choice(['John', 'Alice', 'Bob', 'Emma', 'Michael', 'Sophia', 'Daniel', 'Olivia', 'James', 'Emily'])
        data['Name'].append(name)
        tweet_with_word = tweet.replace("!", " " + random.choice(good_words) + "!")
        data['Tweet'].append(tweet_with_word)
        data['Sentiment'].append(1)  # Positive sentiment
    
    for tweet in neutral_tweets:
        name = random.choice(['John', 'Alice', 'Bob', 'Emma', 'Michael', 'Sophia', 'Daniel', 'Olivia', 'James', 'Emily'])
        data['Name'].append(name)
        data['Tweet'].append(tweet)
        data['Sentiment'].append(2)  # Neutral sentiment
    
    for tweet in negative_tweets:
        name = random.choice(['John', 'Alice', 'Bob', 'Emma', 'Michael', 'Sophia', 'Daniel', 'Olivia', 'James', 'Emily'])
        data['Name'].append(name)
        tweet_with_word = tweet.replace("!", " " + random.choice(bad_words) + "!")
        data['Tweet'].append(tweet_with_word)
        data['Sentiment'].append(0)  # Negative sentiment

# Shuffle the dataset
df = pd.DataFrame(data).sample(frac=1).reset_index(drop=True)

# Save the dataset to a CSV file
df.to_csv('twitter_sentiment_dataset.csv', index=False)

print("Dataset saved as 'twitter_sentiment_dataset.csv'")
