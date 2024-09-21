from src.celery_app import app
import redis

@app.task
def clean_data(file_path):
    import pandas as pd
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Data cleaning steps
    # Remove entries with missing 'url'
    df = df.dropna(subset=['url'])

    # Convert 'created_at' to datetime
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')

    # Save the cleaned data to a new CSV in DOCKER-CONTAINER
    cleaned_file_path = '/home/docker_user/container_data/cleaned_hacker_news_data.csv'
    df.to_csv(cleaned_file_path, index=False)
    publish_file_creation(cleaned_file_path)
    return cleaned_file_path


def publish_file_creation(file_path):
    """Publish an event to Redis to notify about the creation of a file."""
    redis_client = redis.Redis(host='redis', port=6379, db=0)
    redis_client.publish('file_created', file_path)

