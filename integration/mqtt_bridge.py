import paho.mqtt.client as mqtt
import time

# This script can act as a simple bridge/logger to test if messages are flowing
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
TOPICS = [("irrigation/pump/control", 0), ("irrigation/sensor/data", 0)]

def on_connect(client, userdata, flags, rc):
    print(f"Test Bridge Connected with result code {rc}")
    client.subscribe(TOPICS)
    print(f"Subscribed to topics: {[t[0] for t in TOPICS]}")

def on_message(client, userdata, msg):
    print(f"[{msg.topic}] : {msg.payload.decode()}")

client = mqtt.Client(client_id="test_bridge")
client.on_connect = on_connect
client.on_message = on_message

if __name__ == "__main__":
    try:
        print("Starting MQTT Bridge Tester...")
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_forever()
    except KeyboardInterrupt:
        print("Stopping bridge tester.")
