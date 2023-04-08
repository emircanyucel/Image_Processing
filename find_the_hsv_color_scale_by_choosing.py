"""
---These codes are created by Emircan Yücel---

In this script, we will find the hsv color scale by choosing. When we click on a pixel in the frame, the selected pixel
is shown with an hsv color scale.

You can reach my tutorial content, which I have prepared for a detailed explanation of this, and similar content,
where I share my experience and knowledge, from the link below.
https://medium.com/@emircanyucel27

To contact:
https://www.linkedin.com/in/emircan-y%C3%BCcel-267475246
"""

import cv2
import numpy as np


def select_roi(event, x, y, flags, param):
    global frame, roi_points, roi_selected, roi_ready

    if event == cv2.EVENT_LBUTTONDOWN:
        if not roi_ready:
            roi_points.append((x, y))
            if len(roi_points) == 2:
                roi_ready = True
                roi_selected = True
        else:
            roi_points = [(x, y)]
            roi_selected = False
            roi_ready = False


def get_hsv_range_with_margin(roi, margin):
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    hue_min = max(np.min(hsv_roi[:, :, 0]) - margin[0], 0)
    hue_max = min(np.max(hsv_roi[:, :, 0]) + margin[0], 179)
    sat_min = max(np.min(hsv_roi[:, :, 1]) - margin[1], 0)
    sat_max = min(np.max(hsv_roi[:, :, 1]) + margin[1], 255)
    val_min = max(np.min(hsv_roi[:, :, 2]) - margin[2], 0)
    val_max = min(np.max(hsv_roi[:, :, 2]) + margin[2], 255)

    return (hue_min, hue_max, sat_min, sat_max, val_min, val_max)


cap = cv2.VideoCapture(0)

cv2.namedWindow('kamera')
cv2.setMouseCallback('kamera', select_roi)

roi_points = []
roi_ready = False
roi_selected = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if len(roi_points) == 1 and not roi_selected:
        cv2.circle(frame, roi_points[0], 5, (0, 0, 255), 2)

    if roi_selected:
        cv2.rectangle(frame, roi_points[0], roi_points[1], (0, 255, 0), 2)
        roi = frame[roi_points[0][1]:roi_points[1][1], roi_points[0][0]:roi_points[1][0]]

        margin_values = (10, 10, 10)
        hsv_range_with_margin = get_hsv_range_with_margin(roi, margin_values)

        print("HSV scale:", hsv_range_with_margin)

    cv2.imshow('camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
