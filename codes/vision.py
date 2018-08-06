import vrep
import time
import sys
from error import check_errors
import matplotlib.pyplot as plt
from PIL import Image as I
import array
from cnn import create_cnn, preprocess_img_from_path
from keras.preprocessing import image
import numpy as np

def retrive_img_from_vision_senzor(vision_sensor_name, client_ID):
    errors, vision_sensor_handle = vrep.simxGetObjectHandle(client_ID, vision_sensor_name, vrep.simx_opmode_oneshot_wait)
    if not check_errors(errors,"get_object_handle"):
        sys.exit()
    errors, resolution, img = vrep.simxGetVisionSensorImage(client_ID, vision_sensor_handle,0,vrep.simx_opmode_streaming)
    
    time.sleep(1)
    
    errors, resolution, img = vrep.simxGetVisionSensorImage(client_ID, vision_sensor_handle,0,vrep.simx_opmode_buffer)
    image_byte_array = array.array('b',img)
    img = I.frombuffer("RGB", (resolution[0],resolution[1]), image_byte_array, "raw", "RGB", 0, 1)

    return img

def preprocess_sensor_output(img):
    img = img.rotate(180)
    img = img.resize(((128,128)))
    img = img.convert('L')
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)

    return img
    
if __name__ == '__main__':
    vrep.simxFinish(-1)
    client_ID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
    if client_ID!=-1:
        print 'Connected to remote API server'
        img = retrive_img_from_vision_senzor('NAO_vision1',client_ID)
        img = preprocess_sensor_output(img)

        model = create_cnn()     
        pred = model.predict(img)
        print(pred)
    else:
        print 'Connection non successful'
        sys.exit('Could not connect')