# utils.py
import cv2
import numpy as np

def open_camera(camera_index=0):
    """
    Opens the webcam feed and returns the VideoCapture object.
    """
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise Exception("Error: Could not open webcam.")
    return cap

def split_frame(frame, rows, cols):
    """
    Splits a frame into equal parts based on the number of rows and columns.
    """
    height, width, _ = frame.shape
    part_height = height // rows
    part_width = width // cols
    split_frames = []

    for i in range(rows):
        for j in range(cols):
            split_frame = frame[i * part_height:(i + 1) * part_height, j * part_width:(j + 1) * part_width]
            split_frames.append(split_frame)

    return split_frames

def display_split_feed(parts, rows, cols, window_name="Split Feed"):
    """
    Displays the split feed in a grid layout.
    """
    resized_parts = [cv2.resize(part, (parts[0].shape[1], parts[0].shape[0])) for part in parts]
    row_frames = [np.hstack(resized_parts[i * cols:(i + 1) * cols]) for i in range(rows)]
    grid_feed = np.vstack(row_frames)
    cv2.imshow(window_name, grid_feed)

def close_windows():
    """
    Releases OpenCV windows and closes them.
    """
    cv2.destroyAllWindows()
