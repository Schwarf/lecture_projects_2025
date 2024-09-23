import time
from kafka import KafkaConsumer
from datetime import datetime
import json


def create_consumer():
    return KafkaConsumer(
        'sensor_data',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        consumer_timeout_ms=20000  # Stop iteration if no message after 20 seconds
    )


def process_temperatures():
    consumer = create_consumer()
    next_run_time = time.time() + 30

    temperatures = []

    try:
        while True:
            for message in consumer.poll(timeout_ms=1000).values():
                for payload in message:
                    temperature = payload.value["temperature"]
                    temperatures.append(temperature)

            current_time = time.time()
            if current_time >= next_run_time:
                if temperatures:
                    average_temperature = sum(temperatures) / len(temperatures)
                    max_temperature = max(temperatures)
                    min_temperature = min(temperatures)
                    # Print the results
                    current_time_dt = datetime.fromtimestamp(current_time)
                    print(
                        f"Average Temp: {average_temperature:.2f} °C, Max Temp: {max_temperature} °C, Min Temp: {min_temperature} °C for minute ending at {current_time_dt.strftime('%Y-%m-%d %H:%M:%S')}")

                next_run_time += 30  # Schedule next run
                temperatures = []  # Reset temperatures list


    except KeyboardInterrupt:
        print("Stopped by the user.")

    finally:
        consumer.close()


if __name__ == "__main__":
    process_temperatures()
