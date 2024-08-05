import os
import json
import psycopg2
from kafka import KafkaConsumer
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'reddit_topic',  # Ensure this is the correct topic name
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Database connection
try:
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT")
    )
    cur = conn.cursor()
    print("Connected to the database successfully")
except Exception as e:
    print(f"Error connecting to the database: {e}")

# Create table if not exists
try:
    cur.execute('''
        CREATE TABLE IF NOT EXISTS reddit_data (
            id TEXT PRIMARY KEY,
            title TEXT,
            score INT,
            created_utc TIMESTAMP,
            num_comments INT,
            subreddit TEXT,
            processed BOOLEAN
        )
    ''')
    conn.commit()
    print("Table created successfully")
except Exception as e:
    print(f"Error creating table: {e}")

def store_data(data):
    try:
        data['processed'] = True  # Ensure the 'processed' key is present in the data dictionary
        created_utc = datetime.utcfromtimestamp(data['created_utc'])  # Convert UNIX timestamp to datetime
        cur.execute('''
            INSERT INTO reddit_data (id, title, score, created_utc, num_comments, subreddit, processed)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        ''', (data['id'], data['title'], data['score'], created_utc, data['num_comments'], data['subreddit'], data['processed']))
        conn.commit()
        print(f"Stored data: {data}")
    except Exception as e:
        print(f"Error storing data: {e}")
        conn.rollback()  # Rollback the transaction to clear the error

def consume_and_store():
    print("Starting to consume messages...")
    for message in consumer:
        data = message.value
        print(f"Received message: {data}")
        store_data(data)

if __name__ == "__main__":
    consume_and_store()