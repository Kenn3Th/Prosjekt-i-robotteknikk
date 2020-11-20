from center_contour import*
import socket
import time
import cv2




client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_IP = '192.168.12.97'
port = 2222
encoding = 'utf-8'

client.connect((HOST_IP,port)) # Socket oppkobling

print(f"Fått tilgang til {HOST_IP}")




while True: 
    
    data = client.recv(1024)
    print("\n"+data.decode(encoding))

    food = ""
    success, img = cap.read()
    img = cv2.flip(img,0)
    imgContour = img.copy()

    imgBlur = cv2.GaussianBlur(img,(7,7),1)
    imgGray = cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)

    threshhold1 = 55
    threshhold2 = 50
    imgCanny = cv2.Canny(imgGray,threshhold1,threshhold2)
    kernel = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny,kernel,iterations=1)

    figur,center = getContours(imgDil,imgContour) 

    #imgStack = stackImages(0.8,([imgContour])) # Lager en matrise med flere bilder

    print("before if")



    if data.decode(encoding) == "Feed me!":
        #if type(figur) == int:
        food = ObjectAnalysis(figur, center)
        client.send(bytes(food,encoding))
        print(food)
        #time.sleep(20)



client.close()