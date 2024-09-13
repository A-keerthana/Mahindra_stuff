from Skid_Detection import detect_skid

class StabilityTracker:
    def __init__(self):
        self.skid_detected = False
        self.speed = 0

    def track_stability(self, current_speed, current_angle, previous_angle):
        """
        Track the car's stability based on speed and angle changes.
        current_speed: The car's current speed.
        current_angle: The car's current orientation angle.
        previous_angle: The car's previous orientation angle.
        """
        self.speed = current_speed
        self.skid_detected = detect_skid(current_angle, previous_angle)

        if self.skid_detected:
            print("Warning: Car stability compromised (skid detected).")
        elif current_speed > 50:  # Assuming 50 m/s is a high speed threshold
            print("Warning: High-speed cornering, check stability.")
