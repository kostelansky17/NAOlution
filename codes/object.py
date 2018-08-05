import sys
#from naoqi import ALProxy
import argparse
import time
import vrep
from PIL import Image as I
import array
from time import sleep

#from object to unctions?
class ObjectManager():
    def __init__(self, ip, port, component_tag):
        self.client_ID = vrep.simxStart(ip,19999,True,True,port,5)
        self.simx_opmode_blocking = 0x010000
        self.component_tag = component_tag
        self.handle = self._create_handle()

    def _create_handle(self):
        errors, handle = vrep.simxGetObjectHandle(self.client_ID, str(self.component_tag), self.simx_opmode_blocking)
        if check_errors(errors, "create_handeler"):        
            return handle
        
        sys.exit()
    
    def get_position(self):
        errors, position = vrep.simxGetObjectPosition(self.client_ID, self.handle, -1, self.simx_opmode_blocking)
        if check_errors(errors, "get_position"):
            return position

        sys.exit()

    def get_orientation(self):
        errors, orientation = vrep.simxGetObjectOrientation(self.client_ID, self.handle, -1, self.simx_opmode_blocking)
        if check_errors(errors, "get_orientation"):
            return orientation
        
        sys.exit()       

    def set_position(self,position):
        errors, position = vrep.simxSetObjectPosition(self.client_ID, self.handle, -1, position, self.simx_opmode_blocking)
        if check_errors(errors, "set_position"):
            return position
        
        sys.exit()
    
    def set_orientation(self, orientation):
        errors, orientation = vrep.simxSetObjectOrientation(self.client_ID, self.handle, -1, orientation, self.simx_opmode_blocking)
        if check_errors(errors, "set_orientation", ):
            return orientation

        sys.exit()