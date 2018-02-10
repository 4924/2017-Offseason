class Forward:
    def __init__(self, distance, steer, speed, chassis):
        self.ramp = ramp
        self.distance = distance
        self.steer = steer
        self.speed = speed
        self.chassis = chassis

    def update(self):
        self.chassis.arcadeDrive()


class Auto:
    """Scheduler for autonomous actions"""
    def __init__(self):
        self.done = False

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
                    if finshFlag == 1:
                        if(self.autoUpdateCounter[i+1]==0): self.autoUpdateCounter[i+1] = 1
                        self.autoUpdateCounter[i] = 2
                    if finishFlag == 2:
                        if(self.autoUpdateCounter[i+1]==0): self.autoUpdateCounter[i+1] = 1
                i+=1
            if self.autoUpdateCounter.count(2) == len(self.autoUpdateCounter):
                self.done = True
            

