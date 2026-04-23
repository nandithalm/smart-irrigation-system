#ifndef SECRETS_H
#define SECRETS_H

// Replace with your network credentials
const char* WIFI_SSID = "YOUR_WIFI_SSID";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";

// Replace with your Backend API & MQTT Broker details
const char* BACKEND_URL = "http://192.168.1.100:5000/api/sensor-data"; 
const char* MQTT_BROKER = "192.168.1.100";
const int MQTT_PORT = 1883;

// Optional: API keys if ESP talks directly to external services
// const char* OPENWEATHER_API_KEY = "YOUR_API_KEY";

#endif
