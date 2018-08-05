import vrep
import sys
from naoqi import ALProxy

#Moves with NAO's joints in the simulation
def JointControl(client_ID,motion_proxy,i,body):
    while(vrep.simxGetConnectionId(client_ID)!=-1):
        #Getting joint's angles from Choregraphe (please check your robot's IP)
        commandAngles = motion_proxy.getAngles('body', False)
        #Head
        vrep.simxSetJointTargetPosition(client_ID,body[0][i],commandAngles[0],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[1][i],commandAngles[1],vrep.simx_opmode_streaming)
        #Left Leg
        vrep.simxSetJointTargetPosition(client_ID,body[2][i],commandAngles[8],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[3][i],commandAngles[9],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[4][i],commandAngles[10],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[5][i],commandAngles[11],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[6][i],commandAngles[12],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[7][i],commandAngles[13],vrep.simx_opmode_streaming)
        #Right Leg
        vrep.simxSetJointTargetPosition(client_ID,body[8][i],commandAngles[14],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[9][i],commandAngles[15],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[10][i],commandAngles[16],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[11][i],commandAngles[17],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[12][i],commandAngles[18],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[13][i],commandAngles[19],vrep.simx_opmode_streaming)
        #Left Arm
        vrep.simxSetJointTargetPosition(client_ID,body[14][i],commandAngles[2],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[15][i],commandAngles[3],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[16][i],commandAngles[4],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[17][i],commandAngles[5],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[18][i],commandAngles[6],vrep.simx_opmode_streaming)
        #Right Arm
        vrep.simxSetJointTargetPosition(client_ID,body[19][i],commandAngles[20],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[20][i],commandAngles[21],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[21][i],commandAngles[22],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[22][i],commandAngles[23],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(client_ID,body[23][i],commandAngles[24],vrep.simx_opmode_streaming)


#Get the Handle of only one NAO
def get_first_handles(client_ID,body):    
    #Head
    body[0].append(vrep.simxGetObjectHandle(client_ID,'HeadYaw#',vrep.simx_opmode_oneshot_wait)[1])
    body[1].append(vrep.simxGetObjectHandle(client_ID,'HeadPitch#',vrep.simx_opmode_oneshot_wait)[1])
    #Left Leg
    body[2].append(vrep.simxGetObjectHandle(client_ID,'LHipYawPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    body[3].append(vrep.simxGetObjectHandle(client_ID,'LHipRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    body[4].append(vrep.simxGetObjectHandle(client_ID,'LHipPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    body[5].append(vrep.simxGetObjectHandle(client_ID,'LKneePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    body[6].append(vrep.simxGetObjectHandle(client_ID,'LAnklePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    body[7].append(vrep.simxGetObjectHandle(client_ID,'LAnkleRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    #Right Leg
    body[8].append(vrep.simxGetObjectHandle(client_ID,'RHipYawPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    body[9].append(vrep.simxGetObjectHandle(client_ID,'RHipRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    body[10].append(vrep.simxGetObjectHandle(client_ID,'RHipPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    body[11].append(vrep.simxGetObjectHandle(client_ID,'RKneePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    body[12].append(vrep.simxGetObjectHandle(client_ID,'RAnklePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    body[13].append(vrep.simxGetObjectHandle(client_ID,'RAnkleRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    #Left Arm
    body[14].append(vrep.simxGetObjectHandle(client_ID,'LShoulderPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    body[15].append(vrep.simxGetObjectHandle(client_ID,'LShoulderRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    body[16].append(vrep.simxGetObjectHandle(client_ID,'LElbowYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    body[17].append(vrep.simxGetObjectHandle(client_ID,'LElbowRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    body[18].append(vrep.simxGetObjectHandle(client_ID,'LWristYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    #Right Arm
    body[19].append(vrep.simxGetObjectHandle(client_ID,'RShoulderPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    body[20].append(vrep.simxGetObjectHandle(client_ID,'RShoulderRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    body[21].append(vrep.simxGetObjectHandle(client_ID,'RElbowYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    body[22].append(vrep.simxGetObjectHandle(client_ID,'RElbowRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    body[23].append(vrep.simxGetObjectHandle(client_ID,'RWristYaw3#',vrep.simx_opmode_oneshot_wait)[1])


def create_body():
    Head_Yaw=[];Head_Pitch=[]
    L_Hip_Yaw_Pitch=[];L_Hip_Roll=[];L_Hip_Pitch=[];L_Knee_Pitch=[];L_Ankle_Pitch=[];L_Ankle_Roll=[]
    R_Hip_Yaw_Pitch=[];R_Hip_Roll=[];R_Hip_Pitch=[];R_Knee_Pitch=[];R_Ankle_Pitch=[];R_Ankle_Roll=[]
    L_Shoulder_Pitch=[];L_Shoulder_Roll=[];L_Elbow_Yaw=[];L_Elbow_Roll=[];L_Wrist_Yaw=[]
    R_Shoulder_Pitch=[];R_Shoulder_Roll=[];R_Elbow_Yaw=[];R_Elbow_Roll=[];R_Wrist_Yaw=[]
    R_H=[];L_H=[];R_Hand=[];L_Hand=[]
    return [Head_Yaw,Head_Pitch,L_Hip_Yaw_Pitch,L_Hip_Roll,L_Hip_Pitch,L_Knee_Pitch,L_Ankle_Pitch,L_Ankle_Roll,R_Hip_Yaw_Pitch,R_Hip_Roll,R_Hip_Pitch,R_Knee_Pitch,R_Ankle_Pitch,R_Ankle_Roll,L_Shoulder_Pitch,L_Shoulder_Roll,L_Elbow_Yaw,L_Elbow_Roll,L_Wrist_Yaw,R_Shoulder_Pitch,R_Shoulder_Roll,R_Elbow_Yaw,R_Elbow_Roll,R_Wrist_Yaw,L_H,L_Hand,R_H,R_Hand]

if __name__ == "__main__":
    vrep.simxFinish(-1)
    client_ID=vrep.simxStart('127.0.0.2',19999,True,True,5000,5)
    if client_ID == -1:
        print('Connection non successful')
        sys.exit('Could not connect')
    else:
        print("Connection successful")

    naoIP = '127.0.0.1'
    naoPort= 5000

    motion_proxy = ALProxy("ALMotion",naoIP, naoPort)
    posture_proxy = ALProxy("ALRobotPosture", naoIP, naoPort)

    posture = 'StandZero'
    posture_proxy.goToPosture(posture,1.0)

    
    body = create_body()

    get_first_handles(client_ID,body)
    print('READY TO USE')
    JointControl(client_ID,motion_proxy,0,body)

    print('End of simulation')