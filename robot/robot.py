#!/usr/bin/env python3
import wpilib
import wpilib.drive
from networktables import NetworkTables
from Comms import Comm
from Actions import Drive
from Actions import Mandible
import Sensors
from Control import Toggle
from robotpy_ext.common_drivers.navx import AHRS
#from Control import Logic
import Auto
import math
from wpilib.doublesolenoid import DoubleSolenoid

class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        self.table = NetworkTables.getTable("SmartDashboard")
        self.robot_drive = wpilib.drive.DifferentialDrive(wpilib.Spark(0), wpilib.Spark(1))
        self.stick = wpilib.Joystick(0)
        self.elevatorMotor = wpilib.VictorSP(5)
        self.intakeMotor = wpilib.VictorSP(2)
        self.intakeMotorLeft = wpilib.VictorSP(3)
        self.intakeMotorRight = wpilib.VictorSP(4)
        self.climbMotor = wpilib.VictorSP(6)
        self.ahrs = AHRS.create_i2c(0)
        #self.gearSpeed = .5
        #self.lights = wpilib.Relay(1)
        #self.lightToggle = False
        #self.lightToggleBool = True
        #self.togglev = 0


        self.robot_drive.setSafetyEnabled(False)

        wpilib.CameraServer.launch()
        self.xb = wpilib.Joystick(1)
        
        self.Compressor = wpilib.Compressor(0)
        self.Compressor.setClosedLoopControl(True)
        self.enabled = self.Compressor.enabled()
        self.PSV = self.Compressor.getPressureSwitchValue()
        self.LeftSolenoid = wpilib.DoubleSolenoid(0,1)
        self.RightSolenoid = wpilib.DoubleSolenoid(2,3)
        self.Compressor.start()

        self.wheel = wpilib.Encoder(0, 1)
        self.wheel2 = wpilib.Encoder(2, 3, True)
        self.encoder = Sensors.Encode(self.wheel, self.wheel2)
        #wpilib.CameraServer.launch()
        self.ultrasonic = wpilib.AnalogInput(0)
        self.autoSchedule = Auto.Auto(self, )
        self.intakeToggle = False
        self.intakePos = False
        self.openSwitch = wpilib.DigitalInput(9)
        self.closedSwitch = wpilib.DigitalInput(8)

        self.speed = 0.6
        self.leftSpeed = 0.7
        self.rightSpeed = 0.7
        self.speedToggle = False 



    def autonomousInit(self):
        self.counter = 0

        """This function is run once each time the robot enters autonomous mode."""
        self.ahrs.reset()
        #autoPicker = self.table.getNumber('auto', 'defaultValue')
        config = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        while len(config) < 3:
            config = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        #if self.speed == .7:
        	#self.robot_drive.arcadeDrive(-0.6, 0.6)
        #if autoPicker == 0:
        #starting from center go to the left of the switch
            #if config[0] == 'L' :
                #Drive forward 51 inches at 0 degrees, Turn -90 degrees, drive forward 65 inches at -90 degrees, turn 90 degrees, drive forward 79.8 inches at 0 degrees
                #self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 510, 0), Auto.Turn(self.ahrs, self.robot_drive, -90), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 650, -90), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Elevator(self.elevatorMotor, 100), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 798, 0), Auto.Intake(self.intakeMotor, 100)])
            #starting from center go to right of the switch
            #else:
                #Drive forward 51 inches at 0 degrees, Turn 90 degrees, drive forward 65 inches at 90 degrees, turn -90 degrees, drive forward 79.8 inches at 0 degrees
                #self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 510, 0), Auto.Turn(self.ahrs, self.robot_drive, 90), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 530, 90), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Elevator(self.elevatorMotor, 100), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 798, 0), Auto.Intake(self.intakeMotor, 100)])
        #Still from center postition
        #elif autoPicker == 1:
            #If you want to just pass the auto line
            #Turn 90 degrees, drive forward 170 inches at 90 degrees, turn -90 degrees, drive forward 125 inches at 0 degrees
            #self.autoSchedule.addActions([Auto.Turn(self.ahrs, self.robot_drive, 90), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 1700, 90), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 1250, 0)])
        #starting in left position
        #elif autoPicker == 2:
            #If scale is on the left and switch is not, go to scale
            #if config[0] == 'R' and config[1] == 'L':
                #drive forward 60 inches at 0 degrees, turn -15 degrees, drive forward 60 inches at -15 degrees, turn 15 degrees, drive forward 216 inches at 0 degrees, turn 90 degrees
                #self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 0), Auto.Turn(self.ahrs, self.robot_drive, -15), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, -15), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Elevator(self.elevatorMotor, 500), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 2160, 0),Auto.Turn(self.ahrs, self.robot_drive, 90), Auto.Intake(self.intakeMotor, 100)])
            #If switch is on the left and scale is not, go to switch
            #elif config[0] == 'L' and config[1] == 'R':
                #drive forward 60 inches at 0 dgrees, turn -15 degrees, drive forward 60 inches at -15 degrees, turn 15 degrees, drive forward 24 inches at 0 degrees, turn 90 degrees, drive forward 24 inches at 90 degrees
                #self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 1700, 0), Auto.Turn(self.ahrs, self.robot_drive, 90), Auto.Elevator(self.elevatorMotor, 100), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 165, 90), Auto.Intake(self.intakeMotor, 100)])
            #If sacle and switch are on the left, go to scale
            #elif config[0] == 'L' and config[1] == 'L':
                #drive forward 60 inches at 0 degrees, turn -15 degrees, drive forward 60 inches at -15 degrees, turn 15 degrees, drive forward 216 inches at 0 degrees, turn 90 degrees
                #self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 0), Auto.Turn(self.ahrs, self.robot_drive, -15), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, -15), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Elevator(self.elevatorMotor, 500), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 2160, 0),Auto.Turn(self.ahrs, self.robot_drive, 90), Auto.Intake(self.intakeMotor, 100)])
            #If neither are on the left, pass the auto line
            #else:
                #drive forward 125 inches at 0 degrees
                #print("it worked")
                #self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 1250, 0)])
        #starting from right
        #elif autoPicker == 3:
            #If scale is on the right and switch is not, go to scale
            #if config[0] == 'L' and config[1] == 'R':
                #drive forward 60 inches at 0 degrees, turn 15 degrees, drive forward 60 inches at 15 degrees, turn -15 degrees, drive forward 216 inches at 0 degrees, turn -90 degrees
                #self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 0), Auto.Turn(self.ahrs, self.robot_drive, 15), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 15), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Elevator(self.elevatorMotor, 500), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 2160, 0),Auto.Turn(self.ahrs, self.robot_drive, -90), Auto.Intake(self.intakeMotor, 100)])
            #If switch is on the right and scale is not, go to switch
            #elif config[0] == 'R' and config[1] == 'L':
                #drive forward 60 inches at 0 dgrees, turn 15 degrees, drive forward 60 inches at 15 degrees, turn -15 degrees, drive forward 24 inches at 0 degrees, turn -90 degrees, drive forward 24 inches at -90 degrees
                #self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 0), Auto.Turn(self.ahrs, self.robot_drive, 15), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 15), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 240, 0), Auto.Turn(self.ahrs, self.robot_drive, -90), Auto.Elevator(self.elevatorMotor, 100), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 240, -90), Auto.Intake(self.intakeMotor, 100)])
            #If scale and switch are on the right, go to scale
            #elif config[0] == 'R' and config[1] == 'R':
                #drive forward 60 inches at 0 degrees, turn 15 degrees, drive forward 60 inches at 15 degrees, turn -15 degrees, drive forward 216 inches at 0 degrees, turn -90 degrees
                #self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 0), Auto.Turn(self.ahrs, self.robot_drive, 15), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 15), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Elevator(self.elevatorMotor, 500), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 2160, 0),Auto.Turn(self.ahrs, self.robot_drive, -90), Auto.Intake(self.intakeMotor, 100)])
            #If neither are on the right, pass the auto line
            #else:
                #drive forward 125 inches at 0 degrees
                #self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 1250, 0)])

    def autonomousPeriodic(self):
        #print('hello')
        self.counter == 0
        config = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        while len(config) < 3:
            config = wpilib.DriverStation.getInstance().getGameSpecificMessage()
            #self.counter = 1
        #else:
            #value = chooser.getSelected()
        #"""This function is called periodically during autonomous."""
        self.autoSchedule.update()
        self.table.putNumber('encodeD', self.wheel.getDistance())
        self.table.putNumber('encodeD2', self.wheel2.getDistance())
        self.table.putNumber('nav', self.ahrs.getYaw())
        self.counter += 1

        #if  self.counter < 500 and config[0] == 'L':
            #self.robot_drive.arcadeDrive(-.3, 0)
        #elif self.counter < 200 and config[0] == 'R':
            #self.robot_drive.arcadeDrive(-.55, 0)
        #else:
            #self.robot_drive.arcadeDrive(0, 0)
        if self.counter < 200:
            self.robot_drive.arcadeDrive(-.55, 0)
        else:
            self.robot_drive.arcadeDrive(0, 0)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""

        if self.stick.getRawAxis(2) < 0.2:
            self.robot_drive.arcadeDrive(-self.speed*self.stick.getRawAxis(1), self.speed*self.stick.getRawAxis(0))
            self.speed = 0.6 + (self.stick.getRawAxis(3) / 2)
        elif self.stick.getRawAxis(2) > 0.2:
            """Tank Drive"""
            self.leftSpeed = -0.7 * self.stick.getRawAxis(1)
            self.rightSpeed = -0.7 * self.stick.getRawAxis(5)
        
            self.robot_drive.tankDrive(self.leftSpeed, self.rightSpeed)

            if self.stick.getRawButton(6) == 1:
        	    self.robot_drive.tankDrive(0.7, -0.7)
            elif self.stick.getRawButton(5) == 1:
        	    self.robot_drive.tankDrive(-0.7, 0.7)





        self.speedToggle = self.stick.getRawButton(3)

        if self.stick.getRawButton(5):
            self.elevatorMotor.set(1)  #make go up
        elif self.stick.getRawButton(6):
            self.elevatorMotor.set(-1) #make go down
        else:
            self.elevatorMotor.set(0) #make stop

        if self.stick.getRawButton(2):
            self.climbMotor.set(1)  #make go up
        elif self.stick.getRawButton(4):
            self.climbMotor.set(-1) #make go down
        else:
            self.climbMotor.set(0) #make stop

