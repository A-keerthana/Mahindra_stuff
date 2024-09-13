import cv2
from flask_socketio import SocketIO
from object_detection import ObjectDetector
from parking_detection import ParkingDetector
from collision_detection import detect_collision
from app import emit_car_data  # Import from the Flask app

# Initialize Flask SocketIO
socketio = SocketIO()

def full_webcam_detection():
    cap = cv2.VideoCapture(0)  # Use webcam feed
    detector = ObjectDetector()
    parking_detector = ParkingDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect cars in the frame
        results = detector.detect_objects(frame)
        detected_boxes = results[0].boxes.xyxy.cpu().numpy()

        # Collect car data
        car_data = []
        for i, box in enumerate(detected_boxes):
            speed = ...  # Calculate speed (placeholder)
            angle = ...  # Calculate angle (placeholder)
            stability = ...  # Check stability (placeholder)
            car_data.append({'speed': speed, 'angle': angle, 'stability': stability})

        # Emit the car data to the Flask server
        emit_car_data(car_data)

        # Display the frame (optional)
        cv2.imshow('Webcam Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
