class Fan():
	"""Default Device with ON / OFF Functions"""
	deviceID = None

	def __init__(self, deviceID):
		if deviceID is None:
			print("Provide a Device ID")
			return
		self.deviceID = deviceID

	def setSpeed(self):
		pass

	def getSpeed(self):
		pass
