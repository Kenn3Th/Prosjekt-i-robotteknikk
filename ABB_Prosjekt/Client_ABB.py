#!/usr/bin/env python
# -*- coding: utf-8 -*-
from center_contour import*
import socket

#-------- Kamera settings --------#
# Initialiserer opploesningen til kameraet
frameWidth = 1920    
frameHight = 1080
FPS = 1 # Frames Per Second
cap = cv2.VideoCapture(2) # Starter kameraet fra COM port 2
cap.set(3, frameWidth)
cap.set(4, frameHight)
cap.set(5, FPS)
#-------- Socket programmering --------#
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_IP = '192.168.12.97'
port = 2222
encoding = 'utf-8' # Definerer hvilket bibliotek den skal bruke for tolking av beskjeden

client.connect((HOST_IP,port)) # Socket oppkobling

print(f"Fått tilgang til {HOST_IP}") # Verifiserer at den har tilgang til verten
    
while True: 
    data = client.recv(1024) #Definerer at vi kan motta 1024bit.
    print("\n"+data.decode(encoding))
    motatt = data.decode(encoding) 
    msg = ""

    if motatt == "Feed me!" or motatt == "Feed me!Feed me!":
        msg = imageProcess()
        if msg == "":
            msg = imageProcess()
        
        client.send(bytes(msg, encoding))
        print(f"beskjed sendt = {msg}")

client.close()
