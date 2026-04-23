#include "config.h"
#include "secrets.h"
#include "debug.h"
#include "communication.h"

unsigned long lastReadTime = 0;
unsigned long lastSendTime = 0;

void setup() {
  // Initialize Debug Serial
  DEBUG_BEGIN(115200);
  DEBUG_PRINTLN("\n--- Smart Irrigation System Started ---");

  // Initialize Pins
  pinMode(MOISTURE_SENSOR_PIN, INPUT);
  pinMode(PUMP_PIN, OUTPUT);
  pinMode(LED_INDICATOR_PIN, OUTPUT);
  
  // Ensure pump is OFF initially (assuming HIGH triggers relay, adjust if needed)
  digitalWrite(PUMP_PIN, LOW);
  digitalWrite(LED_INDICATOR_PIN, LOW);

  // Setup WiFi and MQTT
  setupWiFi();
  mqttClient.setServer(MQTT_BROKER, MQTT_PORT);
  mqttClient.setCallback(mqttCallback);
}

void loop() {
  // Ensure MQTT connection is alive
  if (!mqttClient.connected()) {
    reconnectMQTT();
  }
  mqttClient.loop();

  unsigned long currentMillis = millis();

  // Read Sensor Data Periodically
  if (currentMillis - lastReadTime >= SENSOR_READ_INTERVAL) {
    lastReadTime = currentMillis;
    
    int moistureValue = analogRead(MOISTURE_SENSOR_PIN);
    DEBUG_PRINT("Raw Moisture Value: ");
    DEBUG_PRINTLN(moistureValue);
    
    // Optional: Local fail-safe logic (if backend fails)
    // if (moistureValue > DRY_THRESHOLD) {
    //   digitalWrite(PUMP_PIN, HIGH); 
    // }

    // Send Data Periodically
    if (currentMillis - lastSendTime >= DATA_SEND_INTERVAL) {
      lastSendTime = currentMillis;
      
      // Indicate data transmission
      digitalWrite(LED_INDICATOR_PIN, HIGH);
      
      // Send data via both REST and MQTT to demonstrate architecture
      // In production, you might choose just one
      sendDataHTTP(moistureValue);
      sendDataMQTT(moistureValue);
      
      digitalWrite(LED_INDICATOR_PIN, LOW);
    }
  }
}
