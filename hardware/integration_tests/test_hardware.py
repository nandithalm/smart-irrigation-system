import requests
import time

BACKEND_URL = "http://localhost:5000/api/sensor-data"

def test_hardware_data_post():
    """Simulates sending data from the hardware to the backend API"""
    payload = {
        "moisture": 450 # Mock value
    }
    try:
        response = requests.post(BACKEND_URL, json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except requests.exceptions.ConnectionError:
        print("Failed to connect to backend. Is the server running?")

if __name__ == "__main__":
    print("Running Hardware Integration Test...")
    test_hardware_data_post()
