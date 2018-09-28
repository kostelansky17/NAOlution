from naolution.managers import simulation_manager as simulation
from naolution.managers.movement_manager import Movement
from naolution.managers import object_manager
from naolution.managers import vision_manager as vision
from consts import VREP_IP_2, VREP_PORT_2, NAOQI_BIN_IP, NAOQI_BIN_PORT, \
                   NAO, TARGET, NAO_VISION_1
import time
import numpy as np
from keras import models


SCENE = "../scenes/NAO1.ttt"
TIMEOUT = 40
MODEL_PATH = "../models/model_0.h5"

def evaluate_individual(run_time, distance_from_target):
    return - distance_from_target * 10

def distance_from_taget(nao_position, target_position):
    return np.sqrt((nao_position[0] - target_position[0])**2 +
                    (nao_position[1] - target_position[1])**2)


def stop_simulation(nao_position, target_position, run_time):
    distance = distance_from_taget(nao_position, target_position)
    if run_time > TIMEOUT or distance < 0.8:
        return True
    return False

def run_simulation(model,):
    client_ID = simulation.start_connection(VREP_IP_2, 
                                            VREP_PORT_2)
    movement = Movement(NAOQI_BIN_IP, NAOQI_BIN_PORT)
    simulation.load_scene(client_ID, SCENE)

    simulation.start_simulation(client_ID)
    time.sleep(6)
    
    nao_handle = object_manager.get_object_handle(client_ID, NAO)
    target_handle = object_manager.get_object_handle(client_ID, TARGET)
    vision_handle = object_manager.get_vison_sensor_handle(client_ID, NAO_VISION_1)
    resolution, sensor_img = simulation.get_vision_sensor_image_str(client_ID, vision_handle)

    time.sleep(1) #mandatory sleep, WON'T WORK without it      

    nao_position = object_manager.get_position(client_ID, nao_handle)
    target_position = object_manager.get_position(client_ID, target_handle)

    movement.move_init()     
    movement.standInit(0.5)

    start_time = time.time()
    end_time = time.time()
    while not stop_simulation(nao_position, target_position, end_time - start_time):
        nao_position = object_manager.get_position(client_ID, nao_handle)
        resolution, sensor_img = simulation.get_vision_sensor_image_buff(client_ID, vision_handle)

        model_input = vision.sensor_output_to_model_input(resolution, sensor_img)
        results = model.predict(model_input)

        movement.move(float(results[0][0]), float(results[0][1]), float(results[0][2]))           
        end_time = time.time()

    movement.move(0,0,0)      
    end_time = time.time()
    distance_from_target = distance_from_taget(nao_position, target_position)

    print("TOTAL TIME: " + str(end_time - start_time))
    print("RANK:" + str(evaluate_individual(end_time - start_time, distance_from_target)))

    movement.standZero(1)
    simulation.stop_simulation(client_ID)
    simulation.close_scene(client_ID)


if __name__ == "__main__":
    model = models.load_model(MODEL_PATH)
    run_simulation(model)
