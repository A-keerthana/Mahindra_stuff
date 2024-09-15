import cv2
import tkinter as tk
from tkinter import filedialog
from ultralytics import YOLO

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

def detect_and_annotate_video(video_path, output_path):
    # Load the YOLOv8 model
    model = YOLO("yolov8s.pt")  # Assuming you have yolov8s.pt in the working directory

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Get the original video frame width, height, and frames per second (fps)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Initialize the VideoWriter for saving the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use mp4 codec
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video.")
            break

        # Perform object detection
        results = model(frame)

        # Filter out only people (class 0) and cars (class 2)
        detections = results[0].boxes  # YOLOv8 output for bounding boxes
        for box in detections:
            class_id = int(box.cls[0])  # Class ID of the detected object
            if class_id == 0:  # Person
                label = "Person"
            elif class_id == 2:  # Car
                label = "Car"
            else:
                continue  # Skip other classes

            # Extract bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            confidence = box.conf[0]  # Confidence score

            # Draw the bounding box
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            # Put the label and confidence score on the frame
            cv2.putText(frame, f"{label} {confidence:.2f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Display the annotated frame
        cv2.imshow('YOLOv8 Detection - People and Cars', frame)

        # Write the annotated frame to the output video file
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()  # Release the VideoWriter
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Use Tkinter to choose the input video file and output file location
    video_path = choose_video_file()
    if video_path:
        output_path = get_output_video_filename()
        if output_path:
            detect_and_annotate_video(video_path, output_path)
