class Ultrasonic:
    def _init_():
        pass

class Switch:
    def _init_():
        pass

class Encode:
	def __init__(self, encoder, encoder2):
		self.encoder = encoder
		self.encoder2 = encoder2

	def getDistance(self):
		return (self.encoder.getDistance() + self.encoder2.getDistance()) / 2

	def getRate(self):
		return (self.encoder.getRate() + self.encoder2.getRate()) / 2

	def reset(self):
		self.encoder.reset()
		self.encoder2.reset()