import random

def generate_interarrival_time():
    """Generate interarrival time using exponential distribution with mean 5 hours."""
    return random.expovariate(1 / 300)  # 300 minutes = 5 hours