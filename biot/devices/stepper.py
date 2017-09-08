class Steppers():
	"""Default Device with ON / OFF Functions"""
	deviceID = None

	def __init__(self, deviceID):
		if deviceID is None:
			print("Provide a Device ID")
			return
		self.deviceID = deviceID

	def setspeed(self):
		pass

	def getspeed(self):
		pass

	def setforward(self):
		pass

	def setreverse(self):
		pass

	def getforward(self):
		pass

	def getreverse(self):
		pass

	def getstatus(self):
		pass
