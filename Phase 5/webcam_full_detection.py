import sys
import os

# Ensure the project root and common directory are included in the path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

import cv2
from flask_socketio import SocketIO
from common.Car_Speed_Tracking import SpeedTracker
from common.Angle_Calculation import calculate_angle
from common.Skid_Detection import detect_skid
from common.Stability_Tracking import StabilityTracker
from common.object_detection import ObjectDetector
from collision_detection import detect_collision
from parking_detection import ParkingDetector
from common.video_utils import close_windows
from app import emit_car_data  # Import from Flask app

# Initialize Flask SocketIO
socketio = SocketIO()

def full_webcam_detection():
    cap = cv2.VideoCapture(0)  # Use the webcam feed
    detector = ObjectDetector()
    speed_tracker = SpeedTracker()
    stability_tracker = StabilityTracker()
    parking_detector = ParkingDetector()

    # Set up the video writer to save the video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output_video.mp4', fourcc, 20.0, (640, 480))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect cars in the frame
        results = detector.detect_objects(frame)
        annotated_frame = detector.annotate_frame(frame, results)

        # Get bounding boxes (assuming results provide them in a list of [x1, y1, x2, y2])
        detected_boxes = results[0].boxes.xyxy.cpu().numpy()

        # Collision detection
        collision = detect_collision(detected_boxes)

        # Parking detection (example car positions)
        car_positions = [(100, 200), (300, 400)]  # Example positions (can extract from results if available)
        for car_id, car_pos in enumerate(car_positions):
            parking_detector.update_car_positions(car_id, car_pos)

        # Collect car data
        car_data = []
        for i, box in enumerate(detected_boxes):
            speed = speed_tracker.calculate_speed(i, car_pos, fps=20, conversion_factor=0.05)
            angle = calculate_angle((100, 150), (90, 180))  # Placeholder front and rear points
            stability = stability_tracker.track_stability(speed, angle, 0)  # Placeholder for previous angle
            car_data.append({'speed': speed, 'angle': angle, 'stability': stability})

        # Emit the car data to the Flask server in real-time
        emit_car_data(car_data)

        # Display the annotated frame
        cv2.imshow('Webcam Full Detection', annotated_frame)

        # Save the frame to the video file
        out.write(annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()  # Release the VideoWriter
    close_windows()

if __name__ == "__main__":
    full_webcam_detection()
