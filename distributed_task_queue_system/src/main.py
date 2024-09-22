import gevent
# import threading
from gevent import monkey
monkey.patch_all()

import redis
from src.add.tasks import add
from src.clean_data.tasks import clean_data
from data_processing.subscribers.subscriber import start_subscriber


def main():
    # Start the subscriber in a separate thread
    # thread = threading.Thread(target=start_subscriber)
    # thread.start()

    subscriber_greenlet = gevent.spawn(start_subscriber)
    try:
        client = redis.Redis(host='localhost', port=6379, db=0)
        response = client.ping()
        print("Redis is connected:", response)
    except Exception as e:
        print("Redis connection error:", e)

    for i in range(1, 10):
        result = add.delay(4 + i, 4)
        print(result.get(timeout=10))  # Should print 8

    # This file-path needs to point to the data path in the container.
    file_path = '/home/docker_user/container_data/hacker_news.csv'
    cleaned_data = clean_data.delay(file_path)

    subscriber_greenlet.join()
    # Wait for the subscriber thread to finish (it won't unless the program exits or an exception occurs)
    # thread.join()


if __name__ == "__main__":
    main()