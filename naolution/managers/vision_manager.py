from naolution.vrep import vrep
import time
import sys
import array
import numpy as np
from PIL import Image as pil_image
from keras.preprocessing import image as keras_image
from naolution.utils.cnn import create_cnn, preprocess_img_from_path
from naolution.utils.checker import check_return_code, check_client_ID


"""
Retrieves image from selected vision sensor.

@param vision_sensor_name: String
@param client_ID: int

@return img: Image
"""
def retrive_img_from_vision_senzor(vision_sensor_name, client_ID):
    return_code, vision_sensor_handle = vrep.simxGetObjectHandle(client_ID, vision_sensor_name, 
                                                                 vrep.simx_opmode_oneshot_wait)
   
    if not check_return_code(return_code,"get_object_handle"):
        sys.exit()

    return_code, resolution, sensor_img = vrep.simxGetVisionSensorImage(client_ID, vision_sensor_handle,
                                                                        0, vrep.simx_opmode_streaming)
    
    time.sleep(1) #mandatory sleep, WON'T WORK without it
    
    return_code, resolution, sensor_img = vrep.simxGetVisionSensorImage(client_ID, vision_sensor_handle,
                                                                        0, vrep.simx_opmode_buffer)
    
    image_byte_array = array.array('b',sensor_img)
    img = pil_image.frombuffer("RGB", (resolution[0],resolution[1]), 
                               image_byte_array, "raw", "RGB", 0, 1)

    return img


"""
Preprocess input from vision sensor to CNN input format definded in cnn.py.

@param img: Image (output of function retrive_img_from_vision_senzor)

@return image preprocess to needed format
"""
def preprocess_sensor_output(img):
    rotated_img = img.rotate(180)
    resized_img = rotated_img.resize(((128,128)))
    grayscale_img = resized_img.convert('L')
    array_img = keras_image.img_to_array(grayscale_img)
    img = np.expand_dims(array_img, axis=0)

    return img


def sensor_output_to_model_input(resolution, sensor_img):
    image_byte_array = array.array('b',sensor_img)
    img = pil_image.frombuffer("RGB", (resolution[0],resolution[1]), 
                               image_byte_array, "raw", "RGB", 0, 1)
    rotated_img = img.rotate(180)
    resized_img = rotated_img.resize(((128,128)))
    grayscale_img = resized_img.convert('L')
    array_img = keras_image.img_to_array(grayscale_img)
    img = np.expand_dims(array_img, axis=0)

    return img


def rescale_model_output(output):
    rescaled = []
    rescaled.append(output[0])
    rescaled.append(output[1])

    return rescaled
        

"""
Functionality testing created while developent
"""
if __name__ == '__main__':
    vrep.simxFinish(-1)
    client_ID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
    
    if check_client_ID(client_ID):
        img = retrive_img_from_vision_senzor('NAO_vision1',client_ID)
        img = preprocess_sensor_output(img)

        model = create_cnn()     
        pred = model.predict(img)
        print(pred)
    