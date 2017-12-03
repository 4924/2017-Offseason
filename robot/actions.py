class Drive:
    def _init_(self, drive):
        """Construct an instance of a Drive.

        :type  drive: wpilib.RobotDrive
        :param drive: The drive base to use.
        """
        self.drive = drive
        self.x = 0
        self.y = 0

    def move(self, x, y):
        """Set the movement for the robot.

        :type  x: int
        :param x: The x value to move.
        :type  y: int
        :param y: The x value to move.
        """
        self.x = x
        self.y = y

    def update(self):
        """Update the motors.
        """
        self.drive.arcadeDrive(self.x,self.y)


class Mandible:
    def _init_(self, gearMotor, switch1, switch2, speed=.5, opening=False):
        self.gearMotor = gearMotor
        self.switch1 = switch1
        self.switch2 = switch2
        self.opening = opening
        self.speed = speed
        self.closepos = opening
    def open(self):
        self.opening = not self.closepos
        
    def close(self):
        self.opening = not self.closepos
        
    def status(self):
        return self.opening
        
    def update(self):
        if self.opening == False and self.switch1.get()== False:
            self.gearMotor.set(0)
        elif self.opening == False and self.switch1.get():
            self.gearMotor.set(self.speed)
        elif self.opening and self.switch2.get()== False:
            self.gearMotor.set(0)
        elif self.opening and self.switch2.get():
            self.gearMotor.set(-self.speed)

        

class Climber:
    def _init_(self, motor):
        self.motor = motor
        self.z = 0

    def move(self, z):
         self.z  = z
         
    def update(self):
        self.motor.set(z)

class Dump:
    def _init_(self, relay, closedSwitch, openSwitch, openDir=True, defaultSwitch1=True, defaultSwitch2=True):
        self.switch1 = closedSwitch
        self.switch2 = openSwitch
        self.relay = relay
        self.openDir = openDir
        self.defaultSwitch1 = defaultSwitch1
        self.defaultSwitch2 = defalutSwitch2
        self.x = 0
        
    def open(self):
        self.x = 1
        
    def close(self):
        self.x = 0
        
    def update(self, switch1, switch2, relay):
        if self.x = 0 and self.switch1 != self.defaultSwitch1:
            self.relay.set(0)
        elif self.x = 0 and self.switch1 == self.defaultSwitch1:
            if openDir == True:
                self.relay.set(3)
            else:
                self.relay.set(2)
        elif self.x = 1 and self.switch2 != self.defaultSwitch2:
            self.relay.set(0)
        elif self.x = 1 and self.switch2 == self.defaultSwitch2:
            if openDir = False
                self.relay.set(2)
            else:
                self.relay.set(3)
            
    def status(self): #0 means mandible is closed, 1 means madible is opened, 2 means mandible is closing, 3 means mandible is opening
        if self.switch1 == self.defaultSwitch1 and self.x == 1:
            return 3
        elif self.switch1 != self.defaultSwitch1 and self.x == 1:
            return 1
        elif self.switch2 == self.defaultSwitch2 and self.x == 0:
            return 2
        elif self.switch2 !=  self.defaultSwitch2 and self.x == 0:
            return 0   n 
            
