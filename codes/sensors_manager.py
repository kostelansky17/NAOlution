import vrep
import sys

class Vrep_object():
	def __init__(self, link, tag):
		self.link = link
		self.tag = tag

	def _get_object_handler(component_tag, simx_opmode_blocking):
		errors, handler = vrep.simxGetObjectHandle(self.link, 
												   str(component_tag),
            									   simx_opmode_blocking)
		#TODO add erors to log

		return handler

	def get_orientation():
		handler = vrep.simxGetObjectHandle(self.link, "NAO", 0x01000)
		errors, orientation = vrep.simxGetObjectOrientation(self.link, handler, 
															-1,
                                                  			simx_opmode_streaming)
		return orientation

if __name__ == "__main__":
	link = vrep.simxStart('127.0.0.2',19999,True,True,5000,5)
	
	print("Connection successful") if link == -1


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
