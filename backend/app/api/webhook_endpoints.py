from flask import request, jsonify
from . import webhook_bp

@webhook_bp.route('/webhook', methods=['POST'])
def general_webhook():
    """Endpoint for third-party integrations (e.g., IFTTT, external alerts)"""
    data = request.json
    print(f"Received webhook payload: {data}")
    return jsonify({"status": "acknowledged"}), 200
