# CodeAlpha Object Detection and Tracking

## 📌 Project Overview

This project is developed as part of the **CodeAlpha Internship – Object Detection and Tracking Task**.

The project implements:

* Object detection in images
* Object detection in videos
* Object tracking in videos
* Real-time object detection and tracking using a laptop webcam
* Tracking of detected objects using **ByteTrack**
* Confidence-based detection using a configurable confidence threshold

The project uses the **YOLO11n pretrained model** from Ultralytics for object detection and **OpenCV** for image, video, and webcam processing.

---

## 🎯 Objectives

The main objectives of this project are:

1. Detect objects in images using YOLO11.
2. Detect objects frame-by-frame in videos.
3. Track detected objects across consecutive video frames.
4. Assign tracking IDs to detected objects.
5. Process multiple images automatically.
6. Process multiple videos automatically.
7. Perform real-time object detection and tracking using a webcam.
8. Save processed detection and tracking results.
9. Understand the practical workflow of computer vision-based object detection and tracking.

---

# 🧠 Technologies Used

| Technology  | Purpose                             |
| ----------- | ----------------------------------- |
| Python      | Main programming language           |
| YOLO11n     | Object detection                    |
| Ultralytics | YOLO11 model and tracking interface |
| ByteTrack   | Multi-object tracking               |
| OpenCV      | Image, video and webcam processing  |
| Git         | Version control                     |
| GitHub      | Source code repository              |

---

# 🤖 YOLO11

**YOLO** stands for **You Only Look Once**.

YOLO is a real-time object detection algorithm that can identify objects in an image or video frame and determine their locations using bounding boxes.

This project uses:

**YOLO11n**

The `n` represents the **nano** version of the YOLO11 model.

YOLO11n is a relatively lightweight pretrained model suitable for experimentation and real-time computer vision applications.

The model can detect objects from the classes included in its pretrained dataset.

Examples of objects that can be detected include:

* Person
* Car
* Bicycle
* Dog
* Cat
* Elephant
* Giraffe
* Zebra
* Truck
* Backpack
* And other supported object classes

The pretrained model is used directly in this project; the model is **not trained from scratch**.

---

# 🎯 Object Detection

Object detection identifies:

1. **What object is present**
2. **Where the object is located**
3. **How confident the model is about the detection**

For example, a detection may contain information such as:

```text
person 0.92
```

This means:

* `person` → detected object class
* `0.92` → model confidence of approximately 92%

The result is displayed using a bounding box around the detected object.

---

# 🔄 Object Tracking

Object detection identifies objects independently in each frame.

Object tracking goes one step further.

Tracking attempts to maintain the identity of an object across consecutive video frames.

For example:

```text
Frame 1 → Person → ID 1
Frame 2 → Person → ID 1
Frame 3 → Person → ID 1
```

The tracking ID helps distinguish different detected objects while they are being tracked.

---

# 🚀 ByteTrack

This project uses **ByteTrack** through the Ultralytics tracking interface.

ByteTrack is a multi-object tracking algorithm that associates detections across consecutive video frames.

The tracking process can be summarized as:

```text
Video Frame
     ↓
YOLO11 Object Detection
     ↓
Detected Bounding Boxes
     ↓
ByteTrack
     ↓
Object Association
     ↓
Tracking IDs
     ↓
Annotated Video
```

### Important

This project uses **ByteTrack**.

It does **not** use Deep SORT.

---

# 📁 Project Structure

```text
CodeAlpha_ObjectDetectionTracking_RealTime/
│
├── input_images/
│   ├── animals.jpg
│   ├── cars.jpg
│   ├── people.jpg
│   └── test.jpg
│
├── input_videos/
│   ├── cars.mp4
│   ├── peoples.mp4
│   ├── street.mp4
│   └── traffic.mp4
│
├── models/
│   └── yolo11n.pt
│
├── output/
│   ├── detected_images/
│   ├── detected_videos/
│   └── tracked_videos/
│
├── venv/
│
├── test_yolo.py
├── detect_image.py
├── detect_video.py
├── track_video.py
├── webcam_tracking.py
├── requirements.txt
├── .gitignore
└── README.md
```

### GitHub Note

The following items are intentionally excluded from GitHub using `.gitignore`:

```text
venv/
models/*.pt
output/
__pycache__/
*.pyc
```

Therefore, the `yolo11n.pt` model file and generated output files are not stored in the GitHub repository.

---

# 💻 System Requirements

Recommended environment:

