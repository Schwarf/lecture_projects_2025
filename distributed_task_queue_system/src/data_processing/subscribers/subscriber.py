import redis
from src.data_processing.tasks import average_computation


def subscriber():
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    pubsub = redis_client.pubsub()
    pubsub.subscribe('cleaned_data_created', 'average_computation_done')
    count_average_computations = 0
    for message in pubsub.listen():
        if message['type'] == 'message':
            data = message['data'].decode('utf-8')  # Get the data/payload of the message
            channel = message['channel'].decode('utf-8')  # Get the channel/intent of the message

            if channel == "average_computation_done":  # Break the loop when both computations are done
                count_average_computations += 1
                if count_average_computations == 2:
                    break
            elif channel == "cleaned_data_created":  # When the cleaned data is available start the data processing
                average_computation.delay(data, "num_comments", "Ask HN")
                average_computation.delay(data, "num_comments", "Show HN")
