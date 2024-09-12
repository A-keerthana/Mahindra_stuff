
import cv2
import numpy as np

# Open the default camera (webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    print("Webcam feed is active.")

def split_frame(frame, parts):
    # Split the frame into 'parts' vertical sections
    height, width, _ = frame.shape
    part_width = width // parts
    split_frames = [frame[:, i*part_width:(i+1)*part_width] for i in range(parts)]
    return split_frames

while True:
    ret, frame = cap.read()

    if ret:
        # Split the frame into 10 equal parts
        parts = split_frame(frame, 10)
        
        # Resize each part and combine them into a single feed
        resized_parts = [cv2.resize(part, (frame.shape[1] // 2, frame.shape[0] // 5)) for part in parts]
        central_feed = np.vstack(resized_parts)

        # Display the combined feed
        cv2.imshow('Split Webcam Feed', central_feed)
    else:
        print("Failed to retrieve frame from webcam.")
        break

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
