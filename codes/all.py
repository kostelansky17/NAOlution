import sys
#from naoqi import ALProxy
import argparse
import time
import vrep

class ConnectionManager():
    def __init__(self, address, port):
        self.address = '127.0.0.2'
        self.port = 19999
        vrep.simxFinish(-1)
        self.client_ID= vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
        if self.client_ID == -1:
            print("Connection unsuccessfull.")
            sys.exit()

class ProxyManager():
    def __init__(self, address, port):
        self.address = '127.0.0.1'
        self.port = 5000
        #self.motion_proxy = ALProxy("ALMotion",self.address, self.port)
        #self.posture_proxy = ALProxy("ALRobotPosture", self.address, self.port)     

class Movement():
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        print('---Movement successfully created---')        

    def move_init(self):
        self.proxy_manager.motion_proxy.moveInit()
        print('---Movement initialized---')  

    def move(self, x, y, spin):
        self.proxy_manager.motion_proxy.move(x, y, spin)

    def moveTo(self, x, y, spin):
        print('---MOVETO initialized---')  
        self.proxy_manager.motion_proxy.moveTo(x, y, spin)

    def standInit(self, speed):
        self.proxy_manager.posture_proxy.goToPosture("StandInit", speed)

class ObjectManager():
    def __init__(self, connection_manager, component_tag):
        self.connection_manager = connection_manager
        self.simx_opmode_blocking = 0x010000
        self.component_tag = component_tag
        self.handler = self._create_handler()

    def _check_errors(errors,fce_name):
        if errors != 0:
            print(fce_name + " returned code " + str(errors))
            return False
        return True    

    def _create_handler(self):
        errors, handler = vrep.simxGetObjectHandle(self.connection_manager.client_ID, str(self.component_tag), self.simx_opmode_blocking)
        if self._check_errors("_create_handeler", errors):        
            return handler
        
        sys.exit()
    
    def get_position(self):
        errors, position = vrep.simxGetObjectPosition(self.connection_manager.client_ID, self.handler, -1, self.simx_opmode_blocking)
        if self._check_errors("get_position", errors):
            return position

        sys.exit()

    def get_orientation(self):
        errors, orientation = vrep.simxGetObjectOrientation(self.connection_manager.client_ID, self.handler, -1, self.simx_opmode_blocking)
        if self._check_errors("get_orientation", errors):
            return orientation
        
        sys.exit()       

    def set_position(self,position):
        errors, position = vrep.sixSetObjectPosition(self.connection_manager.client_ID, self.handler, -1, position, self.simx_opmode_blocking)
        if self._check_errors("set_position", errors):
            return position
        
        sys.exit()
    
    def set_orientation(self, orientation):
        errors, orientation = vrep.simxSetObjectOrientation(self.connection_manager.client_ID, self.handler, -1, orientation, self.simx_opmode_blocking)
        if self._check_errors("set_orientation", errors):
            return orientation

        sys.exit()

if __name__ == "__main__":
    naoIP = '127.0.0.1'
    naoPort = 5000
    connection_manager = ConnectionManager(naoIP, naoPort)
    #proxy_manager = ProxyManager(naoIP,naoPort)
    #movement = Movement(proxy_manager)
    object_manager = ObjectManager(connection_manager,"NAO")
    
    #movement.move_init()    
    print(object_manager.get_position())
    #movement.moveTo(1,0,0)
    print(object_manager.get_position())
    