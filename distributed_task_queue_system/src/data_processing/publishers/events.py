import redis
from redis.typing import EncodableT, ChannelT


def publish_event(event_type: ChannelT, message: EncodableT) -> None:
    """Generic function to publish events to Redis."""
    redis_client = redis.Redis(host='redis', port=6379, db=0)
    redis_client.publish(event_type, message)


def store_average_value(average_value: float, key: str) -> None:
    redis_client = redis.Redis(host='redis', port=6379, db=0)
    redis_client.set(key, average_value)
