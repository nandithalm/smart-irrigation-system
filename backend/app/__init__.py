# Initialize Flask app
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from .config import Config

socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    socketio.init_app(app)

    # Register Blueprints
    from .api.sensor_endpoints import sensor_bp
    from .api.control_endpoints import control_bp
    from .api.webhook_endpoints import webhook_bp

    app.register_blueprint(sensor_bp, url_prefix='/api')
    app.register_blueprint(control_bp, url_prefix='/api')
    app.register_blueprint(webhook_bp, url_prefix='/api')

    return app
