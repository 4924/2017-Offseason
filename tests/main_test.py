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
