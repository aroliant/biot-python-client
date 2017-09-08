class Refrigerator():
	"""Default Device with ON / OFF Functions"""
	deviceID = None

	def __init__(self, deviceID):
		if deviceID is None:
			print("Provide a Device ID")
			return
		self.deviceID = deviceID

	def setCooling(self):
		pass

	def setFreezing(self):
		pass

	def getCooling(self):
		pass

	def getFreezing(self):
		pass

	def setAutomatic(self):
		pass
