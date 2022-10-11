import cv2
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Security cam', frame1)