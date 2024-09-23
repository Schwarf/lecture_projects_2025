import time
import random


def simulate_temperature_with_outliers(base_temp=25.0, variance=2.0, outlier_chance=0.01):
    """ Simulate temperature readings with random fluctuation and occasional outliers. """
    while True:
        if random.random() < outlier_chance:
            # Generate an outlier
            outlier_multiplier = random.uniform(1, 5*variance)
            outlier_variance = variance * outlier_multiplier
            simulated_temp = base_temp + random.choice([-1, 1]) * random.uniform(variance, outlier_variance)
        else:
            # Normal fluctuation
            simulated_temp = base_temp + random.uniform(-variance, variance)
        yield simulated_temp
        time.sleep(1)
