import cv2
from util import get_limits
from PIL import Image
yellow=[100,0,0]
cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    hsvImage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerLimit,upperLimit=get_limits(color=yellow)
    mask=cv2.inRange(hsvImage,lowerLimit,upperLimit)
    mask_=Image.fromarray(mask)
    bbox=mask_.getbbox()

    if bbox is not None:
        frame = cv2.rectangle(frame,(bbox[0],bbox[1]),(bbox[2],bbox[3]),(0,255,0),2)

    cv2.imshow("mask",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    