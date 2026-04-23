from flask import Blueprint

sensor_bp = Blueprint('sensor_bp', __name__)
control_bp = Blueprint('control_bp', __name__)
webhook_bp = Blueprint('webhook_bp', __name__)

from . import sensor_endpoints, control_endpoints, webhook_endpoints
