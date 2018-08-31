import sys
from naoqi import ALProxy
import argparse
import time
import random
import simulation
from movement import Movement
import consts
import vrep

"""
testing file
"""
if __name__ == "__main__":
	mov = Movement(consts.naoqi_bin_ip, consts.naoqi_bin_port)
	
	client_ID = simulation.start_connection(consts.vrep_ip_2, consts.vrep_port_2)
	
	while True:
		try:
			simulation.start_simulation(client_ID)
			
			time.sleep(5)

			mov.move_init()
			mov.moveTo(0.5,0,0)
			mov.move(0,0,0)
			mov.standZero(1)

			simulation.stop_simulation(client_ID)

			time.sleep(1)
		except KeyboardInterrupt:
			break
	#vrep.simxFinish(client_ID)

	

	#client_ID = simulation.start_connection(consts.vrep_ip_2, consts.vrep_port_2)

	vrep.simxFinish(client_ID)

	"""
	client_ID = simulation.start_connection(consts.vrep_ip_2, consts.vrep_port_2)
	simulation.start_simulation(client_ID)

	mov = Movement(consts.naoqi_bin_ip, consts.naoqi_bin_port)
	mov.move_init()
	mov.standInit(0.5)
	time.sleep(1)

	mov.moveTo(0.5,0,0)

	time.sleep(5)

	simulation.stop_simulation(client_ID)
	simulation.start_simulation(client_ID)


	mov.standInit(0.5)
	time.sleep(1)

	mov.moveTo(0.5,0,0)

	time.sleep(5)

	
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

	"""
