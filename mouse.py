
import cv2
import math
img = cv2.imread("Sparsh.png",1)
center = []
circumference = []
cv2.namedWindow("Sparsh")
def call(action,x,y,flag,user):
    global center,circumeference

    if action==cv2.EVENT_LBUTTONDOWN:
        center = [(x,y)]
        cv2.circle(img,center[0],1,(0,0,255),5)
    elif action==cv2.EVENT_LBUTTONUP:
        circumference = [(x,y)]
        radius = math.sqrt(math.pow(center[0][0]-circumference[0][0],2)+math.pow(center[0][1]-circumference[0][1],2))
        cv2.circle(img,center[0],int(radius),(255,0,0),5)
    cv2.imshow("Sparsh",img)
cv2.imshow("Sparsh",img)
cv2.setMouseCallback("Sparsh",call)
cv2.waitKey(0)
cv2.destroyAllWindows()
