#!/bin/bash
# Note: You need arduino-cli installed for this to work
PORT=/dev/ttyUSB0
FQBN=esp8266:esp8266:nodemcuv2

echo "Compiling..."
arduino-cli compile --fqbn $FQBN ../hardware/nodemcu_irrigation/nodemcu_irrigation.ino

echo "Uploading..."
arduino-cli upload -p $PORT --fqbn $FQBN ../hardware/nodemcu_irrigation/nodemcu_irrigation.ino

echo "Done!"
