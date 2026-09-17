\# CodeAlpha Object Detection and Tracking - Real Time



\## 1. Project Title



\*\*Object Detection and Tracking using YOLO11 and ByteTrack\*\*



This project is developed as part of the \*\*CodeAlpha Internship - Object Detection and Tracking Task\*\*.



\---



\# 2. Project Overview



This project is a computer vision application developed using Python, YOLO11, Ultralytics, OpenCV, and ByteTrack.



The main purpose of this project is to detect objects in images and videos and track detected objects across consecutive video frames.



The project supports three types of input:



1\. Multiple images

2\. Multiple video files

3\. Real-time webcam input



The system performs object detection using the pretrained \*\*YOLO11n\*\* model and object tracking using \*\*ByteTrack\*\*.



The detected objects are displayed using bounding boxes, object labels, confidence scores, and tracking IDs.



\---



\# 3. Project Objectives



The main objectives of this project are:



\- To implement object detection using a pretrained YOLO11 model.

\- To process multiple images.

\- To process multiple video files.

\- To detect objects frame by frame in videos.

\- To draw bounding boxes around detected objects.

\- To display object class labels.

\- To display confidence scores.

\- To track objects across consecutive video frames.

\- To assign tracking IDs to detected objects.

\- To implement real-time webcam object detection.

\- To implement real-time webcam object tracking.

\- To save processed images and videos.

\- To demonstrate a complete computer vision pipeline.



\---



\# 4. Technologies Used



| Technology | Purpose |

|------------|---------|

| Python | Main programming language |

| YOLO11 | Object detection |

| YOLO11n | Lightweight pretrained detection model |

| Ultralytics | YOLO11 implementation |

| ByteTrack | Object tracking |

| OpenCV | Image, video, and webcam processing |

| Computer Vision | Object detection and tracking |

| Deep Learning | Object recognition |



\---



\# 5. System Requirements



The project requires:



\- Windows operating system

\- Python 3.x

\- Webcam for real-time testing

\- Internet connection for installing Python packages and downloading the YOLO model

\- Sufficient storage for Python packages, model files, and output videos



\---



\# 6. Project Workflow



The complete project workflow is:



