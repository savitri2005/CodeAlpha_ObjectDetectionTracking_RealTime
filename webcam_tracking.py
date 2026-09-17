from ultralytics import YOLO
import cv2

# Load YOLO11 model
model = YOLO("models/yolo11n.pt")

# Open laptop webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

print("Real-time webcam detection and tracking started.")
print("Confidence threshold: 50%")
print("Press Q to quit.")

while True:

    # Read webcam frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read webcam frame.")
        break

    # YOLO11 detection + ByteTrack tracking
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        conf=0.50
    )

    # Draw bounding boxes, labels and tracking IDs
    annotated_frame = results[0].plot()

    # Display webcam output
    cv2.imshow(
        "Real-Time Object Detection and Tracking",
        annotated_frame
    )

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release webcam
cap.release()
cv2.destroyAllWindows()

print("Webcam tracking stopped.")