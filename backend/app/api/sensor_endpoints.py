from flask import request, jsonify
from . import sensor_bp
from app.database.crud_operations import save_sensor_data
from app.database.data_retrieval import get_latest_sensor_data, get_historical_sensor_data
from app.ai_engine.decision_maker import evaluate_conditions
from app import socketio

@sensor_bp.route('/sensor-data', methods=['POST'])
def receive_sensor_data():
    """Receive data from ESP8266 via HTTP POST"""
    data = request.json
    if not data or 'moisture' not in data:
        return jsonify({"error": "Invalid data format"}), 400

    moisture = data['moisture']
    
    # Save to database
    save_sensor_data(moisture)
    
    # Push update to UI via WebSocket
    socketio.emit('sensor_update', {'moisture': moisture})
    
    # Run AI evaluation
    evaluate_conditions(moisture)
    
    return jsonify({"status": "success", "message": "Data received"}), 201

@sensor_bp.route('/sensor-data', methods=['GET'])
def get_sensor_data():
    """Fetch latest sensor data for the UI"""
    latest = get_latest_sensor_data()
    if not latest:
        return jsonify({"moisture": 0, "status": "No data"}), 200
        
    return jsonify({
        "moisture": latest.moisture,
        "temperature": latest.temperature,
        "timestamp": latest.timestamp.isoformat()
    }), 200

@sensor_bp.route('/sensor-data/history', methods=['GET'])
def get_history():
    """Fetch historical data for charts"""
    history = get_historical_sensor_data(limit=20)
    data = [{
        "moisture": item.moisture,
        "timestamp": item.timestamp.isoformat()
    } for item in history]
    
    return jsonify(data), 200
