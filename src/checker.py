""""
Checks return code of V-rep API functions.

@param retrun_code: int (Code returned by function)
@param fce_name: String (name of the function)

@returns Bool (True if successfull, else False)
"""
def check_return_code(retrun_code, fce_name):
    if retrun_code != 0:
        print(fce_name + " returned code " + str(retrun_code))
        return False
    return True   


"""
Checks client_ID - return code vrep.simxStart()

@param client_ID: int 

@returns Bool (True if successfull, else False)
"""
def check_client_ID(client_ID):
    if client_ID != -1:
        print("Connected to remote V-REP API server.")
    else:
        print("Connection to remote V-REP API server not successfull.")
        return False

    return True