* Windows 10/11
* Python 3.11
* Webcam for real-time testing
* Internet connection for installing Python packages and downloading the pretrained model
* Sufficient disk space for Python packages and model files

A dedicated NVIDIA GPU is **not required** for this project.

The project can run using the CPU, although processing speed depends on the computer hardware and video resolution.

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

Clone the GitHub repository:

```powershell
git clone https://github.com/savitri2005/CodeAlpha_ObjectDetectionTracking_RealTime.git
```

Move into the project folder:

```powershell
cd CodeAlpha_ObjectDetectionTracking_RealTime
```

---

## 2. Create a Virtual Environment

Create a Python virtual environment:

```powershell
python -m venv venv
```

---

## 3. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

After activation, the terminal should show something similar to:

```text
(venv) PS C:\...\CodeAlpha_ObjectDetectionTracking_RealTime>
```

---

## 4. Install Required Libraries

Install the required Python packages:

```powershell
pip install -r requirements.txt
```

The project requires:

```text
ultralytics
opencv-python
```

---

# 📦 Download the YOLO11 Model

The pretrained YOLO11n model is intentionally excluded from GitHub because model files are ignored by `.gitignore`.

After cloning the repository, make sure the `models` folder exists:

```powershell
mkdir models
```

Download the YOLO11n model using Ultralytics:

```powershell
python -c "from ultralytics import YOLO; YOLO('yolo11n.pt')"
```

After the download completes, move the model into the project's `models` folder:

```powershell
Move-Item yolo11n.pt models\yolo11n.pt
```

The expected location is:

```text
models/yolo11n.pt
```

---

# 🧪 Testing the YOLO11 Model

The project contains:

```text
test_yolo.py
```

This file verifies that the YOLO11 model can be loaded successfully.

Run:

```powershell
python test_yolo.py
```

Expected output:

```text
YOLO11 model loaded successfully!
```

---

# 🖼️ Image Object Detection

The file:

```text
detect_image.py
```

performs object detection on all supported images inside:

```text
input_images/
```

Supported image formats:

```text
.jpg
.jpeg
.png
```

The program automatically searches for all supported images and processes them one by one.

---

## ▶️ Run Image Detection

Run:

```powershell
python detect_image.py
```

The program:

1. Loads YOLO11n.
2. Searches the `input_images` folder.
3. Reads each image.
4. Performs object detection.
5. Draws bounding boxes and labels.
6. Displays the result.
7. Saves the detected image.

Output location:

```text
output/detected_images/
```

---

# 🖼️ Image Testing Performed

The project was tested using the following images:

```text
animals.jpg
cars.jpg
people.jpg
test.jpg
```

Example detections observed during testing included:

### animals.jpg

Detected examples:

* Elephant
* Zebra
* Giraffe

### cars.jpg

Detected examples:

* Person
* Cars
* Trucks

### people.jpg

Detected examples:

* Persons
* Bicycles
* Cars
* Truck

### test.jpg

Detected examples:

* Person
* Bicycle
* Car
* Dog
* Backpack

Detection results are saved in:

```text
output/detected_images/
```

---

# 🎥 Video Object Detection

The file:

```text
detect_video.py
```

performs object detection on videos.

The program automatically searches the:

```text
input_videos/
```

folder.

Supported video formats:

```text
.mp4
.avi
.mov
.mkv
```

---

## ▶️ Run Video Detection

Run:

```powershell
python detect_video.py
```

The program:

1. Searches for videos.
2. Opens each video.
3. Reads the video frame-by-frame.
4. Runs YOLO11 object detection on each frame.
5. Draws bounding boxes and labels.
6. Displays the processed video.
7. Saves the detected video.
8. Moves to the next video.

Press:

```text
Q
```

to stop processing the current video.

---

# 🎥 Multiple Video Processing

The project supports processing multiple videos automatically.

The current input videos are:

```text
cars.mp4
peoples.mp4
street.mp4
traffic.mp4
```

The detected videos are saved inside:

```text
output/detected_videos/
```

Output files are created using the prefix:

```text
detected_
```

For example:

```text
detected_cars.mp4
detected_peoples.mp4
detected_street.mp4
detected_traffic.mp4
```

---

# 🚗 Object Tracking in Videos

The file:

```text
track_video.py
```

performs object detection and tracking.

It uses:

```text
YOLO11n + ByteTrack
```

The tracking process maintains object identities across video frames whenever the tracker can associate the detections.

---

## ▶️ Run Video Tracking

Run:

```powershell
python track_video.py
```

The program:

