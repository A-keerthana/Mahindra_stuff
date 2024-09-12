# webcam_split_detection.py
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

import cv2
from common.object_detection import ObjectDetector
from common.video_utils import open_camera, split_frame, close_windows

def split_webcam_detection():
    """
    Runs object detection on split webcam feed (2x5 grid) and displays each part in its own window.
    """
    cap = open_camera()
    detector = ObjectDetector()  # Initialize object detection model

    while True:
        ret, frame = cap.read()
        if ret:
            # Split the frame into 10 parts (2x5 grid)
            parts = split_frame(frame, 2, 5)
            
            # Run object detection on each part separately and display each in its own window
            for idx, part in enumerate(parts):
                # Detect objects and annotate each part
                results = detector.detect_objects(part)
                annotated_part = detector.annotate_frame(part, results)

                # Display each annotated part in its own window
                window_name = f'Part {idx + 1}'
                cv2.imshow(window_name, annotated_part)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    close_windows()

# Call the function if running standalone
if __name__ == "__main__":
    split_webcam_detection()
