"""
---These codes are created by Emircan Yücel---

In this script, we will find the color which has the biggest contour in the image.

You can reach my tutorial content, which I have prepared for a detailed explanation of this, and similar content,
where I share my experience and knowledge, from the link below.
https://medium.com/@emircanyucel27

To contact:
https://www.linkedin.com/in/emircan-y%C3%BCcel-267475246
"""

import cv2
import numpy as np

cx, cy = 0, 0

video = cv2.VideoCapture(0)

while True:
    ret, img = video.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    low_blue = np.array([0, 143, 166])
    high_blue = np.array([70, 255, 255])

    mask = cv2.inRange(hsv, low_blue, high_blue)

    # kernel = np.ones((5, 5), np.uint8)
    # erotion = cv2.erode(mask, kernel, iterations=1)
    # dilation = cv2.dilate(erotion, kernel, iterations=1)

    _, cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


    def getLargestRedContour(img, contours):

        sortedContours = sorted(contours, key=cv2.contourArea, reverse=True)

        for cnt in sortedContours:
            area = cv2.contourArea(cnt)
            if area > 500:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                M = cv2.moments(cnt)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)
                cv2.circle(img, (cx, cy), 3, (0, 0, 0), -1)
                cv2.putText(img, "center", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                cx = (cx + 1) - 320
                cy = -cy + 240
                print("x: {} y: {}".format(cx, cy))

                return cx, cy

        return 0, 0


    getLargestRedContour(img, cnts)
    cv2.imshow("Frame", img)

    k = cv2.waitKey(1)

    if cx or cy != 0:
        break


    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
