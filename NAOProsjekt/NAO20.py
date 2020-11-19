
import sys
sys.path.append("C:\Users\Legendary\Documents\ELVE3610\Prosjekt\pynaoqi-python2.7-2.8.6.23\pynaoqi-python2.7-2.8.6.23-win64-vs2015-20191127_152649\lib")
from naoqi import ALProxy

naoIP = #"192.168.12.62"
PORT = 9559

def setupNAO(name):
    proxy = ALProxy(name,naoIP,PORT)
    return proxy

snakke = setupNAO("ALTextToSpeech")
move = setupNAO("ALMotion")
positur = setupNAO("ALRobotPosture")

snakke.say("Hello. Do you want to play?")
#Sett inn voice recognition
'''
move.post.moveTo(0.5,-0.12,-0.28) #.post gjor at man kan gjore flere ting samtidig
#move.moveToward(1,0,0)
snakke.say("I am walking one meter")
move.waitUntilMoveIsFinished()
snakke.say("Done walking")
positur.goToPosture("Sit",1.0)
'''

print(move.__dict__) #hva move objektet inneholder
#print(dir(move))