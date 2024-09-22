import redis


def publish_event(event_type, message):
    """Generic function to publish events to Redis."""
    redis_client = redis.Redis(host='redis', port=6379, db=0)
    redis_client.publish(event_type, message)


def store_average_value(average_value: float, key: str):
    redis_client = redis.Redis(host='redis', port=6379, db=0)
    redis_client.set(key, average_value)
