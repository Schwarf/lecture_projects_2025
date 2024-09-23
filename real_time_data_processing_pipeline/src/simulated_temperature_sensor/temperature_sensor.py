import time
import random


def temperature_sensor(base_temp=25.0, variance=2.0):
    """ Simulate temperature readings with random fluctuation around a base temperature."""
    while True:
        simulated_temp = base_temp + random.uniform(-variance, variance)
        yield simulated_temp
        time.sleep(1)  