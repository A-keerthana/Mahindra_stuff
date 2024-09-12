"""
V8 code
"""
from ultralytics import YOLO
import cv2

class ObjectDetector:
    def __init__(self, model_path="yolov8s.pt", confidence_threshold=0.4):
        """
        Initializes the YOLOv8 model for object detection.
        """
        # Load the YOLOv8 model (use a local path or download from Ultralytics)
        self.model = YOLO(model_path)
        self.confidence_threshold = confidence_threshold

    def detect_objects(self, frame):
        """
        Runs object detection on a frame and returns the results.
        """
        # YOLOv8 model inference
        results = self.model(frame, conf=self.confidence_threshold)
        return results

    def annotate_frame(self, frame, results):
        """
        Annotates the frame with bounding boxes and labels from detection results.
        """
        annotated_frame = results[0].plot()  # Plot the results directly onto the frame
        return annotated_frame




'''
V5 code
'''
# # object_detection.py
# import torch
# import cv2

# class ObjectDetector:
#     def __init__(self, model_path="yolov5s.pt", confidence_threshold=0.4):
#         """
#         Initializes the object detection model.
#         """
#         self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
#         self.model.conf = confidence_threshold  # Confidence threshold

#     def detect_objects(self, frame):
#         """
#         Runs object detection on a frame and returns the results.
#         """
#         results = self.model(frame)
#         return results

#     def annotate_frame(self, frame, results):
#         """
#         Annotates the frame with bounding boxes and labels from detection results.
#         """
#         annotated_frame = results.render()[0]
#         return annotated_frame
