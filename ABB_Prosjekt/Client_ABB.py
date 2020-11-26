from center_contour import*
import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_IP = '192.168.12.97'
port = 2222
encoding = 'utf-8'

frameWidth = 1920    
frameHight = 1080
FPS = 1 # Frames Per Second
cap = cv2.VideoCapture(2)
cap.set(3, frameWidth)
cap.set(4, frameHight)
cap.set(5, FPS)

client.connect((HOST_IP,port)) # Socket oppkobling

print(f"Fått tilgang til {HOST_IP}")

def imageProcess():
    food = "" # Empty msg to be returned
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
    food = ObjectAnalysis(figur, center)
    return food
    
prev_msg = ""
while True: 
    
    data = client.recv(1024)
    print("\n"+data.decode(encoding))

    #imgStack = stackImages(0.8,([imgContour])) # Lager en matrise med flere bilder

    print("before if")
    msg = ""
    
    if data.decode(encoding) == "Feed me!":
        msg = imageProcess()
        prev_msg = ""
        if prev_msg == msg or msg == "":
            print(f"msg = {msg}")
            pass
        else:
            prev_msg = msg
            client.send(bytes(msg, encoding))
            print(f" beskjed = {msg}")
        time.sleep(5)



client.close()