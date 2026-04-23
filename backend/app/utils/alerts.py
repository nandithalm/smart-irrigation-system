def send_alert(message: str, level: str = "warning"):
    """
    Mock function to send an alert. 
    In reality, could use Twilio, SendGrid, Pushbullet, etc.
    """
    print(f"[{level.upper()} ALERT]: {message}")
    # Integration logic goes here
