import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

import cv2
from common.object_detection import ObjectDetector
from common.video_utils import open_camera, close_windows
from collision_detection import detect_collision
from parking_detection import ParkingDetector

def full_webcam_detection():
    cap = open_camera()
    detector = ObjectDetector()  # Initialize object detection model
    parking_detector = ParkingDetector()

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

        # Parking detection (placeholder car positions)
        car_positions = [(100, 200), (300, 400)]  # Example positions
        for car_id, car_pos in enumerate(car_positions):
            parking_detector.update_car_positions(car_id, car_pos)

        # Display the annotated frame
        cv2.imshow('Webcam Full Detection', annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    close_windows()

if __name__ == "__main__":
    full_webcam_detection()
