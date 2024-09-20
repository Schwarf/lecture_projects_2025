import redis
from src.add_task import add

try:
    client = redis.Redis(host='localhost', port=6379, db=0)
    response = client.ping()
    print("Redis is connected:", response)
except Exception as e:
    print("Redis connection error:", e)

for i in range(1, 10):
    result = add.delay(4+i, 4)
    print(result.get(timeout=10))  # Should print 8
