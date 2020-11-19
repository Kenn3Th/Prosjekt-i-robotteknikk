import cv2
import numpy as np


frameWidth = 1680    
frameHight = 1050
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHight)

def empty(a):
    pass


cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshhold1","Parameters",60,255,empty)
cv2.createTrackbar("Threshhold2","Parameters",50,255,empty)
cv2.createTrackbar("Area","Parameters",10000,50000,empty)



def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0,rows):
            for y in range(0,cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0,0),None,scale,scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),None,scale,scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height,width,3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0,rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0,rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x],(0,0),None,scale,scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale,scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver



def getContours(img,imgContour):


    contours = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    

    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area", "Parameters")
        #find center
        M = cv2.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        if area>areaMin:
            cv2.drawContours(imgContour,contours,-1,(255,0,255,5))
            cv2.circle(imgContour,(cX,cY),7,(255,255,255 ),-1)
            cv2.putText(imgContour, "center", (cX - 20, cY - 20),
		            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            #print(len(approx))
            print(cX,cY)
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x,y), (x + w, y + h), (0,255,0), 5)

            cv2.putText(imgContour, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)






while True:
    success, img = cap.read()
    imgContour = img.copy()

    imgBlur = cv2.GaussianBlur(img,(7,7),1)
    imgGray = cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)

    threshhold1 = cv2.getTrackbarPos("Threshhold1","Parameters")
    threshhold2 = cv2.getTrackbarPos("Threshhold2","Parameters")
    imgCanny = cv2.Canny(imgGray,threshhold1,threshhold2)
    kernel = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny,kernel,iterations=1)

    getContours(imgDil,imgContour)



    imgStack = stackImages(0.8,([imgContour]))

    cv2.imshow("Result",imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break