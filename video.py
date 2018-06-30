
import cv2
import math

cap = cv2.VideoCapture(0)
center = []
circumference = []
while True:
    ret,img = cap.read()
    cv2.namedWindow("Sparsh")
    def call(action,x,y,flag,user):
        global center,circumeference

        if action==cv2.EVENT_LBUTTONDOWN:
            center = [(x,y),(x,y)]
            cv2.circle(img,center[0],1,(0,0,255),5)
        elif action==cv2.EVENT_MOUSEMOVE:
            center[1]=(x,y)
            cv2.line(img,center[0],center[1],(0,255,0),4)
        elif action==cv2.EVENT_LBUTTONUP:
            circumference = [(x,y)]
            radius = math.sqrt(math.pow(center[0][0]-circumference[0][0],2)+math.pow(center[0][1]-circumference[0][1],2))
            cv2.circle(img,center[0],int(radius),(255,0,0),5)
        cv2.imshow("Sparsh",img)
        cv2.imwrite("test1.png",img)
    cv2.imshow("Sparsh",img)
    cv2.setMouseCallback("Sparsh",call)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()
