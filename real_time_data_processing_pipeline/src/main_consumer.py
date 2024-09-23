from datetime import datetime, timedelta, timezone
from kafka import KafkaConsumer
import json


def create_consumer():
    return KafkaConsumer(
        'sensor_data',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        consumer_timeout_ms=20000  # Stop iteration if no message after 2000 ms
    )


def process_temperatures():
    consumer = create_consumer()
    start_time = datetime.utcnow().replace(tzinfo=timezone.utc)
    end_time = start_time + timedelta(minutes=1)

    temperatures = []

    try:
        for message in consumer:
            temperature = message.value['temperature']
            timestamp = message.value['timestamp']
            message_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)

            print(f"Received: {temperature} at {message_time}")  # Debug print

            # Add temperature to list
            temperatures.append(temperature)

            # Check if the current message is still within the current minute
            if message_time >= end_time:
                if temperatures:
                    # Compute statistics
                    average_temp = sum(temperatures) / len(temperatures)
                    max_temp = max(temperatures)
                    min_temp = min(temperatures)

                    # Print the results
                    print(
                        f"Average Temp: {average_temp:.2f} °C, Max Temp: {max_temp} °C, Min Temp: {min_temp} °C for minute ending at {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

                # Reset for the next minute
                temperatures = []
                start_time = message_time
                end_time = start_time + timedelta(minutes=1)

    except KeyboardInterrupt:
        print("Stopped by the user.")

    finally:
        consumer.close()


if __name__ == "__main__":
    process_temperatures()
