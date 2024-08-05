import os
import praw
import json
from kafka import KafkaProducer
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Reddit API with credentials from environment variables
reddit = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                     client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                     username=os.getenv('REDDIT_USERNAME'),
                     password=os.getenv('REDDIT_PASSWORD'),
                     user_agent=os.getenv('REDDIT_USER_AGENT'))

# Initialize Kafka Producer
producer = KafkaProducer(bootstrap_servers='kafka:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

subreddits = ['subreddit1', 'subreddit2']  # List of subreddits to stream

def stream_subreddit_data():
    for subreddit in subreddits:
        subreddit_stream = reddit.subreddit(subreddit).stream.submissions()
        for submission in subreddit_stream:
            try:
                data = {
                    'id': submission.id,
                    'title': submission.title,
                    'score': submission.score,
                    'created_utc': submission.created_utc,
                    'num_comments': submission.num_comments,
                    'subreddit': submission.subreddit.display_name
                }
                producer.send('reddit_topic', data)
                print(f"Sent data to Kafka: {data}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    stream_subreddit_data()