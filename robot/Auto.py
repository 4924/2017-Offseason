class Forward:
    def __init__(self, ramp=Sramp, distance, steer, speed, chassis):
        self.ramp = ramp
        self.distance = distance
        self.steer = steer
        self.speed = speed
        self.chassis = chassis

    def update(self):
        self.chassis.arcadeDrive()
