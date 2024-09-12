def detect_skid(current_angle, previous_angle, threshold=15):
    """
    Detects if the car is skidding based on the change in angle.
    current_angle: The current orientation angle of the car.
    previous_angle: The previous orientation angle of the car.
    threshold: The angle change threshold to classify a skid.
    """
    angle_change = abs(current_angle - previous_angle)
    
    if angle_change > threshold:
        return True  # Skid detected
    return False  # No skid
