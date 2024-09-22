import redis
from src.data_processing.tasks import average_computation


def start_subscriber():
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    pubsub = redis_client.pubsub()
    pubsub.subscribe('cleaned_data_created')

    for message in pubsub.listen():
        if message['type'] == 'message':
            file_path = message['data'].decode('utf-8')
            # Call the task that needs the file
            #process_file.delay(file_path)
            average_computation.delay(file_path, "num_comments", "Ask HN")
            average_computation.delay(file_path, "num_comments", "Show HN")
