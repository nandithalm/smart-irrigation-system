# Hardware Setup Guide

## Components Required
- ESP8266 NodeMCU
- Soil Moisture Sensor (Analog)
- 5V Relay Module
- Submersible Water Pump (5V or 12V)
- Connecting wires

## Wiring Diagram
- **Moisture Sensor:** 
  - VCC -> 3.3V
  - GND -> GND
  - A0 -> NodeMCU A0
- **Relay Module (Pump):**
  - VCC -> 5V or VIN (if using USB power)
  - GND -> GND
  - IN -> NodeMCU D1
- **LED Indicator:**
  - Anode -> NodeMCU D2
  - Cathode -> Resistor (220 ohm) -> GND
