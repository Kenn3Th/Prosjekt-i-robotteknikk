import sys
PATH = 'path/to/NAO/library'
sys.path.append(PATH)
from naoqi import ALProxy

naoIP = "127.0.0.0"
PORT = 9559

def setupNAO(name):
    proxy = ALProxy(name,naoIP,PORT)
    return proxy
