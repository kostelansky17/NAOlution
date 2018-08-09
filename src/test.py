import sys
from naoqi import ALProxy
import argparse
import time
import random


if __name__ == "__main__":
	naoIP = '127.0.0.1'
	naoPort = 5000

	motionProxy = ALProxy("ALMotion",naoIP, naoPort)
	postureProxy = ALProxy("ALRobotPosture", naoIP, naoPort)

	postureProxy.goToPosture("StandInit", 0.5)

	time.sleep(5)
	print("MOVE---------------")
	motionProxy.moveInit()

	motionProxy.moveTo(2, 2, 0.0)
	print("DONE________________")
	while True:
		try:
			time.sleep(0.5)
		except KeyboardInterrupt:
			motionProxy.stopMove()
			motionProxy.rest()
			sys.exit(0) 	