import time

from kafka import KafkaProducer
from src.simulated_temperature_sensor.temperature_sensor import simulate_temperature_with_outliers
import json


def get_kafka_producer() -> KafkaProducer:
    return KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


def send_data_to_kafka(topic) -> None:
    producer = get_kafka_producer()
    temperature_sensor = simulate_temperature_with_outliers()
    for reading in temperature_sensor:
        message = {"temperature": reading, "timestamp": time.time()}
        producer.send(topic, message)
        producer.flush()
        time.sleep(1)


if __name__ == "__main__":
    send_data_to_kafka('sensor_data')
