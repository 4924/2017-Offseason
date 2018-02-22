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
        self.robot_drive = wpilib.drive.MecanumDrive(wpilib.Spark(2), wpilib.Spark(1), wpilib.Spark(5), wpilib.Spark(0))
        self.stick = wpilib.Joystick(0)
        self.ahrs = AHRS.create_i2c(0)
        
    def teleopInit(self):
    	self.ahrs.reset()


  
    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.robot_drive.driveCartesian(self.stick.getY(), self.stick.getX(), self.stick.getZ(), self.ahrs.getYaw())


if __name__ == "__main__":
    wpilib.run(MyRobot)
