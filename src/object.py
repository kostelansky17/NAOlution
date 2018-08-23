import sys
import vrep
from checker import check_return_code

simx_opmode_blocking = 0x010000
    
"""
Get position of selected component

@param client_ID: int
@param handle: Object handel (ref. to get_object_handle)

@return position: list (list of floats)
"""
def get_position(client_ID, handle):
    return_code, position = vrep.simxGetObjectPosition(client_ID, handle, 
                                                       -1, simx_opmode_blocking)
    
    if check_return_code(return_code, "get_position"):
        return position

    sys.exit()


"""
Get orietation of selected component

@param client_ID: int
@param component_tag: String

@return position: list (list of floats)
"""
def get_orientation(client_ID, handle):
    return_code, orientation = vrep.simxGetObjectOrientation(client_ID, handle,
                                                             -1, simx_opmode_blocking)
    
    if check_return_code(return_code, "get_orientation"):
        return orientation
    
    sys.exit()       


"""
Get object handle

@param client_ID: int
@param component_tag: String

@return handle
"""
def get_object_handle(client_ID, component_tag):
    return_code, handle = vrep.simxGetObjectHandle(client_ID, component_tag, 
                                                                 vrep.simx_opmode_blocking)

    if check_return_code(return_code, "get_object_handle"):
        return handle

    sys.exit()


"""
Get object handle

@param client_ID: int
@param vision_tag: String

@return handle
"""
def get_vison_sensor_handle(client_ID, vision_tag):
    return_code, handle = vrep.simxGetObjectHandle(client_ID, vision_tag, 
                                                                 vrep.simx_opmode_oneshot_wait)

    if check_return_code(return_code, "get_object_handle"):
        return handle

    sys.exit()
