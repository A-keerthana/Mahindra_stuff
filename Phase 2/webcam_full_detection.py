# webcam_full_detection.py
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

import cv2
from common.object_detection import ObjectDetector
from common.video_utils import open_camera, close_windows

def full_webcam_detection():
    """
    Runs object detection on the full webcam feed.
    """
    cap = open_camera()
    detector = ObjectDetector()  # Initialize object detection model

    while True:
        ret, frame = cap.read()
        if ret:
            # Detect objects and annotate the frame
            results = detector.detect_objects(frame)
            annotated_frame = detector.annotate_frame(frame, results)

            # Display the annotated frame
            cv2.imshow('Full Webcam Detection', annotated_frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    close_windows()

# Call the function if running standalone
if __name__ == "__main__":
    full_webcam_detection()
