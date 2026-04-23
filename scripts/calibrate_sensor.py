def calibrate(dry_val, wet_val, current_val):
    """
    Map sensor reading from analog range (e.g. 0-1024) to a percentage (0-100%).
    """
    if current_val > dry_val:
        current_val = dry_val
    if current_val < wet_val:
        current_val = wet_val
        
    percentage = ((dry_val - current_val) / (dry_val - wet_val)) * 100
    return round(percentage, 2)

if __name__ == "__main__":
    dry = 800
    wet = 300
    current = int(input("Enter current sensor reading: "))
    print(f"Moisture Percentage: {calibrate(dry, wet, current)}%")
