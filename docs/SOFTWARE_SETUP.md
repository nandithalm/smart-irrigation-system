# Software Setup Guide

## Prerequisites
- Node.js (v18+)
- Python (3.10+)
- Docker (optional)
- Mosquitto MQTT Broker

## Running Locally (Without Docker)
1. **MQTT Broker:** Start Mosquitto locally.
2. **Backend:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   python app/main.py
   ```
3. **Frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Using Docker
Run `docker-compose up --build` from the root directory.
