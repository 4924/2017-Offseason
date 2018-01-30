#!/usr/bin/env python3

import wpilib
import wpilib.drive
from robotpy_ext.common_drivers.navx import AHRS
import wpilib.drive
from networktables import NetworkTables
import math

class Distance:
    """This class calculates how fast the robot should be going"""
    
    def __init__(self, top_speed, top_accl):
        self.top_speed = top_speed
        self.top_accl = top_accl

        
    def speed(self, dist_left, time):
        """Takes distance left in inches and time passed in seconds. Returns speed in inches per second."""
        if(dist_left < (self.top_accl/2)*(self.top_speed/self.top_accl)**2):
            return math.sqrt(dist_left/(self.top_accl/2))*self.top_accl
        elif(time > self.top_speed/self.top_accl):
            return self.top_speed
        else:
            return self.top_accl*time

def AverageOutRateGen(getRate, getRate2):
    def Average():
        return (getRate() + getRate2()) / 2
    return Average

def average(one, two ):
    return (one + two) / 2

class MyRobot(wpilib.SampleRobot):
    """This is a demo program showing the use of the navX MXP to implement
    a "rotate to angle" feature. This demo works in the pyfrc simulator.
    
    This example will automatically rotate the robot to one of four
    angles (0, 90, 180 and 270 degrees).
    
    This rotation can occur when the robot is still, but can also occur
    when the robot is driving.  When using field-oriented control, this
    will cause the robot to drive in a straight line, in whatever direction
    is selected.
    
    This example also includes a feature allowing the driver to "reset"
    the "yaw" angle.  When the reset occurs, the new gyro angle will be
    0 degrees.  This can be useful in cases when the gyro drifts, which
    doesn't typically happen during a FRC match, but can occur during
    long practice sessions.
    
    Note that the PID Controller coefficients defined below will need to
    be tuned for your drive system.
    """

    # The following PID Controller coefficients will need to be tuned */
    # to match the dynamics of your drive system.  Note that the      */
    # SmartDashboard in Test mode has support for helping you tune    */
    # controllers by displaying a form where you can enter new P, I,  */
    # and D constants and test the mechanism.                         */
    
    # Often, you will find it useful to have different parameters in
    # simulation than what you use on the real robot
    
    if wpilib.RobotBase.isSimulation():
        # These PID parameters are used in simulation
        kP = 0.06
        kI = 0.00
        kD = 0.00
        kF = 0.00
    else:
        # These PID parameters are used on a real robot
        kP = 0.000025
        kI = 0.00
        kD = 0.00
        kF = 0.00
    
    kToleranceDegrees = 5
        
    def robotInit(self):
        # Channels for the wheels
        self.table = NetworkTables.getTable("SmartDashboard")
        self.myRobot = wpilib.drive.DifferentialDrive(wpilib.Spark(0), wpilib.Spark(1))
        self.myRobot.setExpiration(0.1)
        self.stick = wpilib.Joystick(0)
        self.wheel = wpilib.Encoder(0, 1)
        self.wheel2 = wpilib.Encoder(2, 3, True)
        self.wheel.reset()
        self.wheel2.reset()
        self.wheel.setDistancePerPulse(0.8922)
        self.wheel2.setDistancePerPulse(0.8922)
        self.rate = AverageOutRateGen(self.wheel.getRate, self.wheel2.getRate)
        self.sum = 0
        self.toggle = True
        self.control = Distance(300, 50)
        
        #
        # Communicate w/navX MXP via the MXP SPI Bus.
        # - Alternatively, use the i2c bus.
        # See http://navx-mxp.kauailabs.com/guidance/selecting-an-interface/ for details
        #
        
        #self.ahrs = AHRS.create_spi()
        self.ahrs = AHRS.create_i2c(0)
        
        turnController = wpilib.PIDController(self.kP, self.kI, self.kD, self.kF,  AverageOutRateGen(self.wheel.getRate, self.wheel2.getRate), output=self)
        turnController.setInputRange(-500,  500.0)
        turnController.setOutputRange(-0.008, 0.008)
        turnController.setAbsoluteTolerance(self.kToleranceDegrees)
        turnController.setContinuous(True)
        
        self.turnController = turnController
        
        # Add the PID Controller to the Test-mode dashboard, allowing manual  */
        # tuning of the Turn Controller's P, I and D coefficients.            */
        # Typically, only the P value needs to be modified.                   */
        wpilib.LiveWindow.addActuator("DriveSystem", "RotateController", turnController)

    def operatorControl(self):
        """Runs the motors with onnidirectional drive steering.
        
        Implements Field-centric drive control.
        
        Also implements "rotate to angle", where the angle
        being rotated to is defined by one of four buttons.
        
        Note that this "rotate to angle" approach can also
        be used while driving to implement "straight-line
        driving".
        """
        
        tm = wpilib.Timer()
        tm.start()
        
        self.myRobot.setSafetyEnabled(True)
        while self.isOperatorControl() and self.isEnabled():
            
            if tm.hasPeriodPassed(1.0):
                print("NavX Gyro", self.ahrs.getYaw(), self.ahrs.getAngle())
            
            rotateToAngle = False
            if self.stick.getRawButton(1):
                self.ahrs.reset()
            
            if self.stick.getRawButton(2) and self.toggle:
                tm.start()
                self.turnController.setSetpoint(300)
                self.wheel.reset()
                self.wheel2.reset()
                self.toggle = False
                rotateToAngle = True
            elif self.stick.getRawButton(2):
                print(tm.get())
                #print(self.control.speed(tm.get(), 500-average(self.wheel.getDistance(), self.wheel2.getDistance())))
                self.turnController.setSetpoint(300)
                rotateToAngle = True
            elif not self.toggle:
                self.toggle = True
            
            if rotateToAngle:
                self.turnController.enable()
                self.sum -= self.rotateToAngleRate
                currentRotationRate = self.sum
            else:
                self.turnController.disable()
                currentRotationRate = self.stick.getRawAxis(1)
            
            
            self.myRobot.arcadeDrive(self.stick.getRawAxis(0), currentRotationRate)
            
            self.table.putNumber('encodeD', self.wheel.getDistance())
            self.table.putNumber('encodeD2', self.wheel2.getDistance())
            self.table.putNumber('rate', self.rate())

            wpilib.Timer.delay(0.005) # wait for a motor update time
        
    def pidWrite(self, output):
        """This function is invoked periodically by the PID Controller,
        based upon navX MXP yaw angle input and PID Coefficients.
        """
        self.rotateToAngleRate = output

if __name__ == '__main__':
    wpilib.run(MyRobot)