```text

Input

&#x20; │

&#x20; ├── Images

&#x20; │

&#x20; ├── Videos

&#x20; │

&#x20; └── Webcam

&#x20;      │

&#x20;      ▼

&#x20;    OpenCV

&#x20;      │

&#x20;      ▼

&#x20;   YOLO11n

&#x20;      │

&#x20;      ▼

&#x20;Object Detection

&#x20;      │

&#x20;      ├── Object Class

&#x20;      ├── Bounding Box

&#x20;      └── Confidence Score

&#x20;      │

&#x20;      ▼

&#x20;   ByteTrack

&#x20;      │

&#x20;      ▼

&#x20;Object Tracking

&#x20;      │

&#x20;      ▼

&#x20;  Tracking IDs

&#x20;      │

&#x20;      ▼

&#x20;Display / Save Results

7\. YOLO11 Model



This project uses the pretrained:



YOLO11n



model.



YOLO stands for You Only Look Once.



YOLO is a real-time object detection model that can identify objects in images and video frames.



The n in YOLO11n means Nano.



YOLO11n is a lightweight model designed for faster inference and real-time applications.



The model file used in this project is:



models/yolo11n.pt



The model is loaded using:



from ultralytics import YOLO



model = YOLO("models/yolo11n.pt")

8\. Initial Project Setup



The project was created with the following folder:



CodeAlpha\_ObjectDetectionTracking\_RealTime



The project contains separate folders for:



Input images

Input videos

YOLO model

Output files

Virtual environment

9\. Creating the Virtual Environment



A Python virtual environment is used to keep the project dependencies separate.



Create the virtual environment using:



python -m venv venv



Activate it using Windows PowerShell:



.\\venv\\Scripts\\Activate.ps1



After activation, the terminal displays:



(venv)

10\. Installing Required Libraries



The main libraries used in this project are:



ultralytics

opencv-python



Install them using:



pip install ultralytics opencv-python



The dependencies are also stored in:



requirements.txt



Install all requirements using:



pip install -r requirements.txt

11\. YOLO11 Model Testing



The file:



test\_yolo.py



is used to verify that the YOLO11 model loads successfully.



The code loads:



models/yolo11n.pt



Run it using:



python test\_yolo.py



Successful output:



YOLO11 model loaded successfully!



This confirms that the YOLO11 model is available and can be loaded by the project.



12\. Image Object Detection



The file:



detect\_image.py



is used for object detection in multiple images.



Images are placed inside:



input\_images/



Supported image formats are:



.jpg

.jpeg

.png



The program automatically finds all supported images.



For every image:



OpenCV reads the image.

YOLO11 processes the image.

Objects are detected.

Bounding boxes are generated.

Object labels are displayed.

Confidence scores are generated.

The annotated image is saved.

The result is displayed.

13\. Running Image Detection



Place images inside:



input\_images/



Then run:



python detect\_image.py



The program processes all images automatically.



The output is saved inside:



output/detected\_images/



Example:



input\_images/animals.jpg



becomes:



output/detected\_images/animals.jpg

14\. Image Detection Testing



The image detection stage was tested using multiple images.



Example images included:



animals.jpg

cars.jpg

people.jpg

test.jpg



The model detected different objects such as:



Persons

Cars

Trucks

Bicycles

Dogs

Backpacks

Elephants

Zebras

Giraffes



The results were successfully saved to the output folder.



15\. Video Object Detection



The file:



detect\_video.py



is used for object detection in multiple videos.



Videos are placed inside:



input\_videos/



Supported formats are:



.mp4

.avi

.mov

.mkv



The program automatically finds all supported videos.



Each video is processed frame by frame.



For every frame:



The frame is read using OpenCV.

YOLO11 detects objects.

Bounding boxes are drawn.

Object labels are displayed.

Confidence scores are displayed.

The processed frame is displayed.

The processed frame is saved into an output video.

16\. Running Video Detection



Place videos inside:



input\_videos/



Then run:



python detect\_video.py



The program processes all videos automatically.



The detection results are saved inside:



output/detected\_videos/



Example:



input\_videos/people.mp4



produces:



output/detected\_videos/detected\_people.mp4

17\. Multiple Video Processing



The project supports multiple videos instead of processing only one video.



For example:



input\_videos/

│

├── people.mp4

├── cars.mp4

├── traffic.mp4

└── street.mp4



The program processes them one after another.



This makes the project more flexible and demonstrates that the application can handle multiple input videos.



18\. Object Tracking



Object detection identifies objects in each frame.



Object tracking goes one step further by attempting to maintain the identity of an object across consecutive frames.



This project uses:



ByteTrack



for object tracking.



The tracking system associates detections between frames and assigns tracking IDs.



19\. ByteTrack



ByteTrack is an object tracking algorithm used to associate detected objects across video frames.



It works together with the YOLO11 detection results.



The workflow is:



Video Frame

&#x20;    ↓

YOLO11 Detection

&#x20;    ↓

Detected Objects

&#x20;    ↓

ByteTrack

&#x20;    ↓

Tracking IDs

20\. Tracking IDs



A tracking ID is a number assigned to an object being tracked.



For example:



person 1

person 2

car 3

car 4



Here:



person



is the object class.



The numbers:



1

2

3

4



are tracking IDs.



The confidence value is separate from the tracking ID.



Example:



person 1 0.92



means:



person → object class

1 → tracking ID

0.92 → confidence score



Tracking IDs are automatically generated by ByteTrack.



21\. Video Object Tracking



The file:



track\_video.py



is used for object tracking in multiple videos.



The program:



Reads videos from input\_videos.

Reads frames using OpenCV.

Detects objects using YOLO11.

Uses ByteTrack to track objects.

Assigns tracking IDs.

Draws bounding boxes.

Displays labels and IDs.

Saves the tracked video.

22\. Running Video Tracking



Run:



python track\_video.py



The program processes all videos inside:



input\_videos/



The tracked videos are saved inside:



output/tracked\_videos/



Example:



input\_videos/people.mp4



produces:



output/tracked\_videos/tracked\_people.mp4

23\. Real-Time Webcam Detection



The project also supports real-time webcam input.



The webcam is accessed using:



cv2.VideoCapture(0)



The webcam continuously provides frames to the application.



Each frame is processed by YOLO11.



24\. Real-Time Webcam Tracking



The file:



webcam\_tracking.py



implements real-time object detection and tracking.



The workflow is:



Webcam

&#x20;  ↓

OpenCV

&#x20;  ↓

YOLO11

&#x20;  ↓

Object Detection

&#x20;  ↓

ByteTrack

&#x20;  ↓

Tracking IDs

&#x20;  ↓

Display



The webcam application displays:



Bounding boxes

Object labels

Confidence scores

Tracking IDs

25\. Running Webcam Tracking



Run:



python webcam\_tracking.py



The webcam window opens automatically.



Objects detected by YOLO11 are displayed with bounding boxes and labels.



ByteTrack assigns tracking IDs to tracked objects.



Press:



Q



to stop the webcam application.



26\. Confidence Threshold



The webcam tracking application uses:



conf=0.50



This means detections with confidence below 50% are filtered out.



The confidence score is different from the tracking ID.



For example:



person 1 0.91



means:



person = object class

1 = tracking ID

0.91 = confidence



The confidence threshold helps reduce very low-confidence detections.



However, confidence filtering does not guarantee that every predicted object class will always be correct.



27\. Object Detection Accuracy



Because this project uses a pretrained general-purpose YOLO11 model, some objects can occasionally be classified incorrectly.



For example, an actual bottle may sometimes be predicted as another class.



Possible reasons include:



Poor lighting

Motion blur

Small objects

Object occlusion

Similar-looking objects

Unusual camera angles

Complex backgrounds

Objects outside the model's trained classes

Limitations of the lightweight YOLO11n model



This is a limitation of the pretrained detection model and does not necessarily indicate an error in the implementation.



28\. Tracking Limitations



Tracking IDs can sometimes change.



This can happen when:



An object becomes temporarily hidden.

Two objects overlap.

The object leaves the camera view.

The object re-enters the frame.

The detector temporarily fails to detect the object.

The object moves very quickly.



These situations can make it difficult for the tracker to maintain the same identity.



29\. Output Files



The project creates different types of outputs.



Detected Images

output/detected\_images/

Detected Videos

output/detected\_videos/

Tracked Videos

output/tracked\_videos/

30\. Complete Project Structure

CodeAlpha\_ObjectDetectionTracking\_RealTime/

│

├── input\_images/

│   ├── animals.jpg

│   ├── cars.jpg

│   ├── people.jpg

│   └── test.jpg

│

├── input\_videos/

│   ├── people.mp4

│   ├── cars.mp4

│   ├── traffic.mp4

│   └── other videos

│

├── models/

│   └── yolo11n.pt

│

├── output/

│   ├── detected\_images/

│   ├── detected\_videos/

│   └── tracked\_videos/

│

├── venv/

│

├── test\_yolo.py

├── detect\_image.py

├── detect\_video.py

├── track\_video.py

├── webcam\_tracking.py

├── requirements.txt

├── .gitignore

└── README.md

31\. Description of Python Files

test\_yolo.py



Tests whether the YOLO11 model loads successfully.



detect\_image.py



Processes multiple images and performs object detection.



detect\_video.py



Processes multiple videos and performs object detection frame by frame.



track\_video.py



Processes multiple videos and performs object detection and object tracking using ByteTrack.



webcam\_tracking.py



Performs real-time webcam object detection and tracking using YOLO11 and ByteTrack.



32\. Requirements File



The project contains:



requirements.txt



The file contains:



ultralytics

opencv-python



Install the requirements using:



pip install -r requirements.txt

33\. Git Ignore



The project contains:



.gitignore



The following files and folders are ignored:



venv/

\_\_pycache\_\_/

\*.pyc

models/\*.pt

output/

\*.tmp

\*.log



The virtual environment and generated output files are not required in the GitHub repository.



The YOLO model file is also excluded from GitHub because it can be downloaded separately.



34\. Complete Installation Guide

Step 1: Clone the repository

git clone https://github.com/your-username/CodeAlpha\_ObjectDetectionTracking\_RealTime.git

Step 2: Open the project

cd CodeAlpha\_ObjectDetectionTracking\_RealTime

Step 3: Create virtual environment

python -m venv venv

Step 4: Activate virtual environment

.\\venv\\Scripts\\Activate.ps1

Step 5: Install dependencies

pip install -r requirements.txt

Step 6: Download or place the YOLO11 model



The project uses:



models/yolo11n.pt



The model should be available at this location before running the programs.



35\. Complete Execution Guide

Test the model

python test\_yolo.py

Detect objects in images

python detect\_image.py

Detect objects in multiple videos

python detect\_video.py

Track objects in multiple videos

python track\_video.py

Run real-time webcam detection and tracking

python webcam\_tracking.py



Press Q to stop the webcam.



36\. Testing Performed



The project was tested using:



Multiple images

Multiple video files

Real-time webcam input



The image detection stage successfully processed multiple images.



The video detection stage successfully processed multiple videos.



The video tracking stage successfully displayed tracking IDs.



The webcam stage successfully performed real-time object detection and tracking.



37\. Example Detection Results



The system can detect common objects such as:



Person

Car

Truck

Bicycle

Dog

Backpack

Bottle

Animal classes



The actual detected classes depend on the pretrained model and the input image or video.



38\. Example Tracking Result



An example tracking result can look like:



person 1

person 2

car 3

car 4



The IDs allow objects to be distinguished from each other while they are being tracked.



39\. Performance Information



During webcam processing, YOLO11 reports processing information such as:



preprocess

inference

postprocess



Example:



Speed: 1.8ms preprocess, 72.9ms inference, 2.0ms postprocess



These values indicate the approximate processing time for a frame and can vary depending on the computer, input resolution, and system load.



40\. Project Advantages



This project demonstrates:



Real-time computer vision

Object detection

Object tracking

Video processing

Webcam processing

Deep learning model usage

Multiple input processing

Tracking ID generation

Python programming

Practical use of OpenCV

Practical use of YOLO11

Practical use of ByteTrack

41\. Limitations



The project is based on a pretrained YOLO11n model.



Therefore:



Detection is not guaranteed to be perfect.

Some objects can be incorrectly classified.

Tracking IDs can occasionally change.

Very small objects may be difficult to detect.

Poor lighting can affect detection.

Occluded objects may be missed.

Fast-moving objects may be difficult to track.

Webcam performance depends on hardware.



The project is intended as an educational and internship implementation demonstrating object detection and tracking.



42\. Future Improvements



Possible future improvements include:



Training YOLO on a custom dataset.

Using a larger YOLO11 model.

Improving object detection accuracy.

Adding more tracking algorithms.

Adding object counting.

Adding line-crossing detection.

Adding region-based counting.

Adding alert systems.

Adding a graphical user interface.

Adding performance monitoring.

Supporting additional input sources.

Improving tracking stability.

43\. CodeAlpha Internship Task



Organization: CodeAlpha



Internship Task: Object Detection and Tracking



Project: Real-Time Object Detection and Tracking



The project demonstrates the practical implementation of computer vision using a pretrained YOLO11 model, OpenCV, and ByteTrack.



44\. Author



Savitri Kullolli



Bachelor of Engineering

Artificial Intelligence \& Machine Learning



45\. Conclusion



This project implements a complete object detection and tracking system.



The project starts with input images, videos, or webcam frames.



OpenCV is used to capture and process the input.



YOLO11 is used to detect objects.



ByteTrack is used to track detected objects across video frames.



The system displays:



Bounding boxes

Object labels

Confidence scores

Tracking IDs



The project supports:



Multiple Image Detection

&#x20;       ↓

Multiple Video Detection

&#x20;       ↓

Multiple Video Tracking

&#x20;       ↓

Real-Time Webcam Detection

&#x20;       ↓

Real-Time Webcam Tracking



This project demonstrates the practical application of Deep Learning, Computer Vision, Object Detection, and Object Tracking using Python.



46\. License



This project is developed for educational and internship purposes.





\### Now save this as the \*\*only README file\*\*



Run:



```powershell

notepad README.md

