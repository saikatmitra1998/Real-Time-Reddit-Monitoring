# Data Collection for Real-Time Reddit Dashboard

This directory contains the script for collecting data from Reddit and sending it to a Kafka topic in real-time.

## Overview

The data collection process involves:
1. Setting up access to the Reddit API.
2. Streaming data from specified subreddits.
3. Sending the streamed data to a Kafka topic for further processing.

## Prerequisites

Before running the data collection script, ensure you have the following installed:
- Python 3.x
- Apache Kafka
- Zookeeper (for Kafka)
- Virtual environment (recommended)

## Setup Instructions

### Step 1: Create a Reddit App

1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps) and create a new application.
2. Choose the "script" app type.
3. Fill in the details:
   - Name: Your app name
   - App type: Script
   - Description: (Optional)
   - About URL: (Optional)
   - Redirect URI: `http://localhost:8000` or any valid URL
4. Note down the `client_id`, `client_secret`, `username`, `password`, and `user_agent`.

### Step 2: Store Credentials Securely

Create a `.env` file in the `data_collection` directory and add your credentials:

```env
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password
REDDIT_USER_AGENT=your_user_agent