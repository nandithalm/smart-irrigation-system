import eventlet
eventlet.monkey_patch()

import os
from app import create_app, socketio
from app.mqtt_bridge.mqtt_subscriber import start_mqtt
from app.database.models import init_db

app = create_app()

@app.before_first_request
def initialize_system():
    # Initialize Database
    init_db(app)
    
    # Start MQTT Subscriber in background
    start_mqtt(app)

if __name__ == '__main__':
    print("Starting Smart Irrigation Backend...")
    # Initialize DB schema outside of request context if running standalone
    init_db(app)
    start_mqtt(app)
    
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=False)
