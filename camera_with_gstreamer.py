"""
---These codes are created by Emircan Yücel---

In this script, we will connect to the camera with gstreamer. Gstreamer is a media processing and streaming framework.
(GStreamer can be used to process, encode, encrypt and distribute audio, video and image data.)

NOTE: If you want to launch camera in linux terminal, you can copy and paste this code to the terminal.

gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw,width=640,height=480,framerate=30/1 ! videoconvert ! autovideosink

You can reach my tutorial content, which I have prepared for a detailed explanation of this, and similar content,
where I share my experience and knowledge, from the link below.
https://medium.com/@emircanyucel27

To contact:
https://www.linkedin.com/in/emircan-y%C3%BCcel-267475246
"""

import cv2

# GStreamer pipeline
pipeline = (
    "v4l2src device=/dev/video0 ! "
    "video/x-raw, width=640, height=480, framerate=30/1 ! "
    "videoconvert ! "
    "appsink"
)

cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error. Please check the connection.")
        break

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
