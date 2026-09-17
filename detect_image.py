from ultralytics import YOLO
import cv2
import os
import glob

# Load the pretrained YOLO11 model
model = YOLO("models/yolo11n.pt")

# Input and output folders
input_folder = "input_images"
output_folder = "output/detected_images"

# Create output folder
os.makedirs(output_folder, exist_ok=True)

# Find all supported images
image_paths = []

image_paths.extend(glob.glob(os.path.join(input_folder, "*.jpg")))
image_paths.extend(glob.glob(os.path.join(input_folder, "*.jpeg")))
image_paths.extend(glob.glob(os.path.join(input_folder, "*.png")))

if not image_paths:
    print("No images found in the input_images folder.")
    exit()

print(f"Found {len(image_paths)} image(s).")

# Process every image
for image_path in image_paths:

    print(f"\nProcessing: {image_path}")

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Could not read this image.")
        continue

    # Run YOLO detection
    results = model(image)

    # Draw bounding boxes, labels and confidence
    annotated_image = results[0].plot()

    # Get filename
    filename = os.path.basename(image_path)

    # Output path
    output_path = os.path.join(output_folder, filename)

    # Save result
    cv2.imwrite(output_path, annotated_image)

    print(f"Detected image saved to: {output_path}")

    # Display result
    cv2.imshow("YOLO11 Object Detection", annotated_image)

    # Press any key to move to the next image
    cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()

print("\nAll images processed successfully!")