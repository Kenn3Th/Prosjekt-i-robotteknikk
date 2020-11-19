import sys
sys.path.append("C:\Users\Legendary\Documents\ELVE3610\Prosjekt\pynaoqi-python2.7-2.8.6.23\pynaoqi-python2.7-2.8.6.23-win64-vs2015-20191127_152649\lib")
from naoqi import ALProxy

naoIP = "192.168.12.62"
PORT = 9559

def setupNAO(name):
    proxy = ALProxy(name,naoIP,PORT)
    return proxy