import vrep
import sys
from naoqi import ALProxy

#Moves with NAO's joints in the simulation
def JointControl(clientID,motionProxy,i,Body):
    while(vrep.simxGetConnectionId(clientID)!=-1):
        #Getting joint's angles from Choregraphe (please check your robot's IP)
        commandAngles = motionProxy.getAngles('Body', False)
        #Head
        vrep.simxSetJointTargetPosition(clientID,Body[0][i],commandAngles[0],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[1][i],commandAngles[1],vrep.simx_opmode_streaming)
        #Left Leg
        vrep.simxSetJointTargetPosition(clientID,Body[2][i],commandAngles[8],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[3][i],commandAngles[9],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[4][i],commandAngles[10],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[5][i],commandAngles[11],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[6][i],commandAngles[12],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[7][i],commandAngles[13],vrep.simx_opmode_streaming)
        #Right Leg
        vrep.simxSetJointTargetPosition(clientID,Body[8][i],commandAngles[14],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[9][i],commandAngles[15],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[10][i],commandAngles[16],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[11][i],commandAngles[17],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[12][i],commandAngles[18],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[13][i],commandAngles[19],vrep.simx_opmode_streaming)
        #Left Arm
        vrep.simxSetJointTargetPosition(clientID,Body[14][i],commandAngles[2],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[15][i],commandAngles[3],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[16][i],commandAngles[4],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[17][i],commandAngles[5],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[18][i],commandAngles[6],vrep.simx_opmode_streaming)
        #Right Arm
        vrep.simxSetJointTargetPosition(clientID,Body[19][i],commandAngles[20],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[20][i],commandAngles[21],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[21][i],commandAngles[22],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[22][i],commandAngles[23],vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetPosition(clientID,Body[23][i],commandAngles[24],vrep.simx_opmode_streaming)


#Get the Handle of only one NAO
def get_first_handles(clientID,Body):    
    #Head
    Body[0].append(vrep.simxGetObjectHandle(clientID,'HeadYaw#',vrep.simx_opmode_oneshot_wait)[1])
    Body[1].append(vrep.simxGetObjectHandle(clientID,'HeadPitch#',vrep.simx_opmode_oneshot_wait)[1])
    #Left Leg
    Body[2].append(vrep.simxGetObjectHandle(clientID,'LHipYawPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[3].append(vrep.simxGetObjectHandle(clientID,'LHipRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[4].append(vrep.simxGetObjectHandle(clientID,'LHipPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[5].append(vrep.simxGetObjectHandle(clientID,'LKneePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[6].append(vrep.simxGetObjectHandle(clientID,'LAnklePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[7].append(vrep.simxGetObjectHandle(clientID,'LAnkleRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    #Right Leg
    Body[8].append(vrep.simxGetObjectHandle(clientID,'RHipYawPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[9].append(vrep.simxGetObjectHandle(clientID,'RHipRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[10].append(vrep.simxGetObjectHandle(clientID,'RHipPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[11].append(vrep.simxGetObjectHandle(clientID,'RKneePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[12].append(vrep.simxGetObjectHandle(clientID,'RAnklePitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[13].append(vrep.simxGetObjectHandle(clientID,'RAnkleRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    #Left Arm
    Body[14].append(vrep.simxGetObjectHandle(clientID,'LShoulderPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[15].append(vrep.simxGetObjectHandle(clientID,'LShoulderRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[16].append(vrep.simxGetObjectHandle(clientID,'LElbowYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[17].append(vrep.simxGetObjectHandle(clientID,'LElbowRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[18].append(vrep.simxGetObjectHandle(clientID,'LWristYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    #Right Arm
    Body[19].append(vrep.simxGetObjectHandle(clientID,'RShoulderPitch3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[20].append(vrep.simxGetObjectHandle(clientID,'RShoulderRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[21].append(vrep.simxGetObjectHandle(clientID,'RElbowYaw3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[22].append(vrep.simxGetObjectHandle(clientID,'RElbowRoll3#',vrep.simx_opmode_oneshot_wait)[1])
    Body[23].append(vrep.simxGetObjectHandle(clientID,'RWristYaw3#',vrep.simx_opmode_oneshot_wait)[1])


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
    clientID=vrep.simxStart('127.0.0.2',19999,True,True,5000,5)
    if clientID == -1:
        print('Connection non successful')
        sys.exit('Could not connect')
    else:
        print("Connection successful")

    naoIP = '127.0.0.1'
    naoPort= 5000

    motionProxy = ALProxy("ALMotion",naoIP, naoPort)
    postureProxy = ALProxy("ALRobotPosture", naoIP, naoPort)

    #Go to the posture StandInitZero
    posture = 'StandZero'
    postureProxy.goToPosture(posture,1.0)

    
    Body = create_body()

    get_first_handles(clientID,Body)
    commandAngles = motionProxy.getAngles('Body', False)
    print('READY TO USE')
    JointControl(clientID,motionProxy,0,Body)

    print('End of simulation')