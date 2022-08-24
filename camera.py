import cv2
cam=cv2.VideoCapture(0)
while True:
    _,frame=cam.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey and  0xff == ord('q'):
        break
cv2.destroyAllWindows()