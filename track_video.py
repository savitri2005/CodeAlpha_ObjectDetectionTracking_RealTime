from ultralytics import YOLO
import cv2
import os
import glob

# Load YOLO11 model
model = YOLO("models/yolo11n.pt")

# Input and output folders
input_folder = "input_videos"
output_folder = "output/tracked_videos"

# Create output folder
os.makedirs(output_folder, exist_ok=True)

# Find all supported videos
video_paths = []

video_paths.extend(glob.glob(os.path.join(input_folder, "*.mp4")))
video_paths.extend(glob.glob(os.path.join(input_folder, "*.avi")))
video_paths.extend(glob.glob(os.path.join(input_folder, "*.mov")))
video_paths.extend(glob.glob(os.path.join(input_folder, "*.mkv")))

if not video_paths:
    print("No videos found in the input_videos folder.")
    exit()

print(f"Found {len(video_paths)} video(s).")

# Process every video
for input_video in video_paths:

    print(f"\nProcessing: {input_video}")

    # Open video
    cap = cv2.VideoCapture(input_video)

    if not cap.isOpened():
        print("Could not open this video.")
        continue

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    # Original filename
    filename = os.path.basename(input_video)

    # Output filename
    output_video = os.path.join(
        output_folder,
        "tracked_" + filename
    )

    # Video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    writer = cv2.VideoWriter(
        output_video,
        fourcc,
        fps,
        (width, height)
    )

    print("Object tracking started.")
    print("Press Q to stop this video.")

    while True:

        # Read frame
        ret, frame = cap.read()

        if not ret:
            break

        # YOLO11 + ByteTrack
        results = model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml"
        )

        # Draw boxes, labels and tracking IDs
        annotated_frame = results[0].plot()

        # Display tracking result
        cv2.imshow(
            "YOLO11 Object Detection and Tracking",
            annotated_frame
        )

        # Save frame
        writer.write(annotated_frame)

        # Press Q to stop current video
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    cap.release()
    writer.release()
    cv2.destroyAllWindows()

    print(f"Tracking completed: {output_video}")

print("\nAll videos tracked successfully!")