import cv2
import numpy as np

class SpeedTracker:
    def __init__(self):
        self.prev_positions = {}  # Stores previous positions of cars

    def calculate_speed(self, car_id, current_position, fps, conversion_factor):
        """
        Calculate speed of the car between frames.
        car_id: Unique identifier for each detected car.
        current_position: Current (x, y) position of the car.
        fps: Frames per second of the camera feed.
        conversion_factor: Conversion from pixels to real-world units (e.g., meters).
        """
        if car_id in self.prev_positions:
            prev_position = self.prev_positions[car_id]
            # Calculate pixel distance between current and previous positions
            pixel_distance = np.linalg.norm(np.array(current_position) - np.array(prev_position))
            
            # Speed in pixels per frame
            speed_in_pixels = pixel_distance / fps
            
            # Convert to real-world speed (e.g., meters/second)
            speed_in_mps = speed_in_pixels * conversion_factor
            
            # Update the previous position
            self.prev_positions[car_id] = current_position
            
            return speed_in_mps
        else:
            # Store the current position as the first position
            self.prev_positions[car_id] = current_position
            return 0  # No speed calculated for the first frame
