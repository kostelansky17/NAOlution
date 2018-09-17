from naolution import vrep
from naolution.consts import VREP_IP_1, VREP_PORT_1, NAOQI_BIN_IP, NAOQI_BIN_PORT
import sys
from naolution.managers import simulation_manager as simulation
from naoqi import ALProxy
from naolution.utils.checker import check_client_ID


"""
Streams moving of NAO's joints from Choreographe to V-REP

@param client_id: int
@param motion_proxy: ALProxy("ALMotion",nao_IP, nao_port)
@param body: NAO's body created by create_body()
"""
def joints_control(client_ID, motion_proxy, body):
    while( True ):
        try:
            if( vrep.simxGetConnectionId(client_ID) == -1 ):
                vrep.simxFinish(client_ID)
                client_ID = vrep.simxStart(VREP_IP_1, VREP_PORT_1, True, True, 5000, 5)
                get_first_handles(client_ID, body)
            else:
                #Getting joint's angles from Choregraphe
                commandAngles = motion_proxy.getAngles('Body', False)
                #Head
                vrep.simxSetJointTargetPosition(client_ID, body[0][0], commandAngles[0], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[1][0], commandAngles[1], vrep.simx_opmode_streaming)
                #Left Leg
                vrep.simxSetJointTargetPosition(client_ID, body[2][0], commandAngles[8], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[3][0], commandAngles[9], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[4][0], commandAngles[10], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[5][0], commandAngles[11], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[6][0], commandAngles[12], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[7][0], commandAngles[13], vrep.simx_opmode_streaming)
                #Right Leg
                vrep.simxSetJointTargetPosition(client_ID, body[8][0], commandAngles[14], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[9][0], commandAngles[15], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[10][0], commandAngles[16], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[11][0], commandAngles[17], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[12][0], commandAngles[18], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[13][0], commandAngles[19], vrep.simx_opmode_streaming)
                #Left Arm
                vrep.simxSetJointTargetPosition(client_ID, body[14][0], commandAngles[2], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[15][0], commandAngles[3], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[16][0], commandAngles[4], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[17][0], commandAngles[5], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[18][0], commandAngles[6], vrep.simx_opmode_streaming)
                #Right Arm
                vrep.simxSetJointTargetPosition(client_ID, body[19][0], commandAngles[20], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[20][0], commandAngles[21], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[21][0], commandAngles[22], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[22][0], commandAngles[23], vrep.simx_opmode_streaming)
                vrep.simxSetJointTargetPosition(client_ID, body[23][0], commandAngles[24], vrep.simx_opmode_streaming)
        except KeyboardInterrupt:
            vrep.simxFinish(client_ID)
            break

"""
Streams moving of NAO's joints from Choreographe to V-REP

@param client_id: int
@param body: NAO's body created by create_body()
"""
def get_first_handles(client_ID, body):    
    #Head
    body[0].append(vrep.simxGetObjectHandle(client_ID, 'HeadYaw#', vrep.simx_opmode_oneshot_wait) [1])
    body[1].append(vrep.simxGetObjectHandle(client_ID, 'HeadPitch#', vrep.simx_opmode_oneshot_wait) [1])
    #Left Leg
    body[2].append(vrep.simxGetObjectHandle(client_ID, 'LHipYawPitch3#', vrep.simx_opmode_oneshot_wait) [1])
    body[3].append(vrep.simxGetObjectHandle(client_ID, 'LHipRoll3#', vrep.simx_opmode_oneshot_wait) [1])
    body[4].append(vrep.simxGetObjectHandle(client_ID, 'LHipPitch3#', vrep.simx_opmode_oneshot_wait) [1])
    body[5].append(vrep.simxGetObjectHandle(client_ID, 'LKneePitch3#', vrep.simx_opmode_oneshot_wait) [1])
    body[6].append(vrep.simxGetObjectHandle(client_ID, 'LAnklePitch3#', vrep.simx_opmode_oneshot_wait) [1])
    body[7].append(vrep.simxGetObjectHandle(client_ID, 'LAnkleRoll3#', vrep.simx_opmode_oneshot_wait) [1])
    #Right Leg
    body[8].append(vrep.simxGetObjectHandle(client_ID, 'RHipYawPitch3#', vrep.simx_opmode_oneshot_wait) [1])
    body[9].append(vrep.simxGetObjectHandle(client_ID, 'RHipRoll3#', vrep.simx_opmode_oneshot_wait) [1])
    body[10].append(vrep.simxGetObjectHandle(client_ID, 'RHipPitch3#', vrep.simx_opmode_oneshot_wait) [1])
    body[11].append(vrep.simxGetObjectHandle(client_ID, 'RKneePitch3#', vrep.simx_opmode_oneshot_wait) [1])
    body[12].append(vrep.simxGetObjectHandle(client_ID, 'RAnklePitch3#', vrep.simx_opmode_oneshot_wait) [1])
    body[13].append(vrep.simxGetObjectHandle(client_ID, 'RAnkleRoll3#', vrep.simx_opmode_oneshot_wait) [1])
    #Left Arm
    body[14].append(vrep.simxGetObjectHandle(client_ID, 'LShoulderPitch3#', vrep.simx_opmode_oneshot_wait) [1])
    body[15].append(vrep.simxGetObjectHandle(client_ID, 'LShoulderRoll3#', vrep.simx_opmode_oneshot_wait) [1])
    body[16].append(vrep.simxGetObjectHandle(client_ID, 'LElbowYaw3#', vrep.simx_opmode_oneshot_wait) [1])
    body[17].append(vrep.simxGetObjectHandle(client_ID, 'LElbowRoll3#', vrep.simx_opmode_oneshot_wait) [1])
    body[18].append(vrep.simxGetObjectHandle(client_ID, 'LWristYaw3#', vrep.simx_opmode_oneshot_wait) [1])
    #Right Arm
    body[19].append(vrep.simxGetObjectHandle(client_ID, 'RShoulderPitch3#', vrep.simx_opmode_oneshot_wait) [1])
    body[20].append(vrep.simxGetObjectHandle(client_ID, 'RShoulderRoll3#', vrep.simx_opmode_oneshot_wait) [1])
    body[21].append(vrep.simxGetObjectHandle(client_ID, 'RElbowYaw3#', vrep.simx_opmode_oneshot_wait) [1])
    body[22].append(vrep.simxGetObjectHandle(client_ID, 'RElbowRoll3#', vrep.simx_opmode_oneshot_wait) [1])
    body[23].append(vrep.simxGetObjectHandle(client_ID, 'RWristYaw3#', vrep.simx_opmode_oneshot_wait) [1])

