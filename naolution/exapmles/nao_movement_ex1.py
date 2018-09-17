from naolution.managers.movement_manager import Movement
from naolution.consts import NAOQI_BIN_IP, NAOQI_BIN_PORT
from naoqi import ALProxy

'''
Before running you need to change NAOQI_BIN_IP, NAOQI_BIN_PORT in consts.py to match your NAOqi API

approach using class Movement which contains multiple NAOqi API methods
'''
if __name__ == "__main__":
    movement = Movement(NAOQI_BIN_IP, NAOQI_BIN_PORT)

    movement.move_init()     
    movement.standInit(0.5)

    movement.moveTo(0.7, 0.3, 0.0)
