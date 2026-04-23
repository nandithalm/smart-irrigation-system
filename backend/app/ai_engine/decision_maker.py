from .fuzzy_controller import FuzzyController
from .weather_api import get_rain_probability
from app.mqtt_bridge.mqtt_publisher import send_pump_command
from app.database.crud_operations import save_pump_log, save_ai_insight
from app import socketio

fuzzy = FuzzyController()

def evaluate_conditions(moisture_level):
    """
    Combines sensor data with weather data to make a decision.
    """
    # 1. Fetch weather forecast (mocked or real)
    rain_prob = get_rain_probability()
    
    # 2. Evaluate using Fuzzy Logic
    need_water, reasoning = fuzzy.get_irrigation_need(moisture_level, rain_prob)
    
    # 3. Log AI Insight
    save_ai_insight(reasoning)
    
    # Push insight to UI
    socketio.emit('ai_insight', {'reasoning': reasoning, 'rain_prob': rain_prob})
    
    # 4. Actuate Pump
    command = "ON" if need_water else "OFF"
    
    # Only send command if it's changing state (optimization)
    # For demonstration, we'll send it and log it
    send_pump_command(command)
    save_pump_log(command, source="AI_AUTO")
    
    # Notify UI
    socketio.emit('pump_status_update', {'status': command, 'source': 'AI_AUTO'})
