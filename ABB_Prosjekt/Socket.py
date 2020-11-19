import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = '127.0.0.0'
host = IP
port = 8888
encoding = 'utf-8'

msg = ''
client.connect((host,port)) #Socket oppkobling
print('Send command til roboten, skriv exit for å avslutte programmet')
print(client.recv(1024))
while(msg != 'stopp'):
    data = client.recv(1024)
    print("\n"+data.decode(encoding))

    msg = input() #Les inn beskjed fra brukeren
    client.send(bytes(msg,encoding)) #Sender data til robotstudio
client.close()
