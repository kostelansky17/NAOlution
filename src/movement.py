from naoqi import ALProxy


"""
Class able to do selected NAOqi functions
"""
class Movement():
    """
    Creates proxy
    
    @param adress: String (Choreographe IP)
    @param port: int (Choreographe port)
    """
    def __init__(self, adress, port):
        self.address = adress
        self.port = port
        self.motion_proxy = ALProxy("ALMotion",self.address, self.port)
        self.posture_proxy = ALProxy("ALRobotPosture", self.address, self.port)               

    """
    Initializes motion proxy
    """
    def move_init(self):
        self.motion_proxy.moveInit()

    """
    Moves with NAO in diection
    x, y in range(-1,1)

    @param x: float (dirextion in x axis - forward(positive float) or backwards(negative float) )
    @param y: float (dirextion in x axis - left(positive float) or rigt(negative float) )
    @param spin: floar (spin in radians)
    """
    def move(self, x, y, spin):
        self.motion_proxy.move(x, y, spin)

    """
    Moves with NAO to position
    x, y distance in meters
    
    @param x: float (distance in x axis - forward(positive float) or backwards(negative float) )
    @param y: float (distance in x axis - left(positive float) or rigt(negative float) )
    @param spin: floar (spin in radians)
    """
    def moveTo(self, x, y, spin):
        self.motion_proxy.moveTo(x, y, spin)

    """
    Moves with Stands to position "StandInit"

    @param speed: speed of movement
    """
    def standInit(self, speed):
        self.posture_proxy.goToPosture("StandInit", speed)

    def standZero(self, speed):
        self.posture_proxy.goToPosture("StandZero",speed)
        