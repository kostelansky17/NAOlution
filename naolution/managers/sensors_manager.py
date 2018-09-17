from naolution import vrep
import sys

def _get_object_handler(component_tag, simx_opmode_blocking):
	errors, handler = vrep.simxGetObjectHandle(link, str(component_tag), simx_opmode_blocking)

	return handler

def get_orientation():
	handler = vrep.simxGetObjectHandle(link, "NAO", 0x01000)
	errors, orientation = vrep.simxGetObjectOrientation(link, handler, -1, simx_opmode_streaming)
	return orientation

if __name__ == "__main__":
	link = vrep.simxStart('127.0.0.2',19999,True,True,5000,5)
	
	if link == -1:
		print("Connection successful")


	handler = None
	component_tag = "N"
	simx_opmode_blocking = 0x010000
	simx_opmode_streaming = 0x020000
	simx_opmode_buffer = 0x060000
	errors, handler = vrep.simxGetObjectHandle(link, str(component_tag), simx_opmode_blocking)
	errors, o = vrep.simxGetObjectPosition(link, handler, -1, simx_opmode_blocking)
	print(errors)
	print(o)

	errors, o = vrep.simxGetObjectPosition(link, handler, -1, simx_opmode_blocking)
	print(errors)
	print(o)

	errors, o = vrep.simxGetObjectPosition(link, handler, -1, simx_opmode_blocking)
	print(errors)
	print(o)
	sys.exit(0)
