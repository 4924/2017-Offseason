class Distance:
    """This class calculates how fast the robot should be going"""
    
    def __init__(self, top_speed, top_accl):
        self.top_speed = top_speed
        self.top_accl = top_accl
        
    def speed(self, dist_left, time):
        """Takes distance left in inches and time passed in seconds. Returns speed in inches per second."""
        if(dist_left < (self.top_accl/2)*(self.top_speed/self.top_accl)**2):
            return math.sqrt(dist_left/(self.top_accl/2))*self.accl
        elif(time > self.top_speed/self.top_accl):
            return self.top_speed
        else:
            return self.top_accl*time
