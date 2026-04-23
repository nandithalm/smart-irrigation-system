from .models import SensorData, PumpLog, AIInsights
from . import db_session
from sqlalchemy import desc

def get_latest_sensor_data():
    return db_session.query(SensorData).order_by(desc(SensorData.timestamp)).first()

def get_historical_sensor_data(limit=50):
    return db_session.query(SensorData).order_by(desc(SensorData.timestamp)).limit(limit).all()

def get_latest_pump_status():
    return db_session.query(PumpLog).order_by(desc(PumpLog.timestamp)).first()

def get_latest_ai_insight():
    return db_session.query(AIInsights).order_by(desc(AIInsights.timestamp)).first()
