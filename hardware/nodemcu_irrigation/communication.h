#ifndef COMMUNICATION_H
#define COMMUNICATION_H

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <PubSubClient.h>
#include <WiFiClient.h>
#include "secrets.h"
#include "config.h"
#include "debug.h"

WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);

// Function to handle incoming MQTT messages (pump control)
void mqttCallback(char* topic, byte* payload, unsigned int length) {
  DEBUG_PRINT("Message arrived on topic: ");
  DEBUG_PRINTLN(topic);
  
  String message = "";
  for (unsigned int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  
  DEBUG_PRINT("Message: ");
  DEBUG_PRINTLN(message);

  if (String(topic) == MQTT_TOPIC_CONTROL) {
    if (message == "ON") {
      digitalWrite(PUMP_PIN, HIGH);
      DEBUG_PRINTLN("Pump turned ON via MQTT");
    } else if (message == "OFF") {
      digitalWrite(PUMP_PIN, LOW);
      DEBUG_PRINTLN("Pump turned OFF via MQTT");
    }
  }
}

// Connect to WiFi
void setupWiFi() {
  delay(10);
  DEBUG_PRINTLN();
  DEBUG_PRINT("Connecting to WiFi: ");
  DEBUG_PRINTLN(WIFI_SSID);

  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    DEBUG_PRINT(".");
  }

  DEBUG_PRINTLN("");
  DEBUG_PRINTLN("WiFi connected.");
  DEBUG_PRINT("IP address: ");
  DEBUG_PRINTLN(WiFi.localIP());
}

// Reconnect MQTT
void reconnectMQTT() {
  while (!mqttClient.connected()) {
    DEBUG_PRINT("Attempting MQTT connection...");
    if (mqttClient.connect(MQTT_CLIENT_ID)) {
      DEBUG_PRINTLN("connected");
      // Subscribe to control topic
      mqttClient.subscribe(MQTT_TOPIC_CONTROL);
    } else {
      DEBUG_PRINT("failed, rc=");
      DEBUG_PRINT(mqttClient.state());
      DEBUG_PRINTLN(" try again in 5 seconds");
      delay(5000);
    }
  }
}

// Send data via HTTP REST
void sendDataHTTP(int moistureLevel) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(wifiClient, BACKEND_URL);
    http.addHeader("Content-Type", "application/json");

    // Create simple JSON payload
    String payload = "{\"moisture\": " + String(moistureLevel) + "}";
    
    int httpResponseCode = http.POST(payload);
    
    if (httpResponseCode > 0) {
      DEBUG_PRINT("HTTP Response code: ");
      DEBUG_PRINTLN(httpResponseCode);
    } else {
      DEBUG_PRINT("Error code: ");
      DEBUG_PRINTLN(httpResponseCode);
    }
    http.end();
  } else {
    DEBUG_PRINTLN("WiFi Disconnected");
  }
}

// Send data via MQTT
void sendDataMQTT(int moistureLevel) {
  if (!mqttClient.connected()) {
    reconnectMQTT();
  }
  mqttClient.loop();

  String payload = "{\"moisture\": " + String(moistureLevel) + "}";
  mqttClient.publish(MQTT_TOPIC_SENSOR, payload.c_str());
  DEBUG_PRINT("MQTT Published: ");
  DEBUG_PRINTLN(payload);
}

#endif
