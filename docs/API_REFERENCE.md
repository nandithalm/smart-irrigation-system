# API Reference

## REST API (Base URL: `/api`)

### `POST /sensor-data`
Receives moisture data from hardware.
- **Body:** `{"moisture": 450}`
- **Response:** `201 Created`

### `GET /sensor-data`
Gets the latest sensor data.
- **Response:** `{"moisture": 450, "timestamp": "..."}`

### `GET /sensor-data/history`
Gets historical data for charts.

### `POST /control`
Sends a command to the pump.
- **Body:** `{"command": "ON" | "OFF"}`

### `GET /control/status`
Gets the latest pump status.

## WebSockets

- **`sensor_update`**: Emitted when new data arrives.
- **`pump_status_update`**: Emitted when pump status changes.
- **`ai_insight`**: Emitted when AI generates a new reasoning.
