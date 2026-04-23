import requests

BACKEND_URL = "http://localhost:5000/api/sensor-data"

def simulate_esp8266_send_data(moisture_value):
    print(f"ESP8266 Simulating sending data: Moisture {moisture_value}")
    payload = {"moisture": moisture_value}
    try:
        response = requests.post(BACKEND_URL, json=payload)
        print(f"Backend Response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Failed to reach backend: {e}")

if __name__ == "__main__":
    simulate_esp8266_send_data(850) # Dry soil
