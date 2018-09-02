from movement import Movement
from consts import naoqi_bin_ip, naoqi_bin_port
from naoqi import ALProxy

'''
Before running you need to change naoqi_bin_ip, naoqi_bin_port in consts.py to match your NAOqi API
'''
#approach using class Movement which contains multiple NAOqi API methods
movement = Movement(naoqi_bin_ip, naoqi_bin_port)

movement.move_init()     
movement.standInit(0.5)

movement.move(0.7, 0.3, 0.0)

#approach using dircetly NAOqi API
motion_proxy = ALProxy("ALMotion",naoqi_bin_ip, naoqi_bin_port)
posture_proxy = ALProxy("ALRobotPosture", naoqi_bin_ip, naoqi_bin_port)

motion_proxy.moveInit()
posture_proxy.goToPosture("StandInit", 0.5)

motion_proxy.move(0.7, 0.3, 0.0)