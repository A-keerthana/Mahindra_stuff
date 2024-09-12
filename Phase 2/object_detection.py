# object_detection.py
import torch
import cv2

class ObjectDetector:
    def __init__(self, model_path="yolov5s.pt", confidence_threshold=0.4):
        """
        Initializes the object detection model.
        """
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
        self.model.conf = confidence_threshold  # Confidence threshold

    def detect_objects(self, frame):
        """
        Runs object detection on a frame and returns the results.
        """
        results = self.model(frame)
        return results

    def annotate_frame(self, frame, results):
        """
        Annotates the frame with bounding boxes and labels from detection results.
        """
        annotated_frame = results.render()[0]
        return annotated_frame
