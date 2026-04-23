import paho.mqtt.publish as publish
import time

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
TOPIC_CONTROL = "irrigation/pump/control"

def simulate_backend_command(command):
    print(f"Backend Simulating sending command: {command} via MQTT")
    try:
        publish.single(TOPIC_CONTROL, payload=command, hostname=MQTT_BROKER, port=MQTT_PORT)
        print("Command sent successfully.")
    except Exception as e:
        print(f"MQTT Publish failed: {e}")

if __name__ == "__main__":
    simulate_backend_command("ON")
    time.sleep(2)
    simulate_backend_command("OFF")
