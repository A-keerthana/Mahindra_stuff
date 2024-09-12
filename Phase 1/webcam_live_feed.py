
import cv2

# Open the default camera (webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    print("Webcam feed is active.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Display the frame
        cv2.putText(frame, 'Webcam Feed Active', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Webcam Feed', frame)
    else:
        print("Failed to retrieve frame from webcam.")
        break

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
