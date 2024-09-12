import time

class ParkingDetector:
    def __init__(self):
        self.parked_cars = {}  # Stores car positions and their last movement time

    def update_car_positions(self, car_id, current_position):
        import numpy as np
        """
        Update the position of the car and check if it's parked.
        car_id: Unique identifier for each detected car.
        current_position: Current (x, y) position of the car.
        """
        if car_id in self.parked_cars:
            prev_position, last_movement_time = self.parked_cars[car_id]

            # If the car's position hasn't changed, check if it's been stationary for too long
            if np.linalg.norm(np.array(current_position) - np.array(prev_position)) < 5:  # 5-pixel threshold
                if time.time() - last_movement_time > 10:  # 10 seconds of being stationary
                    print(f"Parking alert: Car {car_id} has been stationary for over 10 seconds.")
            else:
                # Car moved, reset the last movement time
                self.parked_cars[car_id] = (current_position, time.time())
        else:
            # Car is seen for the first time
            self.parked_cars[car_id] = (current_position, time.time())
