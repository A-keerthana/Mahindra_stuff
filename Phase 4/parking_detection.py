import time
import numpy as np

class ParkingDetector:
    def __init__(self):
        self.car_positions = {}  # Store car positions and last movement time

    def update_car_positions(self, car_id, current_position):
        """
        Updates the position of a car and checks if it's stationary for too long.
        :param car_id: Unique ID of the car.
        :param current_position: Current (x, y) position of the car.
        """
        if car_id in self.car_positions:
            prev_position, last_movement_time = self.car_positions[car_id]

            # If car hasn't moved much, check if it's been stationary for too long
            if np.linalg.norm(np.array(current_position) - np.array(prev_position)) < 5:  # 5-pixel threshold
                if time.time() - last_movement_time > 10:  # 10 seconds stationary
                    print(f"Parking alert: Car {car_id} has been stationary for over 10 seconds.")
            else:
                # Car has moved, update the last movement time
                self.car_positions[car_id] = (current_position, time.time())
        else:
            # First time seeing this car
            self.car_positions[car_id] = (current_position, time.time())
