import sys
#from naoqi import ALProxy
import argparse
import time
import vrep
from PIL import Image as I
import array
from time import sleep

class Movement():
    def __init__(self, adress, port):
        self.address = '127.0.0.1'
        self.port = 5000
        #self.motion_proxy = ALProxy("ALMotion",self.address, self.port)
        #self.posture_proxy = ALProxy("ALRobotPosture", self.address, self.port)          
        print('---Movement successfully created---')        

    def move_init(self):
        self.motion_proxy.moveInit()
        print('---Movement initialized---')  

    def move(self, x, y, spin):
        self.motion_proxy.move(x, y, spin)

    def moveTo(self, x, y, spin):
        print('---MOVETO initialized---')  
        self.motion_proxy.moveTo(x, y, spin)

    def standInit(self, speed):
        self.posture_proxy.goToPosture("StandInit", speed)