from naolution.consts import NAOQI_BIN_IP, NAOQI_BIN_PORT
from naoqi import ALProxy


'''
Before running you need to change NAOQI_BIN_IP, NAOQI_BIN_PORT in consts.py to match your NAOqi API

Approach using dircetly NAOqi API
'''
if __name__ == "__main__":
    motion_proxy = ALProxy("ALMotion",NAOQI_BIN_IP, NAOQI_BIN_PORT)
    posture_proxy = ALProxy("ALRobotPosture", NAOQI_BIN_IP, NAOQI_BIN_PORT)

    motion_proxy.moveInit()
    posture_proxy.goToPosture("StandInit", 0.5)

    motion_proxy.moveTo(0.7, 0.3, 0.0)
