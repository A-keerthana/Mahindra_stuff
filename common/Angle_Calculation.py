def calculate_angle(front_point, rear_point):
    import numpy as np
    """
    Calculate the angle of the car's orientation based on the front and rear points.
    front_point: (x, y) coordinates of the front of the car.
    rear_point: (x, y) coordinates of the rear of the car.
    Returns the angle in degrees.
    """
    delta_x = front_point[0] - rear_point[0]
    delta_y = front_point[1] - rear_point[1]
    
    # Calculate the angle in radians and convert to degrees
    angle = np.arctan2(delta_y, delta_x) * (180.0 / np.pi)
    
    return angle
