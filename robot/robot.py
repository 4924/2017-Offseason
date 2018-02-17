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

class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.table = NetworkTables.getTable("SmartDashboard")
        self.robot_drive = wpilib.drive.DifferentialDrive(wpilib.Spark(0), wpilib.Spark(1))
        self.stick = wpilib.Joystick(0)
        self.elevatorMotor = wpilib.VictorSP(6)
        self.intakemotor = wpilib.VictorSP(3)
        self.intakemotorleft = wpilib.VictorSP(4)
        self.intakemotorright = wpilib.VictorSP(5)
        self.ahrs = AHRS.create_i2c(0)
        #self.gearSpeed = .5
        #self.lights = wpilib.Relay(1)
        #self.lightToggle = False
        #self.lightToggleBool = True
        #self.togglev = 0
        self.wheel = wpilib.Encoder(0, 1)
        self.wheel2 = wpilib.Encoder(2, 3, True)
        self.encoder = Sensors.Encode(self.wheel, self.wheel2)
        #wpilib.CameraServer.launch()
        self.ultrasonic = wpilib.AnalogInput(0)
        self.autoSchedule = Auto.Auto() 
        chooser = wpilib.SendableChooser()
        chooser.addObject('Start Pos 2', '0')
        chooser.addObject('Start Pos 2', '1')
        chooser.addObject('Start Pos 1', '2')
        chooser.addObject('Start Pos 3', '3')

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.ahrs.reset()
        autoPicker = chooser.getSelected()
        config = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        if autoPicker == 0:
            #starting from center go to the left of the switch
            if config[0] == 'L' :
                #Drive forward 51 inches at 0 degrees, Turn -90 degrees, drive forward 65 inches at -90 degrees, turn 90 degrees, drive forward 79.8 inches at 0 degrees
                self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 510, 0), Auto.Turn(self.ahrs, self.robot_drive, -90), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 650, -90), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 798, 0)])
            #starting from center go to right of the switch
            else:
                #Drive forward 51 inches at 0 degrees, Turn 90 degrees, drive forward 65 inches at 90 degrees, turn -90 degrees, drive forward 79.8 inches at 0 degrees
                self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 510, 0), Auto.Turn(self.ahrs, self.robot_drive, 90), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 530, 90), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 798, 0)])
        #Still from center postition
        elif autoPicker == 1:
            #If you want to just pass the auto line
            #Turn 90 degrees, drive forward 170 inches at 90 degrees, turn -90 degrees, drive forward 125 inches at 0 degrees
            self.autoSchedule.addActions([Auto.Turn(self.ahrs, self.robot_drive, 90), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 1700, 90), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 1250, 0)])
        #starting in left position
        elif autoPicker == 2:
            #If scale is on the left and switch is not, go to scale
            if config[0] == 'R' and config[1] == 'L':
                #drive forward 60 inches at 0 degrees, turn -15 degrees, drive forward 60 inches at -15 degrees, turn 15 degrees, drive forward 216 inches at 0 degrees, turn 90 degrees
                self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 0), Auto.Turn(self.ahrs, self.robot_drive, -15), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, -15), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 2160, 0),Auto.Turn(self.ahrs, self.robot_drive, 90)])
            #If switch is on the left and scale is not, go to switch
            elif config[0] == 'L' and config[1] == 'R':
                #drive forward 60 inches at 0 dgrees, turn -15 degrees, drive forward 60 inches at -15 degrees, turn 15 degrees, drive forward 24 inches at 0 degrees, turn 90 degrees, drive forward 24 inches at 90 degrees
                self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 0), Auto.Turn(self.ahrs, self.robot_drive, -15), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, -15), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 240, 0), Auto.Turn(self.ahrs, self.robot_drive, 90), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 240, 90)])
            #If sacle and switch are on the left, go to scale
            elif config[0] == 'L' and config[1] == 'L':
                #drive forward 60 inches at 0 degrees, turn -15 degrees, drive forward 60 inches at -15 degrees, turn 15 degrees, drive forward 216 inches at 0 degrees, turn 90 degrees
                self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 0), Auto.Turn(self.ahrs, self.robot_drive, -15), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, -15), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 2160, 0),Auto.Turn(self.ahrs, self.robot_drive, 90)])
            #If neither are on the left, pass the auto line
            else:
                #drive forward 125 inches at 0 degrees
                self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 1250, 0)])
        #starting form right
        elif autoPicker == 3:
            #If scale is on the right and switch is not, go to scale
            if config[0] == 'L' and config[1] == 'R':
                #drive forward 60 inches at 0 degrees, turn 15 degrees, drive forward 60 inches at 15 degrees, turn -15 degrees, drive forward 216 inches at 0 degrees, turn -90 degrees
                self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 0), Auto.Turn(self.ahrs, self.robot_drive, 15), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 15), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 2160, 0),Auto.Turn(self.ahrs, self.robot_drive, -90)])
            #If switch is on the right and scale is not, go to switch
            elif config[0] == 'R' and config[1] == 'L':
                #drive forward 60 inches at 0 dgrees, turn 15 degrees, drive forward 60 inches at 15 degrees, turn -15 degrees, drive forward 24 inches at 0 degrees, turn -90 degrees, drive forward 24 inches at -90 degrees
                self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 0), Auto.Turn(self.ahrs, self.robot_drive, 15), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 15), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 240, 0), Auto.Turn(self.ahrs, self.robot_drive, -90), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 240, -90)])
            #If scale and switch are on the right, go to scale
            elif config[0] == 'R' and config[1] == 'R':
                #drive forward 60 inches at 0 degrees, turn 15 degrees, drive forward 60 inches at 15 degrees, turn -15 degrees, drive forward 216 inches at 0 degrees, turn -90 degrees
                self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 0), Auto.Turn(self.ahrs, self.robot_drive, 15), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 600, 15), Auto.Turn(self.ahrs, self.robot_drive, 0), Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 2160, 0),Auto.Turn(self.ahrs, self.robot_drive, -90)])
            #If neither are on the right, pass the auto line
            else:
                #drive forward 125 inches at 0 degrees
                self.autoSchedule.addActions([Auto.Forward(300, 20, self.ahrs, self.encoder, self.robot_drive, 1250, 0)])

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        self.autoSchedule.update()
        self.table.putNumber('encodeD', self.wheel.getDistance())
        self.table.putNumber('encodeD2', self.wheel2.getDistance())
        self.table.putNumber('nav', self.ahrs.getYaw())

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.robot_drive.arcadeDrive(-self.stick.getY(), self.stick.getX())

        if self.stick.getRawButton(5):
            self.elevatorMotor.set(0.6)  #make go up
        elif self.stick.getRawButton(6):
            self.elevatorMotor.set(-0.6) #make go down
        else:
            self.elevatorMotor.set(0) #make stop


        if self.stick.getRawButton(1):
            self.intakemotor.set(0.6)  #intake
        elif self.stick.getRawButton(2):
            self.intakemotor.set(-0.6)  #output
        else:
            self.intakemotor.set(0) #stop

        leftValue = self.stick.getRawAxis(5) + self.stick.getRawAxis(4)
        if  abs(leftValue) > .3: self.intakemotorleft.set(leftValue)
        else: self.intakemotorleft.set(0)
        rightValue = -self.stick.getRawAxis(5) + self.stick.getRawAxis(4)
        if abs(rightValue) > .3: self.intakemotorright.set(rightValue)
        else: self.intakemotorright.set(0)




        self.table.putNumber('encodeD', self.wheel.getDistance())
        self.table.putNumber('encodeD2', self.wheel2.getDistance())
        self.table.putNumber('nav', self.ahrs.getYaw())
        

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()

if __name__ == "__main__":
    wpilib.run(MyRobot)
