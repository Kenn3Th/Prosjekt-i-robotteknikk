from center_contour import*
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_IP = '192.168.12.25'
port = 2222
encoding = 'utf-8'

client.connect((HOST_IP,port)) # Socket oppkobling

print(f"Fått tilgang til {HOST_IP}")

center = [[50,100],[200,150],[0,0],[185,70],[185,70],[250,170],[185,70],[185,70],[185,70],[0,0]]
i = 0
while True: 
    data = client.recv(1024)
    print("\n"+data.decode(encoding))
    if data == "Feed me!":
        food = ObjectAnalysis(i+3, center[i])
        client.send(bytes(food,encoding))
        print(food)
        i += 1
    if i>10:
        i=0

    #time.sleep(20)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


client.close()