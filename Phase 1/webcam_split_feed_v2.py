import cv2
import numpy as np

# Open the default camera (webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    print("Webcam feed is active.")

def split_frame(frame, rows, cols):
    # Split the frame into equal parts (rows x cols grid)
    height, width, _ = frame.shape
    part_height = height // rows
    part_width = width // cols
    split_frames = []

    # Slice the frame into parts based on rows and columns
    for i in range(rows):
        for j in range(cols):
            split_frame = frame[i * part_height:(i + 1) * part_height, j * part_width:(j + 1) * part_width]
            split_frames.append(split_frame)

    return split_frames

while True:
    ret, frame = cap.read()

    if ret:
        # Split the frame into a 2x5 grid (10 parts)
        parts = split_frame(frame, 2, 5)

        # Display each part in a separate window
        for idx, part in enumerate(parts):
            window_name = f'Part {idx + 1}'
            cv2.imshow(window_name, part)

    else:
        print("Failed to retrieve frame from webcam.")
        break

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
