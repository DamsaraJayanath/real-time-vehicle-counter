# Real-Time Vehicle Counter

## Overview

**Real-Time Vehicle Counter** is a computer vision project that detects, tracks, and counts vehicles from video input using YOLOv8, OpenCV, and the SORT tracking algorithm.

The system performs real-time vehicle detection using YOLOv8, assigns unique IDs to detected vehicles using SORT tracking, and counts vehicles when they cross a predefined counting line.

This project demonstrates the practical application of object detection, multi-object tracking, and real-time computer vision pipelines for traffic monitoring systems.

---

## Features

* Real-time vehicle detection
* Multi-object tracking with unique IDs
* Vehicle counting using line-crossing detection
* Bounding box visualization
* Confidence score filtering
* Region-of-interest masking
* Real-time video processing

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

### 1. Vehicle Detection

YOLOv8 processes each video frame and detects objects by generating:

* Bounding boxes
* Object classes
* Confidence scores

Example:

```
Vehicle:
(x1, y1, x2, y2)

Confidence:
0.91
```

---

### 2. Vehicle Tracking

The detected objects are passed to the SORT tracking algorithm.

SORT assigns unique IDs to vehicles and maintains their identity across multiple frames.

Example:

```
Vehicle ID 1
Vehicle ID 2
Vehicle ID 3
```

This allows the system to recognize the same vehicle while it moves through the video.

---

### 3. Vehicle Counting

A virtual counting line is placed in the video.

When the center point of a tracked vehicle crosses this line, the vehicle ID is added to the count list.

This prevents the same vehicle from being counted multiple times.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/damsarajayanath/real-time-vehicle-counter.git
```

Navigate to the project directory:

```bash
cd real-time-vehicle-counter
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements

Create a `requirements.txt` file:

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

Run the application:

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

* Detect vehicles from video streams
* Track multiple vehicles simultaneously
* Assign unique IDs
* Count vehicles crossing a selected area

---

## Future Improvements

Possible improvements:

* Train YOLO on custom vehicle datasets
* Add vehicle speed estimation
* Add vehicle type classification
* Create a real-time traffic dashboard
* Deploy as an API service
* Use advanced tracking algorithms such as DeepSORT or ByteTrack

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Object detection
* Multi-object tracking
* YOLO model inference
* OpenCV video processing
* Real-time computer vision systems
* Tracking and counting algorithms

---

## Author

**Damsara Jayanath**

Machine Learning / Computer Vision Engineer in Progress
