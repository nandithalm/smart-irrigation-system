# Integration Guide

This document explains how the hardware and software talk to each other.

## Data Flow
1. **ESP8266** reads soil moisture.
2. **ESP8266** sends data via HTTP POST to `/api/sensor-data` AND publishes to MQTT topic `irrigation/sensor/data`.
3. **Backend** receives HTTP POST, saves to DB, emits WebSocket event `sensor_update` to React Frontend.
4. **Backend AI** evaluates data, saves insight, emits `ai_insight` to React Frontend.
5. If pump needs to turn on, **Backend** publishes "ON" to `irrigation/pump/control`.
6. **ESP8266** receives MQTT message and turns relay ON.

## Manual Override Flow
1. User clicks "Turn ON" in **React Frontend**.
2. **React** sends HTTP POST to `/api/control` with `{"command": "ON"}`.
3. **Backend** publishes to MQTT topic `irrigation/pump/control`.
4. **Backend** emits WebSocket event `pump_status_update`.
5. **ESP8266** receives MQTT message and turns relay ON.
