"""
---These codes are created by Emircan Yücel---

In this script, we will detect the shapes of the blue regions in the image in the picture.

You can reach my tutorial content, which I have prepared for a detailed explanation of this, and similar content,
where I share my experience and knowledge, from the link below.
https://medium.com/@emircanyucel27

To contact:
https://www.linkedin.com/in/emircan-y%C3%BCcel-267475246
"""


import cv2
import numpy as np

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, img = video.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    kernel = np.ones((5, 5), np.uint8)

    cv2.line(img, (0, 240), (640, 240), (0, 255, 0), 1, )
    cv2.line(img, (320, 480), (320, 0), (0, 255, 0), 1, )
    cv2.circle(img, (320, 240), 40, (0, 255, 0), 1)


    low_blue = np.array([80, 160, 60])
    high_blue = np.array([179, 255, 255])
    mask_blue = cv2.inRange(hsv, low_blue, high_blue)

    erotion_blue = cv2.erode(mask_blue, kernel, iterations=1)
    dilation_blue = cv2.dilate(erotion_blue, kernel, iterations=1)

    _, cnts_blue, _ = cv2.findContours(dilation_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for c in cnts_blue:
        area = cv2.contourArea(c)
        if area > 200:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Points: " + str(len(approx)), (x + w + 20, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 255, 0), 2)

            if len(approx) == 4:
                cv2.putText(img, "square", (x + w + 20, y + h + 45), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            elif len(approx) == 3:
                cv2.putText(img, "triangle", (x + w + 20, y + h + 45), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            else:
                cv2.putText(img, "circle", (x + w + 20, y + h + 45), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            break

    cnts_blue = sorted(cnts_blue, key=lambda x: cv2.contourArea(x), reverse=True)
    for c in cnts_blue:
        (x, y, w, h) = cv2.boundingRect(c)

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        break

    for i in cnts_blue:
        M = cv2.moments(i)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.drawContours(img, [i], -1, (0, 255, 0), 2)
            cv2.circle(img, (cx, cy), 3, (0, 0, 255), -1)
            cv2.putText(img, "center", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cx = (cx + 1) - 320
            cy = -cy + 240
            print("x: {}, y: {}".format(cx, cy))


    low_red = np.array([0, 190, 140])
    high_red = np.array([10, 255, 255])
    red_mask = cv2.inRange(hsv, low_red, high_red)

    erotion_red = cv2.erode(red_mask, kernel, iterations=1)
    dilation_red = cv2.dilate(erotion_red, kernel, iterations=1)

    _, cnts_red, _ = cv2.findContours(dilation_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for d in cnts_red:
        area = cv2.contourArea(d)
        if area > 200:
            peri = cv2.arcLength(d, True)
            approx = cv2.approxPolyDP(d, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(d)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Points: " + str(len(approx)), (x + w + 20, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 255, 0), 2)

            if len(approx) == 4:
                cv2.putText(img, "Dortgen", (x + w + 20, y + h + 45), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            elif len(approx) == 3:
                cv2.putText(img, "Ucgen", (x + w + 20, y + h + 45), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            else:
                cv2.putText(img, "Daire", (x + w + 20, y + h + 45), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            break

    cnts_red = sorted(cnts_red, key=lambda x: cv2.contourArea(x), reverse=True)  ####
    for c in cnts_red:
        (x, y, w, h) = cv2.boundingRect(c)

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        break

    for k in cnts_red:
        M = cv2.moments(k)
        if M['m00'] != 0:
            cx2 = int(M['m10'] / M['m00'])
            cy2 = int(M['m01'] / M['m00'])
            cv2.drawContours(img, [k], -1, (0, 255, 0), 2)
            cv2.circle(img, (cx2, cy2), 3, (0, 0, 255), -1)
            cv2.putText(img, "center", (cx2 - 20, cy2 - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            cx2 = (cx2 + 1) - 320
            cy2 = (-cy2) + 240
            print("x: {} y: {}".format(cx2, cy2))

    cv2.imshow("Frame", img)
    cv2.imshow("Mask Blue", mask_blue)
    cv2.imshow("Mask Red", red_mask)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
