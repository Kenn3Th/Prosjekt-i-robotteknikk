from center_contour import*
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_IP = '192.168.12.25'
port = 2222
encoding = 'utf-8'

client.connect((HOST_IP,port)) # Socket oppkobling

print(f"Fått tilgang til {HOST_IP}")

center = [[50,100],[200,150],[185,70],[250,170]]
edges = [3,4,6,8]
i = 0
food = ""

while True: 
    success, img = cap.read()
    img = cv2.flip(img,0)
    imgContour = img.copy()

    imgBlur = cv2.GaussianBlur(img,(7,7),1)
    imgGray = cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)

    threshhold1 = cv2.getTrackbarPos("Threshhold1","Parameters")
    threshhold2 = cv2.getTrackbarPos("Threshhold2","Parameters")
    imgCanny = cv2.Canny(imgGray,threshhold1,threshhold2)
    kernel = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny,kernel,iterations=1)

    figur,center = getContours(imgDil,imgContour) # Finner 

    imgStack = stackImages(0.8,([imgContour])) # Lager en matrise med flere bilder

    data = client.recv(1024)
    print("\n"+data.decode(encoding))
    msg = ObjectAnalysis(figur, center)
    print(msg)
    time.sleep(2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if data.decode(encoding) == "Feed me!":
        food = ObjectAnalysis(edges[i], center[i])
        client.send(bytes(food,encoding))
        print(food)
        i += 1
    if i>=3:
        i=0

    #time.sleep(20)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


client.close()