# Real-Time Vehicle Detection and Counting System using YOLOv8 and SORT

## Overview

This project implements a real-time vehicle detection, tracking, and counting system using Computer Vision techniques.

The system detects vehicles from video input using YOLOv8, tracks detected vehicles using the SORT tracking algorithm, and counts vehicles when they cross a predefined counting line.

The goal of this project is to explore practical applications of object detection and multi-object tracking in real-world scenarios such as traffic monitoring and intelligent transportation systems.

---

## Features

* Real-time vehicle detection
* Multi-object tracking with unique IDs
* Vehicle counting using line-crossing detection
* Bounding box visualization
* Confidence-based detection filtering
* Region-of-interest masking for improved detection efficiency

---

## Technologies Used

* Python
* OpenCV
* YOLOv8
* SORT (Simple Online and Realtime Tracking)
* NumPy
* CVZone

---

## How It Works

The system follows this pipeline:

```
Video Input
      |
      ↓
YOLOv8 Object Detection
      |
      ↓
Detection Filtering
      |
      ↓
SORT Object Tracking
      |
      ↓
Vehicle ID Assignment
      |
      ↓
Line Crossing Detection
      |
      ↓
Vehicle Count
```

---

## Project Workflow

### 1. Object Detection

YOLOv8 processes each video frame and detects objects by generating:

* Bounding boxes
* Class labels
* Confidence scores

Example output:

```
Vehicle:
x1, y1, x2, y2
Confidence: 0.91
```

---

### 2. Object Tracking

The SORT algorithm receives YOLO detections and assigns unique IDs to detected vehicles.

Example:

```
Vehicle ID 1
Vehicle ID 2
Vehicle ID 3
```

This allows the system to identify the same vehicle across multiple frames.

---

### 3. Vehicle Counting

A virtual counting line is placed in the video.

When a tracked vehicle's center point crosses this line, the system increases the vehicle count.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/vehicle-detection-and-counting-yolov8.git
```

Navigate to the project folder:

```bash
cd vehicle-detection-and-counting-yolov8
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements

Create `requirements.txt`:

```
opencv-python
ultralytics
cvzone
numpy
filterpy
scipy
```

---

## Running the Project

Run:

```bash
python main.py
```

Press:

```
q
```

to close the video window.

---

## Results

The system can:

* Detect vehicles in video streams
* Track each vehicle with a unique ID
* Count vehicles passing through a selected area

---

## Future Improvements

Possible improvements:

* Train YOLO on custom vehicle datasets
* Add vehicle speed estimation
* Add vehicle classification (car, bus, truck)
* Deploy as a real-time traffic monitoring application
* Add dashboard visualization
* Use advanced trackers such as DeepSORT or ByteTrack

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Object detection
* Multi-object tracking
* Real-time computer vision pipelines
* YOLO model inference
* OpenCV video processing

---

## Author

Damsara Jayanath

Machine Learning / Computer Vision Engineer in Progress
