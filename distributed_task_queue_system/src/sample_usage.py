import redis
from src.add.tasks import add
from src.clean_data.tasks import clean_data

try:
    client = redis.Redis(host='localhost', port=6379, db=0)
    response = client.ping()
    print("Redis is connected:", response)
except Exception as e:
    print("Redis connection error:", e)

for i in range(1, 10):
    result = add.delay(4+i, 4)
    print(result.get(timeout=10))  # Should print 8


file_path = "/usr/src/app/data/lecture_2025_data/hacker_news/hacker_news.csv"
cleaned_data = clean_data.delay(file_path)

