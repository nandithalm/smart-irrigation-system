from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean
from datetime import datetime
from . import Base

class SensorData(Base):
    __tablename__ = 'sensor_data'
    id = Column(Integer, primary_key=True)
    moisture = Column(Float, nullable=False)
    temperature = Column(Float, nullable=True) # If we add DHT11 later
    timestamp = Column(DateTime, default=datetime.utcnow)

class PumpLog(Base):
    __tablename__ = 'pump_log'
    id = Column(Integer, primary_key=True)
    status = Column(String(10), nullable=False) # "ON" or "OFF"
    source = Column(String(50), nullable=True)  # "MANUAL", "AI_AUTO"
    timestamp = Column(DateTime, default=datetime.utcnow)
    
class AIInsights(Base):
    __tablename__ = 'ai_insights'
    id = Column(Integer, primary_key=True)
    reasoning = Column(String(255), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
