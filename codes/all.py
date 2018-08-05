import sys
#from naoqi import ALProxy
import argparse
import time
import vrep
from PIL import Image as I
import array
from time import sleep
from vision import getVisionSensor
from cnn import create_cnn, preprocess_img
from keras.preprocessing import image
from error import check_errors

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

def feedCNN(model, deelay, ip, port):
    client_ID = vrep.simxStart(ip,19999,True,True,port,5)
    if not check_errors(client_ID, "Start"):
        sys.exit()
    while vrep.simxGetConnectionId(client_ID) != -1:
        image = getVisionSensor('NAO_vision1',client_ID)
        processed_img = preprocess_img(image)
        prediction = model.predict(preprocess_img)
        print("---PREDICTION---")
        print(prediction)
        time.sleep(deelay)
        #move to prediction simulationusly with running joints manager


if __name__ == "__main__":
    #naoIP = '127.0.0.1'
    #naoPort = 5000
    #connection_manager = ConnectionManager(naoIP, naoPort)
    #proxy_manager = ProxyManager(naoIP,naoPort)
    #movement = Movement(proxy_manager)
    #object_manager = ObjectManager('127.0.0.1',5000,"NAO")
    
    #movement.move_init()    
    #print(object_manager.get_position())
    #movement.moveTo(1,0,0)
    #print(object_manager.get_position())
    #client_ID = vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
    #if client_ID == -1:
    #    print("Connection unsuccessfull.")
    #    sys.exit()
    #object_manager = ObjectManager("NAO")
    #while True:
    #    print(object_manager.get_orientation())
    #    sleep(1)
    #object_manager.set_position((0,0,0))
    client_ID = vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
    #image = getVisionSensor('NAO_vision1',client_ID)
    model = create_cnn()
    feedCNN(model,1,'127.0.0.1',5000)
    #preprocess_and_save_img(client_ID, 'NAO_vision1')



    