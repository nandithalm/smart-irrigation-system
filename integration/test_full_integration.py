import unittest
import requests
import time
import threading
from .backend_to_esp8266 import simulate_backend_command
from .esp8266_to_backend import simulate_esp8266_send_data

class TestFullIntegration(unittest.TestCase):
    
    def test_end_to_end_sensor_flow(self):
        """Test sending data from ESP mockup to backend REST API"""
        # We assume the Flask backend is running on localhost:5000
        try:
            simulate_esp8266_send_data(350)
            # Fetch latest data to see if it was saved
            resp = requests.get("http://localhost:5000/api/sensor-data")
            self.assertEqual(resp.status_code, 200)
            data = resp.json()
            # If DB is empty this might fail, so we just check the status
            self.assertIn("moisture", data)
        except requests.exceptions.ConnectionError:
            self.fail("Backend is not running. Please start Flask app first.")

    def test_mqtt_command_flow(self):
        """Test publishing MQTT command from Backend mockup to ESP"""
        # We assume Mosquitto broker is running on localhost:1883
        # Since we can't easily assert MQTT without a listening client, we just run it
        try:
            simulate_backend_command("ON")
            time.sleep(1)
            simulate_backend_command("OFF")
        except Exception as e:
            self.fail(f"MQTT Publish failed: {e}")

if __name__ == '__main__':
    unittest.main()
