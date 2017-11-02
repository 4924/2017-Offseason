class Drive:
    def _init_(drive):
        """Construct an instance of a Drive.

        :type  drive: wpilib.RobotDrive
        :param drive: The drive base to use.
        """
        self.drive = drive
        self.x = 0
        self.y = 0

    def move(x, y):
        """Set the movement for the robot.

        :type  x: int
        :param x: The x value to move.
        :type  y: int
        :param y: The x value to move.
        """
        self.x = x
        self.y = y

    def update():
        """Update the motors.
        """
        self.drive.arcadeDrive(self.x,self.y)


class Mandible:
    def _init_(gearMotor, switch1, switch2, speed=.5, opening=False):
        self.gearMotor = gearMotor
        self.switch1 = switch1
        self.switch2 = switch2
        self.opening = opening
        self.speed = speed
        self.closepos = opening
    def open():
        self.opening = not self.closepos
        
    def close():
        self.opening = not self.closepos
        
    def status():
        return self.opening
        
    def update():
        if self.opening == False and self.switch1.get()== False:
            self.gearMotor.set(0)
        elif self.opening == False and self.switch1.get():
            self.gearMotor.set(self.speed)
        elif self.opening and self.switch2.get()== False:
            self.gearMotor.set(0)
        elif self.opening and self.switch2.get():
            self.gearMotor.set(-self.speed)

        

class Climber:
    def _inti_():
        pass
    #.update
    #.move

class Cart:
    def _inti_():
        pass
    #.open
    #.close
    #.update
    #.status