#Intake

        
        '''if self.stick.getRawButton(1) and not self.intakeToggle:
            self.intakePos = not self.intakePos
            
        if self.stick.getRawButton(1):
            self.intakeMotor.set(1)
        else:
            self.intakeMotor.set(0)

        leftValue = self.stick.getRawAxis(5) - self.stick.getRawAxis(4)
        if  abs(leftValue) > .3: self.intakeMotorLeft.set(leftValue)
        else: self.intakeMotorLeft.set(0)
        rightValue = -self.stick.getRawAxis(5) + self.stick.getRawAxis(4)
        if abs(rightValue) > .3: self.intakeMotorRight.set(rightValue)
        else: self.intakeMotorRight.set(0)'''

        if(self.xb.getRawButton(7)):
                self.LeftSolenoid.set(DoubleSolenoid.Value.kForward)
                self.RightSolenoid.set(DoubleSolenoid.Value.kForward)
        elif(self.xb.getRawButton(8)):
                self.LeftSolenoid.set(DoubleSolenoid.Value.kReverse)
                self.RightSolenoid.set(DoubleSolenoid.Value.kReverse)

        self.table.putNumber('encodeD', self.wheel.getDistance())
        self.table.putNumber('encodeD2', self.wheel2.getDistance())
        self.table.putNumber('nav', self.ahrs.getYaw())
        

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()

if __name__ == "__main__":
    wpilib.run(MyRobot)
