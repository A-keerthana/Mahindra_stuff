# Replace the camera_urls with the actual RTSP URLs of your IP cameras.

import cv2



# Define RTSP URLs of your cameras
camera_urls = [
    "rtsp://username:password@camera1_ip_address/stream",
    "rtsp://username:password@camera2_ip_address/stream",
]

# Open each camera feed using OpenCV's VideoCapture
camera_feeds = [cv2.VideoCapture(url) for url in camera_urls]

def display_feeds(camera_feeds):
    while True:
        for idx, cap in enumerate(camera_feeds):
            ret, frame = cap.read()
            if ret:
                # Show the feed in a window for each camera
                cv2.imshow(f'Camera {idx+1}', frame)
            else:
                print(f"Failed to get feed from Camera {idx+1}")

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release all camera feeds
    for cap in camera_feeds:
        cap.release()

    cv2.destroyAllWindows()

# Call the function to display the feeds
display_feeds(camera_feeds)
