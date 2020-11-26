from  center_contour import*

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



    def getEdges(img,imgContour):


    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    edges = 0
    center = []

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
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x,y), (x + w, y + h), (0,255,0), 5)
            cv2.putText(imgContour, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)
            edges = len(approx)
            center = (cX,cY)
    return edges,center