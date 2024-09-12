# webcam_full_detection.py
import cv2
from object_detection import ObjectDetector
from video_utils import open_camera, close_windows

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
