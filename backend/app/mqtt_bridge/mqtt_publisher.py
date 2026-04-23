import paho.mqtt.publish as publish
from .broker_config import MQTT_BROKER, MQTT_PORT, TOPIC_CONTROL

def send_pump_command(command: str):
    """
    Publishes a command to the MQTT broker to control the pump.
    command: "ON" or "OFF"
    """
    try:
        publish.single(TOPIC_CONTROL, payload=command, hostname=MQTT_BROKER, port=MQTT_PORT)
        print(f"MQTT Published: {command} to {TOPIC_CONTROL}")
    except Exception as e:
        print(f"Failed to publish MQTT message: {e}")
