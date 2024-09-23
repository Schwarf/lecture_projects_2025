# First steps
- Install kafka and run it.
- Make simple "Hello-World example" with producer and consumer

## Ideas: 
- Simulate a simple temperature sensor:   
  - Implement a simple temperature sensor with start_temperature a default variance etc.   
  - Implement a producer that reads the temperature sensor every 2-10 seconds (randomly) and sends it to Kafka
  - Implement a consumer that processes all messages of the last 30 seconds, implements 
    computes the average of the new values, the min and max temperature of the last interval. 
  - ToDo: Add moving average
- Get real sensor real-time data via web API? 