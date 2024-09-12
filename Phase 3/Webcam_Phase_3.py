# webcam_phase3.py
import cv2
from Car_Speed_Tracking import SpeedTracker
from Angle_Calculation import calculate_angle
from Skid_Detection import detect_skid
from Stability_Tracking import StabilityTracker
from common.object_detection import ObjectDetector
from common.video_utils import open_camera, close_windows

def process_webcam():
    cap = open_camera()
    detector = ObjectDetector()  # Initialize object detection model
    speed_tracker = SpeedTracker()
    stability_tracker = StabilityTracker()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect cars in the frame
        results = detector.detect_objects(frame)
        annotated_frame = detector.annotate_frame(frame, results)

        # Placeholder: Assuming we get car positions from object detection results
        # (You would integrate the actual object detection results here)
        car_positions = [(100, 200), (300, 400)]  # Example car positions

        # Process each car
        for car_id, car_pos in enumerate(car_positions):
            speed = speed_tracker.calculate_speed(car_id, car_pos, fps=30, conversion_factor=0.05)
            print(f"Car {car_id}: Speed = {speed} m/s")

            # Assuming you have front and rear points for angle calculation
            front_point, rear_point = (100, 150), (90, 180)
            angle = calculate_angle(front_point, rear_point)
            print(f"Car {car_id}: Angle = {angle} degrees")

            # Detect skid
            previous_angle = 0  # Placeholder
            skid = detect_skid(angle, previous_angle)
            print(f"Car {car_id}: Skid = {skid}")

            # Track stability
            stability_tracker.track_stability(speed, angle, previous_angle)

        # Display the annotated frame
        cv2.imshow('Webcam Phase 3', annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    close_windows()

if __name__ == "__main__":
    process_webcam()
