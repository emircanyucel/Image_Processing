"""
---These codes are created by Emircan Yücel---

In this script, we will detect two color on frame. First, camera will search the biggest red area in the image.
If the red area is greater than the specified condition, the camera will stop searching the red area and start
searching for the blue area.

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

    def getLargestRedOrBlueContour(img, red_contours, blue_contours):

        sortedRedContours = sorted(red_contours, key=cv2.contourArea, reverse=True)
        sortedBlueContours = sorted(blue_contours, key=cv2.contourArea, reverse=True)

        if len(sortedRedContours) == 0 or len(sortedBlueContours) == 0:
            print("Searching for color on camera.")
        else:

            largestRedContour = sortedRedContours[0]
            largestBlueContour = sortedBlueContours[0]

            red_area = cv2.contourArea(largestRedContour)
            blue_area = cv2.contourArea(largestBlueContour)


            if red_area > 10000 and blue_area > 500:
                x, y, w, h = cv2.boundingRect(largestBlueContour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                M = cv2.moments(largestBlueContour)
                cx = int(M['m10'] / M['m00'])
                x = (cx + 1) - 320
                cy = int(M['m01'] / M['m00'])
                y = -cy + 240
                cv2.drawContours(img, [largestBlueContour], -1, (0, 255, 0), 2)
                cv2.circle(img, (cx, cy), 3, (0, 0, 0), -1)
                cv2.putText(img, "center", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                print("x: {} y: {}".format(x, y))
                return x, y
            elif red_area > 500:
                x, y, w, h = cv2.boundingRect(largestRedContour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                M = cv2.moments(largestRedContour)
                cx = int(M['m10'] / M['m00'])
                x = (cx + 1) - 320
                cy = int(M['m01'] / M['m00'])
                y = -cy + 240
                cv2.drawContours(img, [largestRedContour], -1, (0, 255, 0), 2)
                cv2.circle(img, (cx, cy), 3, (0, 0, 0), -1)
                cv2.putText(img, "center", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                print("x: {} y: {}".format(x, y))
                return x, y

    ret, img = video.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    def kirmizi():
        low_red = np.array([0, 150, 0])
        high_red = np.array([5, 255, 255])

        mask_red = cv2.inRange(hsv, low_red, high_red)

        _, cnts_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        return cnts_red


    def mavi():
        low_blue = np.array([100,150,0])
        high_blue = np.array([140,255,255])
        mask_blue = cv2.inRange(hsv, low_blue, high_blue)

        _, cnts_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        return cnts_blue


    kirmizi = kirmizi()
    mavi = mavi()

    getLargestRedOrBlueContour(img, kirmizi, mavi)

    cv2.imshow("Frame", img)
    k = cv2.waitKey(1)


    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
