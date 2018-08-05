import vrep
import time
import sys
from error import check_errors

#format, proces strem? 
def getVisionSensor(visionSensorName, client_ID):
    errors, visionSensorHandle=vrep.simxGetObjectHandle(client_ID,visionSensorName,vrep.simx_opmode_oneshot_wait)
    if not check_errors(errors,"get_object_handle"):
        sys.exit()
    errors, resolution, image = vrep.simxGetVisionSensorImage(client_ID,visionSensorHandle,0,vrep.simx_opmode_streaming)
    if not check_errors(errors,"get_vision_sensor_image"):
        sys.exit()
    
    return image
    
if __name__ == '__main__':
    vrep.simxFinish(-1)
    client_ID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
    if clientID!=-1:
        print 'Connected to remote API server'
        getVisionSensor('NAO_vision1',client_ID)

    else:
        print 'Connection non successful'
        sys.exit('Could not connect')