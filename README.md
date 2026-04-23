# Smart Irrigation System

A complete IoT-based Smart Irrigation System with a React frontend, Python Flask backend, and simulated/real ESP8266 NodeMCU hardware integration. It uses an AI engine (Fuzzy Logic) to determine irrigation needs based on soil moisture and weather.

## Architecture
- **Frontend**: React, Vite, Axios, Socket.io-client
- **Backend**: Python, Flask, SQLite, MQTT, OpenWeatherMap (simulated)
- **Hardware**: ESP8266 NodeMCU (or Python mock script)
- **Messaging**: MQTT for real-time hardware commands, REST for data syncing, WebSockets for UI updates.

## Getting Started

### 1. Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app/main.py
```

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### 3. Hardware Simulation
If you don't have the ESP8266, you can run the simulator:
```bash
cd scripts
python mock_hardware.py
```

### 4. Docker
You can also run the entire stack using Docker:
```bash
docker-compose up --build
```
