#!/usr/bin/env python3
import wpilib
from networktables import NetworkTables
from Comms import Comm
from Actions import Drive
from Actions import Mandible
from Sensors import Ultrasonic
from Sensors import Switch
from Control import Toggle
from Control import Logic
import Auto

class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.table = NetworkTables.getTable("SmartDashboard")
        self.robot_drive = wpilib.RobotDrive(0,1)
        self.drive_base = Drive(self.robot_drive)
        self.stick = wpilib.Joystick(0)
        self.climbingMotor = wpilib.Talon(2)
        self.ballSwitch1 = wpilib.DigitalInput(4)
        self.ballSwitch2 = wpilib.DigitalInput(5)
        self.rightmandlible = Mandible( wpilib.Spark(2), wpilib.DigitalInput(0), wpilib.DigitalInput(1))
        self.leftmandlible = Mandible( wpilib.Spark(3), wpilib.DigitalInput(2), wpilib.DigitalInput(3))
        self.ballMotor1 = wpilib.Relay(0)
        self.gyro = wpilib.ADXRS450_Gyro(0)
        self.gearSpeed = .5
        self.lights = wpilib.Relay(1)
        self.lightToggle = False
        self.lightToggleBool = True
        self.togglev = 0
        wpilib.CameraServer.launch()
        self.ultrasonic = wpilib.AnalogInput(0)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0
        autoPicker = self.table.getNumber('auto', 0)
        if(autoPicker == 0):
            routine = [Auto.Forward(ramp=Auto.ramp(), distance=5, steer=gyro, speed=0.8, chassis=self.robot_drive), Auto.Turn(steer=gyro, angle=90, chassis=self.robot_drive)]
        elif(autoPicker == 1):
            routine = [Auto.Turn]

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        for i in auto_loop_counter:
            finishFlag = routine[i].update()
            if(finshFlag == 1):
                auto_loop_counter.add(i+1)
                auto_loop_counter.remove(i)
            if(finishFlag == 2):
                auto_loop_counter.add(i+1)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        if self.stick.getRawButton(5):
            if self.togglev == 0:
                self.robot_drive.arcadeDrive(-0.75*self.stick.getY(), self.table.getNumber("cameraX", 0)/1.6)
                self.togglev = 1
            else:
                self.robot_drive.arcadeDrive(-0.75*self.stick.getY(), self.table.getNumber("cameraX", 0)*1.4)
                self.togglev = 0
        elif self.stick.getRawButton(9):
            self.robot_drive.arcadeDrive(-1*self.stick.getY(),-1*self.stick.getX())
        else:
            self.drive_base.move(-0.75*self.stick.getY(),-0.75*self.stick.getX())
            




        if self.stick.getRawButton(3):
            self.climbingMotor.set(-.3)
        else:
            self.climbingMotor.set(0)

        if self.stick.getRawButton(4) and self.lightToggleBool == False:
            pass
        elif self.stick.getRawButton(4) and self.lightToggleBool:
            self.lightToggle = not self.lightToggle
            if self.lightToggle:
                self.lights.set(wpilib.Relay.Value.kForward)
            else:
                self.lights.set(wpilib.Relay.Value.kOff)
            self.lightToggleBool = False
        elif self.stick.getRawButton(4) == False and self.lightToggleBool == False:
            self.lightToggleBool = True



        if self.stick.getRawButton(1):
            self.rightmandible.open()
            self.leftmandible.open()
        else:
            self.rightmandible.close()
            self.leftmandible.close()


  

        if self.stick.getRawButton(2) == False and self.ballSwitch1.get()==False:
            self.ballMotor1.set(wpilib.Relay.Value.kOff)
        elif self.stick.getRawButton(2) == False and self.ballSwitch1.get():
            self.ballMotor1.set(wpilib.Relay.Value.kReverse)
        elif self.stick.getRawButton(2) and self.ballSwitch2.get()==False:
            self.ballMotor1.set(wpilib.Relay.Value.kOff)
        elif self.stick.getRawButton(2) and self.ballSwitch2.get():
            self.ballMotor1.set(wpilib.Relay.Value.kForward)

        self.table.putNumber('ultra', self.ultrasonic.getVoltage())
        self.table.putNumber('GearMotor1 Forward', self.gearMotor1.get())
        self.table.putNumber('GearMotor2 Forward', self.gearMotor2.get())
        self.table.putNumber('GearMotor1 Reverse', self.gearMotor1.get())
        self.table.putNumber('GearMotor2 Reverse', self.gearMotor2.get())
        self.table.putNumber('gyro', self.gyro.getAngle())
        
        self.drive_base.update()
        #Other updates

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()

if __name__ == "__main__":
    wpilib.run(MyRobot)
