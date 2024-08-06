# Real-time Reddit Monitoring

This project is designed to monitor Reddit data in real-time. It streams data from specified subreddits using Kafka, preprocesses it, and stores it in a PostgreSQL database. The project uses Docker and Docker Compose for easy deployment and management.

## Table of Contents

- [Project Overview](#project-overview)
- [Directory Structure](#directory-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Makefile Commands](#makefile-commands)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project consists of several components:
- **reddit_stream.py**: Streams Reddit data to Kafka.
- **preprocess.py**: (Optional) Preprocesses the data.
- **store_data.py**: Consumes Kafka messages and stores them in PostgreSQL.

## Prerequisites

Before you begin, ensure you have the following installed:
- Docker
- Docker Compose

## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/real-time-reddit-monitoring.git
    cd real-time-reddit-monitoring
    ```

2. **Set up environment variables**:
    Create a `.env` file in the project root directory and add your Reddit and PostgreSQL credentials:
    ```env
    # Reddit API credentials
    REDDIT_CLIENT_ID=your_reddit_client_id
    REDDIT_CLIENT_SECRET=your_reddit_client_secret
    REDDIT_USERNAME=your_reddit_username
    REDDIT_PASSWORD=your_reddit_password
    REDDIT_USER_AGENT=your_user_agent

    # PostgreSQL credentials
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    POSTGRES_DB=reddit_db
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    ```

3. **Build and run the Docker containers**:
    ```sh
    make up
    ```

## Usage

- **Start the application**:
    ```sh
    make up
    ```

- **Stop the application**:
    ```sh
    make down
    ```

- **View logs**:
    ```sh
    make logs
    ```

## Environment Variables

Ensure the following environment variables are set in your `.env` file:

- `REDDIT_CLIENT_ID`: Your Reddit client ID
- `REDDIT_CLIENT_SECRET`: Your Reddit client secret
- `REDDIT_USERNAME`: Your Reddit username
- `REDDIT_PASSWORD`: Your Reddit password
- `REDDIT_USER_AGENT`: Your Reddit user agent
- `POSTGRES_USER`: PostgreSQL username
- `POSTGRES_PASSWORD`: PostgreSQL password
- `POSTGRES_DB`: PostgreSQL database name
- `POSTGRES_HOST`: PostgreSQL host (usually the service name in Docker Compose)
- `POSTGRES_PORT`: PostgreSQL port (default is 5432)

## Makefile Commands

- **`make up`**: Build and start the Docker containers.
- **`make down`**: Stop and remove the Docker containers.
- **`make logs`**: View logs of the running containers.
- **`make build`**: Build the Docker images.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
