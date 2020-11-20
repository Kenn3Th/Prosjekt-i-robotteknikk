from center_contour import*
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_IP = '192.168.12.25'
port = 2222
encoding = 'utf-8'

client.connect((HOST_IP,port)) # Socket oppkobling

edges = 4
center = [20,150]
while True:
    
    #figur,center = getContours(imgDil,imgContour) # Finner 

    #print(center)
    #imgStack = stackImages(0.8,([imgContour])) # Lager en matrise med flere bilder
    #cv2.imshow("Result",imgStack) # Viser resultat paa skjerm 

    msg = ObjectAnalysis(edges, center)
    client.send(bytes(msg,encoding)) # sender meldingen

    print(msg)
    #time.sleep(2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


client.close()