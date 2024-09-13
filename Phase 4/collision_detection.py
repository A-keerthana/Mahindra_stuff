import numpy as np

def calculate_iou(box1, box2):
    """
    Calculate the Intersection over Union (IoU) of two bounding boxes.
    :param box1: bounding box in the format [x1, y1, x2, y2]
    :param box2: bounding box in the format [x1, y1, x2, y2]
    :return: IoU value.
    """
    x1_inter = max(box1[0], box2[0])
    y1_inter = max(box1[1], box2[1])
    x2_inter = min(box1[2], box2[2])
    y2_inter = min(box1[3], box2[3])

    inter_area = max(0, x2_inter - x1_inter) * max(0, y1_inter - y1_inter)
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])

    iou = inter_area / float(box1_area + box2_area - inter_area)
    return iou

def detect_collision(detected_boxes, iou_threshold=0.5):
    """
    Detect potential collisions by checking IoU between bounding boxes.
    :param detected_boxes: list of bounding boxes in the format [x1, y1, x2, y2]
    :param iou_threshold: IoU threshold for triggering a collision alert.
    """
    collision_detected = False
    for i in range(len(detected_boxes)):
        for j in range(i + 1, len(detected_boxes)):
            iou = calculate_iou(detected_boxes[i], detected_boxes[j])
            if iou > iou_threshold:
                print(f"Collision alert: Object {i} and Object {j} are too close! IoU = {iou:.2f}")
                collision_detected = True
    return collision_detected