1. Opens each input video.
2. Reads frames continuously.
3. Performs YOLO11 object detection.
4. Passes detections to ByteTrack.
5. Associates objects across frames.
6. Assigns tracking IDs.
7. Draws bounding boxes, labels and IDs.
8. Displays the tracking result.
9. Saves the processed video.

Press:

```text
Q
```

to stop processing the current video.

---

# 🆔 Understanding Tracking Labels

A tracking result may display information similar to:

```text
person 1 0.92
```

These values represent different things:

```text
person → Object class
1      → Tracking ID
0.92   → Detection confidence
```

### Object Class

The object class tells what the model believes the object is.

### Tracking ID

The tracking ID identifies an object being tracked across frames.

### Confidence

The confidence value indicates the model's confidence in its detected class.

These three values should not be confused with each other.

---

# 📹 Tracking Output

Tracked videos are saved in:

```text
output/tracked_videos/
```

The output filename uses:

```text
tracked_
```

For example:

```text
tracked_cars.mp4
tracked_peoples.mp4
tracked_street.mp4
tracked_traffic.mp4
```

---

# 📷 Real-Time Webcam Object Detection and Tracking

The file:

```text
webcam_tracking.py
```

provides real-time object detection and tracking using the laptop webcam.

The webcam is accessed using:

```python
cv2.VideoCapture(0)
```

The processing pipeline is:

```text
Laptop Webcam
      ↓
OpenCV
      ↓
Video Frame
      ↓
YOLO11 Object Detection
      ↓
ByteTrack
      ↓
Tracking IDs
      ↓
Bounding Boxes + Labels
      ↓
Live Display
```

---

# ▶️ Run Real-Time Webcam Tracking

Make sure your webcam is available.

Run:

```powershell
python webcam_tracking.py
```

The webcam window will open.

The application performs:

* Real-time object detection
* Object tracking
* Bounding-box drawing
* Class labeling
* Tracking ID assignment
* Confidence filtering

Press:

```text
Q
```

to stop the webcam application.

---

# 🎚️ Confidence Threshold

The webcam tracking implementation uses:

```python
conf=0.50
```

This means detections below the configured confidence threshold are filtered out by the detection/tracking pipeline.

The current threshold is:

```text
50%
```

A confidence threshold can reduce low-confidence detections, but it does **not guarantee that every object will be classified correctly**.

---

# ⚠️ Object Detection Accuracy

This project uses a pretrained general-purpose YOLO11n model.

Because the model is not specifically trained on the user's own objects or environment, incorrect classifications can sometimes occur.

For example, an object may occasionally be assigned an incorrect class.

This can happen because of factors such as:

* Object appearance
* Lighting conditions
* Camera angle
* Object size
* Background
* Occlusion
* Similar-looking objects
* Training data limitations
* Model size

Therefore, the output of a pretrained object detector should be interpreted as a model prediction rather than a guaranteed identification.

---

# 🔄 Tracking Limitations

Tracking IDs are generated by the tracking algorithm and may change in some situations.

For example, an ID can change when:

* An object becomes temporarily hidden.
* Objects overlap.
* An object leaves the frame and later returns.
* The detector temporarily fails to detect the object.
* The object moves quickly.
* Lighting or image quality changes.

Therefore, a tracking ID represents the track maintained by the tracker rather than a permanent real-world identity.

---

# 📊 Project Workflow

The complete workflow of this project is:

```text
                 Input
                   │
        ┌──────────┼──────────┐
        │          │          │
      Images     Videos     Webcam
        │          │          │
        ↓          ↓          ↓
     YOLO11     YOLO11      YOLO11
        │          │          │
        ↓          ↓          ↓
    Detection   Detection   Detection
                   │          │
                   ↓          ↓
               ByteTrack   ByteTrack
                   │          │
                   ↓          ↓
                Tracking    Tracking
                   │          │
                   └────┬─────┘
                        ↓
                 Annotated Output
```

---

# 📂 Output Structure

The program creates output folders automatically.

```text
output/
│
├── detected_images/
│
├── detected_videos/
│
└── tracked_videos/
```

### Detected Images

Stored in:

```text
output/detected_images/
```

### Detected Videos

Stored in:

```text
output/detected_videos/
```

### Tracked Videos

Stored in:

```text
output/tracked_videos/
```

---

# 📝 Python Files

## `test_yolo.py`

Checks whether the YOLO11n model can be loaded successfully.

---

## `detect_image.py`

Performs object detection on all supported images in the `input_images` folder.

---

## `detect_video.py`

Performs object detection on all supported videos in the `input_videos` folder.

