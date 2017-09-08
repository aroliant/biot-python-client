class Magnetometer():
	"""Default Device with ON / OFF Functions"""
	deviceID = None

	def __init__(self, deviceID):
		if deviceID is None:
			print("Provide a Device ID")
			return
		self.deviceID = deviceID

	def getInputaxis(self):
		pass

	def getOutputaxis(self):
		pass

	def getSpinaxis(self):
		pass
