import redis


def publish_event(event_type, message):
    """Generic function to publish events to Redis."""
    redis_client = redis.Redis(host='redis', port=6379, db=0)
    redis_client.publish(event_type, message)


def publish_cleaned_data_created(file_path):
    """Specific function to publish when cleaned data file is created."""
    publish_event('cleaned_data_created', file_path)
