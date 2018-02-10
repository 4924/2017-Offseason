import sys
def test_imports(robot_path):
    sys.path.append(robot_path)
    from comms import Comm
    from actions import Drive
    from actions import Arm
    from sensors import Ultrasonic
    from sensors import Switch
    from control import Toggle
    from control import Logic

def test_Drive(robot_path, wpilib, hal_data):
    from actions import Drive

    wpi_drive = wpilib.RobotDrive(0,1) 
    drive_base = Drive(wpi_drive)

    assert drive_base.x==0
    assert drive_base.y==0
    assert drive_base.drive==wpi_drive

    drive_base.move(0.5, 0.4)
    assert drive_base.x==0.5
    assert drive_base.y==0.4

    drive_base.move(-0.6, 1)
    assert drive_base.x==-0.6
    assert drive_base.y==1

    drive_base.move(0, -1)
    assert drive_base.x==0
    assert drive_base.y==-1

    drive_base.update()
     
