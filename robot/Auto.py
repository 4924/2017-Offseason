import wpilib
import math

class Forward:
    def __init__(self, top_speed, top_accl, navX, encoder, chassis, distance, angle):
        self.top_speed = top_speed
        self.top_accl = top_accl
        self.navX = navX
        self.distance = distance
        self.encoder = encoder
        self.angle = angle
        self.chassis = chassis
        self.kP = 0.0005
        self.kI = 0.001
        self.kD = 0.00
        self.kF = 0.00
        self.aP = 0.08
        self.aI = 0.02
        self.aD = 0.3
        self.aF = 0.00
        self.kToleranceDegrees = 5
        self.aToleranceDegrees = 1
        self.fwdWrite = pidWriteObject()
        self.turnWrite = pidWriteObject()
        self.sum = 0
        currentSpeedRate = 0
        currentRotationRate = 0
        self.control = Distance(self.top_speed, self.top_accl, self.distance)
        self.tm = wpilib.Timer()
        self.tm.start()
        self.firstTime = True


        self.fwdController = wpilib.PIDController(self.kP, self.kI, self.kD, self.kF, self.encoder.getRate, self.fwdWrite)
        self.fwdController.setInputRange(-500.0,  500.0)
        self.fwdController.setOutputRange(-0.008, 0.008)
        self.fwdController.setAbsoluteTolerance(self.kToleranceDegrees)
        self.fwdController.setContinuous(True)

        self.turnController = wpilib.PIDController(self.aP, self.aI, self.aD, self.aF, navXPID(self.navX), self.turnWrite)
        self.turnController.setInputRange(-180.0,  180.0)
        self.turnController.setOutputRange(-0.4, 0.4)
        self.turnController.setAbsoluteTolerance(self.aToleranceDegrees)
        self.turnController.setContinuous(True)


    def update(self):
        if self.firstTime:
            self.firstTime = False
            self.start_time = self.tm.getMsClock()
            self.encoder.reset()

        self.fwdController.enable()
        self.turnController.enable()
        speed = self.control.speed(self.encoder.getDistance(), (self.tm.getMsClock() - self.start_time)/100)
        self.fwdController.setSetpoint(speed)
        self.turnController.setSetpoint(self.angle)
        self.sum -= self.fwdWrite.value
        currentSpeedRate = self.sum
        currentRotationRate = self.turnWrite.value
        self.chassis.arcadeDrive(currentSpeedRate, currentRotationRate)
        if(self.fwdController.onTarget() and self.control.speed(self.encoder.getDistance(), (self.tm.getMsClock() - self.start_time)/100)==0 and self.sum < 0.1 and self.sum > -0.1):
            return 1
        else:
            return 0


class Auto:
    """Scheduler for autonomous actions"""
    def __init__(self, actions):
        self.done = False
        self.actions = actions
        self.autoUpdateCounter = [0]

    def addActions(self, actions):
        """Adds a list of actions to the queue"""
        self.actions = actions
        self.autoUpdateCounter = [0]*len(self.actions)
        self.autoUpdateCounter[0] = 1

    def update(self):
        """Runs a queued actions"""
        if self.actions and not self.done:
            i = 0
            while i < len(self.autoUpdateCounter):
                if self.autoUpdateCounter[i] == 1:
                    finishFlag = self.actions[i].update()
                    if finishFlag == 1:
                        if(len(self.autoUpdateCounter)>i+1 and self.autoUpdateCounter[i+1]==0): self.autoUpdateCounter[i+1] = 1
                        self.autoUpdateCounter[i] = 2
                        print(i+1)
                    if finishFlag == 2:
                        if(len(self.autoUpdateCounter)>i+1 and self.autoUpdateCounter[i+1]==0): self.autoUpdateCounter[i+1] = 1
                i+=1
            if self.autoUpdateCounter.count(2) == len(self.autoUpdateCounter):
                self.done = True
            
class pidWriteObject:
    def __init__(self):
        self.value = 0

    def pidWrite(self, output):
        self.value = output

