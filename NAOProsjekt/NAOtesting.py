# -*- encoding: UTF-8 -*-

import sys
PATH = "path/to/NAO/library"
sys.path.append(PATH)
import naoqi as nao
from naoqi import ALProxy
import time
import argparse
import NAOconfig

naoIP = "127.0.0.0"
port = 9559
motion = nao.ALProxy("ALMotion", naoIP, port)
stand = nao.ALProxy("ALRobotPosture", naoIP, port)
tts    = nao.ALProxy("ALTextToSpeech", naoIP, port)
videoProxy = nao.ALProxy("ALVideoDevice",naoIP, port)


#Henter bilde
subscriber = videoProxy.subscribeCamera("demo", 0, 3, 13, 1)
imageNao = videoProxy.getImageRemote(subscriber)

motion.moveInit()
try:
    stand.goToPosture("StandInit",0.8)
except (ValueError, RuntimeError):
    pass
'''
count = 0
while(count <6):
    if(count%2 == 0):
        motion.post.moveTo(0.1, 0, 0)
    elif(count%3 == 0): 
        tts.say("Lets play a game!")
    count += 1


#nao.myDisplayImageFunction(imageNao) 
try:
    stand.goToPosture("Sit",1.0)
except (ValueError,RuntimeError):
    pass
'''

def locate_ball():
	headMov = NAOconfig.loadProxy("ALMotion")
	i = 0
	a = [-1.5,0,1.5]
	b = [2.0,4.0,6.0]
	isAbsolute = True
	headMov.stiffnessInterpolation("HeadYaw", 1.0, 1.0)
	targetName = "RedBall"
	diameter = 0.03
	distanceX = 0.03
	distanceY = 0.0
	angleWz = 0.0
	thresholdX = 0.1
	thresholdY = 0.1
	thresholdWz = 1.0
	effector = "None"
	mode = "Move"
	tracker = NAOconfig.loadProxy( "ALTracker" )
	tracker.setEffector(effector)
	tracker.registerTarget(targetName, diameter)
	tracker.setRelativePosition([-distanceX, distanceY, angleWz, thresholdX, thresholdY, thresholdWz])
	tracker.setMode(mode)
	t_end = time.time() + 30
	tracker.track(targetName) 
	for j in range(3):
        headMov.angleInterpolation("HeadPitch", a[j], b[j], isAbsolute)
        for i in range(3):
            headMov.angleInterpolation("HeadYaw", a[i], b[i], isAbsolute)
            i+=1
            if tracker.isTargetLost():
                continue
            else:
                break 
        j += 1

	headMov.angleInterpolation("HeadYaw", 0, 8.0, isAbsolute)
		
	if time.time() == t_end:
		tracker.stopTracker()
	tracker.unregisterTarget(targetName)
	headMov.stiffnessInterpolation("HeadYaw", 0.0, 1.0)

tts.say("Trying to find ball")

tts.say("Try again")
