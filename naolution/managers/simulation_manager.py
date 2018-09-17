import sys
from naolution import vrep
from naolution.utils.checker import check_client_ID, check_return_code

simx_opmode_blocking = 0x010000


"""
Starts connection to V-REP server

@param adress: string
@param port: int

@return client_ID: int
"""
def start_connection(adress, port):
    client_ID = vrep.simxStart(adress, port, True, True, 5000, 5)

    if not check_client_ID(client_ID):
        sys.exit()

    return client_ID

"""
Starts V-REP simulation

@param client_ID: int
"""
def start_simulation(client_ID):
    return_code = vrep.simxStartSimulation(client_ID, simx_opmode_blocking)

    if not check_return_code(return_code, "simxStartSimulation"):
        sys.exit()


"""
Stops V-REP simulation. Resets simulation to beginning

@param client_ID: int
"""
def stop_simulation(client_ID):
    return_code = vrep.simxStopSimulation(client_ID, simx_opmode_blocking)

    if not check_return_code(return_code, "simxStartSimulation"):
        sys.exit()


"""
Stops connection to V-REP server

@param client_ID: int
"""
def stop_connection(client_ID):
    vrep.simxFinish(client_ID)


"""
Loads V-REP scene

@param client_ID: int
"""
def load_scene(client_ID, scene):
    return_code = vrep.simxLoadScene(client_ID, scene, 0xFF,vrep.simx_opmode_blocking)


"""
Closes V-REP scene

@param client_ID: int
"""
def close_scene(client_ID):
    return_code = vrep.simxCloseScene(client_ID, vrep.simx_opmode_blocking)


"""
Gets vision sensor image, mode buffer

@param client_ID: int
@vision_handle: vision sensor handle

@return resolution: image resolution
@return sensor_img: image
"""
def get_vision_sensor_image_str(client_ID, vision_handle):
    return_code, resolution, sensor_img = vrep.simxGetVisionSensorImage(client_ID, vision_handle, 0, 
                                                                        vrep.simx_opmode_streaming)
  
    return resolution, sensor_img


"""
Gets vision sensor image, mode buffer

@param client_ID: int
@vision_handle: vision sensor handle

@return resolution: image resolution
@return sensor_img: image
"""
def get_vision_sensor_image_buff(client_ID, vision_handle):
    return_code, resolution, sensor_img = vrep.simxGetVisionSensorImage(client_ID, vision_handle, 0, 
                                                                        vrep.simx_opmode_buffer)
    return resolution, sensor_img