---

## `track_video.py`

Performs object detection and multi-object tracking on all supported videos using YOLO11n and ByteTrack.

---

## `webcam_tracking.py`

Performs real-time object detection and tracking using the laptop webcam.

---

# 📋 requirements.txt

The project uses the following main dependencies:

```text
ultralytics
opencv-python
```

Install them using:

```powershell
pip install -r requirements.txt
```

---

# 🚫 .gitignore

The `.gitignore` file prevents unnecessary or large files from being uploaded to GitHub.

Current ignored items include:

```text
venv/
__pycache__/
*.pyc
models/*.pt
output/
*.tmp
*.log
```

This keeps the GitHub repository smaller and avoids uploading the virtual environment, model weights and generated output files.

---

# 🔧 Complete Execution Guide

After cloning and installing the project, use the following sequence.

### Step 1 — Activate environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 2 — Verify the model

```powershell
python test_yolo.py
```

### Step 3 — Run image detection

```powershell
python detect_image.py
```

### Step 4 — Run video detection

```powershell
python detect_video.py
```

### Step 5 — Run video tracking

```powershell
python track_video.py
```

### Step 6 — Run real-time webcam tracking

```powershell
python webcam_tracking.py
```

Press `Q` when you want to stop the active video or webcam window.

---

# 🧪 Testing Performed

The project was tested using:

### Images

```text
animals.jpg
cars.jpg
people.jpg
test.jpg
```

### Videos

```text
cars.mp4
peoples.mp4
street.mp4
traffic.mp4
```

### Webcam

The real-time tracking application was tested using the laptop webcam.

The webcam application successfully performed real-time inference and displayed detection and tracking results.

---

# ⚡ Performance

The project was tested on a Windows laptop using CPU-based processing.

Example YOLO11 inference output during webcam testing was approximately:

```text
Preprocess: 1.8 ms
Inference: 72.9 ms
Postprocess: 2.0 ms
```

Actual performance can vary depending on:

* CPU
* RAM
* Video resolution
* Number of detected objects
* Lighting
* Input image size
* Background complexity

---

# ✅ Advantages

* Uses a pretrained YOLO11 model.
* Supports image object detection.
* Supports multiple video files.
* Supports multi-object tracking.
* Uses ByteTrack for tracking.
* Supports real-time webcam processing.
* Automatically creates output folders.
* Uses a simple Python-based implementation.
* Can be extended for more advanced computer vision applications.

---

# ⚠️ Limitations

* The pretrained YOLO11n model may occasionally misclassify objects.
* Detection accuracy depends on the pretrained model and input conditions.
* Tracking IDs are not guaranteed to remain permanent.
* CPU processing can be slower than GPU processing.
* The project does not train a custom object detection model.
* The project is intended as an internship-level computer vision implementation rather than a production surveillance system.
* Real-time performance depends on the computer hardware and camera resolution.

---

# 🚀 Future Improvements

Possible future improvements include:

* Training a custom YOLO model on a domain-specific dataset.
* Using a more powerful YOLO model when hardware permits.
* Improving detection accuracy for specific objects.
* Adding a graphical user interface.
* Adding object counting.
* Adding line-crossing detection.
* Adding region-of-interest detection.
* Adding real-time statistics.
* Adding detection logs.
* Adding configurable confidence thresholds.
* Adding support for additional camera sources.
* Deploying the system as a web application.

---

# 🎓 CodeAlpha Internship

This project was developed as part of the **CodeAlpha Artificial Intelligence / Machine Learning Internship**.

### Task

**Object Detection and Tracking**

### Main Implementation

```text
YOLO11n
   +
OpenCV
   +
ByteTrack
```

The project demonstrates practical implementation of object detection, video processing, multi-object tracking and real-time webcam processing.

---

# 🌐 GitHub Repository

Source code:

https://github.com/savitri2005/CodeAlpha_ObjectDetectionTracking_RealTime

---

# 👩‍💻 Author

**Savitri Kullolli**

AI & Machine Learning Student

---

# 📌 Conclusion

This project demonstrates an end-to-end object detection and tracking workflow using a pretrained YOLO11n model.

The system can:

```text
Detect objects in images
        ↓
Detect objects in videos
        ↓
Track objects across video frames
        ↓
Assign tracking IDs
        ↓
Process multiple videos
        ↓
Perform real-time webcam detection and tracking
```

The project provides practical experience with **computer vision, object detection, video processing, multi-object tracking and real-time AI applications**.

---

## 📄 License

This project was created for educational and internship purposes.
