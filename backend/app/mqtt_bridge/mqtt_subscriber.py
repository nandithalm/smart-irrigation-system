import paho.mqtt.client as mqtt
import json
import eventlet
from .broker_config import MQTT_BROKER, MQTT_PORT, TOPIC_SENSOR

# Use a global client instance
client = mqtt.Client(client_id="flask_backend_sub")

def on_connect(client, userdata, flags, rc):
    print(f"MQTT Connected with result code {rc}")
    client.subscribe(TOPIC_SENSOR)

def on_message(client, userdata, msg):
    """
    Handle incoming MQTT messages from ESP8266.
    (This runs in a background thread/greenlet)
    """
    try:
        payload = msg.payload.decode()
        data = json.loads(payload)
        
        # We need to process this data. 
        # Since this is running outside the Flask request context, 
        # we can use the app context to access DB, or just send a request to our own API.
        
        # For simplicity in this demo, let's use the requests library to send it to our own REST endpoint
        # so it follows the same path as if it were an HTTP POST.
        import requests
        requests.post("http://localhost:5000/api/sensor-data", json=data)
        
    except Exception as e:
        print(f"Error processing MQTT message: {e}")

client.on_connect = on_connect
client.on_message = on_message

def start_mqtt(app):
    """
    Start the MQTT loop in a background thread.
    """
    def _run():
        try:
            client.connect(MQTT_BROKER, MQTT_PORT, 60)
            client.loop_forever()
        except Exception as e:
            print(f"MQTT Subscriber could not start: {e}")

    # Run in background to avoid blocking Flask
    eventlet.spawn(_run)
