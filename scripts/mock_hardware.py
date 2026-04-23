import time
import random
import requests

BACKEND_URL = "http://localhost:5000/api/sensor-data"

def run_mock():
    print("Starting Hardware Mock...")
    moisture = 500
    while True:
        # Simulate soil drying out
        moisture += random.randint(-10, 30)
        
        # Keep within bounds
        if moisture > 1000:
            moisture = 1000
            
        print(f"Sending Mock Moisture: {moisture}")
        try:
            requests.post(BACKEND_URL, json={"moisture": moisture})
        except requests.exceptions.ConnectionError:
            print("Failed to reach backend. Retrying in 10s...")
            
        time.sleep(10)

if __name__ == "__main__":
    run_mock()
