import cv2
import tkinter as tk
from tkinter import filedialog, simpledialog
from Car_Speed_Tracking import SpeedTracker
from Angle_Calculation import calculate_angle
from Skid_Detection import detect_skid
from Stability_Tracking import StabilityTracker
from object_detection import ObjectDetector
from video_utils import close_windows

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
    detector = ObjectDetector()  # Initialize object detection model to detect only people and cars
    speed_tracker = SpeedTracker()
    stability_tracker = StabilityTracker()

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

        # Detect people and cars in the frame
        results = detector.detect_objects(frame)
        annotated_frame = detector.annotate_frame(frame, results)

        # Extract car and person positions from detection results
        car_positions = []
        for result in results:
            # Assuming each result contains the bounding box as [x1, y1, x2, y2]
            x1, y1, x2, y2 = result.xyxy
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)
            car_positions.append((center_x, center_y))

        # Process each detected person or car
        for car_id, car_pos in enumerate(car_positions):
            speed = speed_tracker.calculate_speed(car_id, car_pos, fps=fps, conversion_factor=0.05)
            print(f"Car {car_id}: Speed = {speed} m/s")

            # Assuming you have front and rear points for angle calculation (these would be specific to the car/person detected)
            front_point, rear_point = (car_pos[0] + 10, car_pos[1]), (car_pos[0] - 10, car_pos[1])
            angle = calculate_angle(front_point, rear_point)
            print(f"Car {car_id}: Angle = {angle} degrees")

            # Detect skid
            previous_angle = 0  # Placeholder for previous angle (could be tracked over time)
            skid = detect_skid(angle, previous_angle)
            print(f"Car {car_id}: Skid = {skid}")

            # Track stability
            stability_tracker.track_stability(speed, angle, previous_angle)

        # Display the annotated frame
        cv2.imshow('Video Phase 3', annotated_frame)

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
