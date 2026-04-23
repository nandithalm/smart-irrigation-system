from . import db_session
from .models import SensorData, PumpLog, AIInsights

def save_sensor_data(moisture, temperature=None):
    new_data = SensorData(moisture=moisture, temperature=temperature)
    db_session.add(new_data)
    db_session.commit()
    return new_data

def save_pump_log(status, source="MANUAL"):
    log = PumpLog(status=status, source=source)
    db_session.add(log)
    db_session.commit()
    return log

def save_ai_insight(reasoning):
    insight = AIInsights(reasoning=reasoning)
    db_session.add(insight)
    db_session.commit()
    return insight
