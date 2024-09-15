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
        Runs object detection on a frame and returns the filtered results (only people and cars).
        """
        # YOLOv8 model inference
        results = self.model(frame, conf=self.confidence_threshold)
        
        # Filter detections to include only people (class 0) and cars (class 2)
        filtered_results = results[0].boxes.cpu().numpy()
        people_and_cars = []
        
        for result in filtered_results:
            class_id = int(result.cls)  # Get the class ID
            if class_id == 0 or class_id == 2:  # Filter for people (0) and cars (2)
                people_and_cars.append(result)

        return people_and_cars

    def annotate_frame(self, frame, results):
        """
        Annotates the frame with bounding boxes and labels for people and cars from detection results.
        """
        for result in results:
            # Extract bounding box, class label, and confidence score
            x1, y1, x2, y2 = result[0], result[1], result[2], result[3]
            label = "Person" if int(result[5]) == 0 else "Car"
            confidence = result[4]

            # Annotate the frame with bounding boxes and labels
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        return frame




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