class navXPID:
    def __init__(self, nav):
        self.nav = nav

    def pidRead(self):
        return self.nav.getRoll()

class Distance:
    """This class calculates how fast the robot should be going"""
    
    def __init__(self, top_speed, top_accl, total_distance):
        self.top_speed = top_speed
        self.top_accl = top_accl
        self.total_distance = total_distance

        
    def speed(self, dist_traveled, time):
        """Takes distance left in inches and time passed in seconds. Returns speed in inches per second."""
        if self.total_distance - dist_traveled <= 0:
            #print("done")
            return 0
        
        if (self.top_speed**2)/self.top_accl > self.total_distance:
            if dist_traveled <= self.total_distance/2:
                #print("tri accl")
                return time * self.top_accl
                
            elif dist_traveled > self.total_distance/2:
                #print("tri deccl")
                return math.sqrt((2 * self.total_distance * self.top_accl) - (2 * dist_traveled * self.top_accl))

        elif (self.top_speed**2)/self.top_accl < self.total_distance:
            if self.top_speed**2/(self.top_accl*2) < dist_traveled and dist_traveled < self.total_distance - (self.top_speed**2/(self.top_accl*2)):
                #print("trap top")
                return self.top_speed
            
            elif self.top_speed ** 2 /(self.top_accl * 2) > dist_traveled:
                #print("trap accl")
                return time * self.top_accl
            
            elif self.total_distance - (self.top_speed**2/(self.top_accl *2)) < self.total_distance:
                #print("trap deccl")
                return math.sqrt((2 * self.total_distance * self.top_accl) - (2 * dist_traveled * self.top_accl))
            
        #print("did nothing")

class Turn:
    def __init__(self, navX, chassis, angle):
        self.navX = navX
        self.chassis = chassis
        self.angle = angle
        self.aP = 0.08
        self.aI = 0.02
        self.aD = 0.3
        self.aF = 0.00
        self.aToleranceDegrees = 1
        self.turnWrite = pidWriteObject()
        currentRotationRate = 0
        self.tm = wpilib.Timer()
        self.tm.start()
        self.firstTime = True

        self.turnController = wpilib.PIDController(self.aP, self.aI, self.aD, self.aF, navXPID(self.navX), self.turnWrite)
        self.turnController.setInputRange(-180.0,  180.0)
        self.turnController.setOutputRange(-0.4, 0.4)
        self.turnController.setAbsoluteTolerance(self.aToleranceDegrees)
        self.turnController.setContinuous(True)


    def update(self):
        if self.firstTime:
            self.firstTime = False
            self.start_time = self.tm.getMsClock()

        self.turnController.enable()
        self.turnController.setSetpoint(self.angle)
        currentRotationRate = self.turnWrite.value
        self.chassis.arcadeDrive(0, currentRotationRate)
        if self.turnController.onTarget():
            return 1
        else:
            return 0

class Elevator:
    def __init__(self, elevatorMotor, time, speed = -1):
        self.time = time
        self.speed = speed
        self.elevatorMotor = elevatorMotor
        self.tm = wpilib.Timer()
        self.tm.start()
        self.firstTime = True

    def update(self):
        if self.firstTime:
            self.firstTime = False
            self.elevatorMotor.set(self.speed)
            self.start_time = self.tm.getMsClock()

        if self.tm.getMsClock() - self.start_time < self.time:
            self.elevatorMotor.set(self.speed)

        if self.tm.getMsClock() - self.start_time > self.time:
            return 1

        return 2

class Intake:
    def __init__(self, intakeMotor, time, speed = .8):
        self.time = time
        self.speed = speed
        self.intakeMotor = intakeMotor
        self.tm = wpilib.Timer()
        self.tm.start()
        self.firstTime = True

    def update(self):
        if self.firstTime:
            self.firstTime = False
            self.intakeMotor.set(self.speed)
            self.start_time = self.tm.getMsClock()

        if self.tm.getMsClock() - self.start_time < self.time:
            self.intakeMotor.set(self.speed)

        if self.tm.getMsClock() - self.start_time > self.time:
            return 1

        return 2