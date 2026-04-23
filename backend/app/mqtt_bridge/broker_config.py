import os

MQTT_BROKER = os.environ.get('MQTT_BROKER', 'localhost')
MQTT_PORT = int(os.environ.get('MQTT_PORT', 1883))

TOPIC_CONTROL = "irrigation/pump/control"
TOPIC_SENSOR = "irrigation/sensor/data"
