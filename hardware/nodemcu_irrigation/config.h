#ifndef CONFIG_H
#define CONFIG_H

// --- Hardware Pin Definitions ---
#define MOISTURE_SENSOR_PIN A0   // Analog pin for Soil Moisture Sensor
#define PUMP_PIN D1              // Digital pin for Relay (Pump)
#define LED_INDICATOR_PIN D2     // Digital pin for Status LED

// --- Thresholds & Calibration ---
// Note: These values depend on the specific sensor and soil type.
// 0 (wet) to 1024 (dry) is typical for generic analog sensors.
#define DRY_THRESHOLD 700        
#define WET_THRESHOLD 300

// --- System Configuration ---
#define SENSOR_READ_INTERVAL 5000  // Read sensor every 5 seconds
#define DATA_SEND_INTERVAL 10000   // Send data to backend every 10 seconds

// MQTT Settings
#define MQTT_CLIENT_ID "ESP8266_Irrigation_Node_1"
#define MQTT_TOPIC_SENSOR "irrigation/sensor/data"
#define MQTT_TOPIC_CONTROL "irrigation/pump/control"

#endif
