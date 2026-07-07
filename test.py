import cv2 as cv
from ultralytics import YOLO
import cvzone
from sort import *
import numpy as np

cap = cv.VideoCapture('video/sample.mp4')
cap.set(3, 1280)
cap.set(4, 720)

model = YOLO("yolo_weights/yolov8n.pt")
mask = cv.imread("mask.png")

tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)
limits = [0, 400, 1280, 400]

totalCount = []

while True:
    success, img = cap.read()
    imgRegion = cv.bitwise_and(img, mask)
    if not success:
        break

    detections = np.empty((0,5))
    results = model(imgRegion)
    r = results[0]

    for box in r.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        w, h = x2 - x1, y2 - y1

        conf = round(float(box.conf[0]),2)

        cls = int(box.cls[0])
        class_name = model.names[cls]

        vehicle_classes = ['car', 'truck', 'bus', 'motorcycle']

        if conf > 0.4 and class_name in vehicle_classes:
            # print(class_name)
            # cvzone.cornerRect(img, (x1,y1,w,h), l=5, rt=3, colorR=(255,0,0))
            currentArray = np.array([x1,y1,x2,y2,conf])
            detections = np.vstack((detections, currentArray))

    resultTracker = tracker.update(detections)
    cv.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), 3)
    for result in resultTracker:
        x1, y1, x2, y2, id = result
        x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
        # print(result)
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(255, 0, 0))
        # cvzone.putTextRect(img, f'{int(id)}', (max(0, x1), max(35, y1)), scale=2, thickness=2, offset=3)

        cx, cy = x1+w//2, y1+h//2
        cv.circle(img, (cx, cy), 3, (255,0,255), cv.FILLED)

        if limits[0] < cx < limits[2] and limits[1] - 30 < cy < limits[1] + 30:
            if totalCount.count(id) == 0:
                totalCount.append(id)
                cv.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 0, 255), 2)

    cvzone.putTextRect(img, f'Count: {len(totalCount)}', (50, 50))
    cv.imshow("Video", img)
    # cv.imshow("mask", imgRegion)
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
