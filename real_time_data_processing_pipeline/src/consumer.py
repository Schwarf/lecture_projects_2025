from kafka import KafkaConsumer
import json

# Create a Kafka consumer
consumer = KafkaConsumer('test',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Read and print messages
for message in consumer:
    print(f"Received message: {message.value}")