"""
Creates body composing from NAO's joints

@return body
"""
def create_body():
    #Head 
    Head_Yaw=[];Head_Pitch=[]
    #Left Leg
    L_Hip_Yaw_Pitch=[]; L_Hip_Roll=[]; L_Hip_Pitch=[]; L_Knee_Pitch=[]; L_Ankle_Pitch=[]; L_Ankle_Roll=[]
    #Right Leg
    R_Hip_Yaw_Pitch=[]; R_Hip_Roll=[] ;R_Hip_Pitch=[] ;R_Knee_Pitch=[]; R_Ankle_Pitch=[]; R_Ankle_Roll=[]
    #Left Arm     
    L_Shoulder_Pitch=[]; L_Shoulder_Roll=[]; L_Elbow_Yaw=[]; L_Elbow_Roll=[]; L_Wrist_Yaw=[]
    #Right Arm     
    R_Shoulder_Pitch=[]; R_Shoulder_Roll=[]; R_Elbow_Yaw=[]; R_Elbow_Roll=[]; R_Wrist_Yaw=[]
    
    R_H=[]; L_H=[]; R_Hand=[]; L_Hand=[]
    
    return [Head_Yaw, Head_Pitch,
            L_Hip_Yaw_Pitch, L_Hip_Roll, L_Hip_Pitch, L_Knee_Pitch, L_Ankle_Pitch, L_Ankle_Roll,
            R_Hip_Yaw_Pitch, R_Hip_Roll, R_Hip_Pitch, R_Knee_Pitch, R_Ankle_Pitch, R_Ankle_Roll,
            L_Shoulder_Pitch, L_Shoulder_Roll, L_Elbow_Yaw, L_Elbow_Roll, L_Wrist_Yaw,
            R_Shoulder_Pitch, R_Shoulder_Roll, R_Elbow_Yaw, R_Elbow_Roll, R_Wrist_Yaw,
            L_H, L_Hand, R_H, R_Hand]


"""
Connects to V-REP and starts connection between Choreographe and V-REP
"""
if __name__ == "__main__":
    vrep.simxFinish(-1)
    client_ID = simulation.start_connection(VREP_IP_1, VREP_PORT_1)

    motion_proxy = ALProxy("ALMotion", NAOQI_BIN_IP, NAOQI_BIN_PORT)
    posture_proxy = ALProxy("ALRobotPosture", NAOQI_BIN_IP, NAOQI_BIN_PORT)

    posture_proxy.goToPosture("StandZero",1.0)

    body = create_body()
    get_first_handles(client_ID, body)
    
    print("Joints manager is ready.")
    joints_control(client_ID,motion_proxy,body)
    print("End of the simulation.")
