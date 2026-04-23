import random

def get_rain_probability():
    """
    Simulates calling an external weather API like OpenWeatherMap.
    Returns a probability between 0.0 and 1.0.
    """
    # In a real scenario, you'd use requests.get() to fetch the weather forecast.
    # For demonstration, we'll return a random probability.
    
    # Simulate a 30% chance it's going to rain soon
    if random.random() < 0.3:
        return random.uniform(0.7, 1.0) # High probability
    else:
        return random.uniform(0.0, 0.3) # Low probability
