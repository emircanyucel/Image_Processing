#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
---These codes are created by Emircan Yücel---

In this script, we will find the color which has the biggest contour in the image. While doing this, we will tell the
algorithm the color we want by using the object-based programming technique.

You can reach my tutorial content, which I have prepared for a detailed explanation of this, and similar content,
where I share my experience and knowledge, from the link below.
https://medium.com/@emircanyucel27

To contact:
https://www.linkedin.com/in/emircan-y%C3%BCcel-267475246
"""

# Opencv Imports
import cv2
import numpy as np


class VisionofDrone:
    """
    1st argumet:
    Colors:
    - red
    - blue
    - green
    """

    def __init__(self, targetcolor):
        self.video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.position = {'color': targetcolor, 'found': False, 'x': 0, 'y': 0}
        self.resX = 640
        self.resY = 480
        self.video.set(3, self.resX)
        self.video.set(4, self.resY)
        self.targetcolor = targetcolor
        cx = 0
        cy = 0

    def OpenCV(self):

        def getContours(imgContour):

            _, contours, _ = cv2.findContours(imgContour, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            for cnt in contours:
                area = cv2.contourArea(cnt)

                if area > 300:
                    cv2.drawContours(img, cnt, -1, (0, 255, 0), 2)
                    peri = cv2.arcLength(cnt, True)
                    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
                    # c = max(contours, key=cv2.contourArea)
                    x, y, w, h = cv2.boundingRect(approx)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            for i in contours:
                M = cv2.moments(i)
                if M['m00'] != 0:
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                    cv2.drawContours(img, [i], -1, (0, 255, 0), 2)
                    cv2.circle(img, (cx, cy), 3, (0, 0, 0), -1)
                    cv2.putText(img, "center", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                    cx = (cx + 1) - 320
                    cy = -cy + 240
                    print("x: {} y: {}".format(cx, cy))

        while True:
            success, img = self.video.read()

            if not success:
                print("img değişkeni başlatma işlemi başarısız(success == False).")
                break

            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            color = None

            if self.targetcolor == 'red':
                color = cv2.inRange(hsv, np.array([0, 140, 200]), np.array([179, 255, 255]))
            elif self.targetcolor == 'blue':
                color = cv2.inRange(hsv, np.array([100, 50, 50]), np.array([140, 255, 255]))
            elif self.targetcolor == 'green':
                color = cv2.inRange(hsv, np.array([36, 0, 0]), np.array([86, 255, 255]))

            kernel = np.ones((5, 5), np.uint8)

            erotion = cv2.erode(color, kernel, iterations=1)
            dilation = cv2.dilate(erotion, kernel, iterations=1)

            getContours(dilation)

            cv2.imshow("Frame", img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.video.release()
        cv2.destroyAllWindows()


colorDetectionRed = VisionofDrone('red')


def initFuncRed():
    global colorDetectionRed
    colorDetectionRed.OpenCV()


initFuncRed()
