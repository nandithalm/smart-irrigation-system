import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.abspath(os.environ.get('DB_PATH', '../database/irrigation.db'))}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    MQTT_BROKER = os.environ.get('MQTT_BROKER', 'localhost')
    MQTT_PORT = int(os.environ.get('MQTT_PORT', 1883))
    MQTT_CLIENT_ID = os.environ.get('MQTT_CLIENT_ID', 'flask_backend')
    
    OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY')
    CITY = os.environ.get('CITY', 'San Francisco')
