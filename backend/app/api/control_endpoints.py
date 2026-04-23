from flask import request, jsonify
from . import control_bp
from app.mqtt_bridge.mqtt_publisher import send_pump_command
from app.database.crud_operations import save_pump_log
from app.database.data_retrieval import get_latest_pump_status
from app import socketio

@control_bp.route('/control', methods=['POST'])
def control_pump():
    """Manual override from the React UI"""
    data = request.json
    if not data or 'command' not in data:
        return jsonify({"error": "Command not provided"}), 400
        
    command = data['command'].upper() # "ON" or "OFF"
    if command not in ["ON", "OFF"]:
        return jsonify({"error": "Invalid command"}), 400
        
    # Send command via MQTT
    send_pump_command(command)
    
    # Log it
    save_pump_log(command, source="MANUAL")
    
    # Notify UI
    socketio.emit('pump_status_update', {'status': command, 'source': 'MANUAL'})
    
    return jsonify({"status": "success", "command_sent": command}), 200

@control_bp.route('/control/status', methods=['GET'])
def get_pump_status():
    """Get the latest recorded pump status"""
    latest = get_latest_pump_status()
    if not latest:
        return jsonify({"status": "OFF"}), 200
        
    return jsonify({
        "status": latest.status,
        "source": latest.source,
        "timestamp": latest.timestamp.isoformat()
    }), 200
