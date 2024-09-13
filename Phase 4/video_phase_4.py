import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)


import cv2
import tkinter as tk
from tkinter import filedialog
from common.Car_Speed_Tracking import SpeedTracker
from common.Angle_Calculation import calculate_angle
from common.Skid_Detection import detect_skid
from common.Stability_Tracking import StabilityTracker
from common.object_detection import ObjectDetector
from collision_detection import detect_collision
from parking_detection import ParkingDetector
from common.video_utils import close_windows

def choose_video_file():
    """
    Opens a file dialog to choose a video file.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mov")])
    return video_path

def get_output_video_filename():
    """
    Opens a dialog to let the user specify the name and location of the output video.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    output_file = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4"), ("AVI files", "*.avi")])
    return output_file

def process_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    detector = ObjectDetector()  # Initialize object detection model
    speed_tracker = SpeedTracker()
    stability_tracker = StabilityTracker()
    parking_detector = ParkingDetector()

    # Get the original video frame width, height, and frames per second (fps)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Initialize the VideoWriter for saving the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use mp4 codec
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
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
        car_positions = [(100, 200), (300, 400)]  # Example positions (can extract from results if available)
        for car_id, car_pos in enumerate(car_positions):
            parking_detector.update_car_positions(car_id, car_pos)

        # Display the annotated frame
        cv2.imshow('Video Phase 4', annotated_frame)

        # Write the annotated frame to the output video file
        out.write(annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()  # Release the VideoWriter
    close_windows()

if __name__ == "__main__":
    video_path = choose_video_file()
    if video_path:
        output_path = get_output_video_filename()
        if output_path:
            process_video(video_path, output_path)
