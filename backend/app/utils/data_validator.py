def validate_sensor_data(data):
    if not isinstance(data, dict):
        return False, "Data must be JSON object"
    if 'moisture' not in data:
        return False, "Missing 'moisture' field"
    try:
        float(data['moisture'])
    except ValueError:
        return False, "'moisture' must be a number"
        
    return True, ""
