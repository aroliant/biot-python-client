class Device():
	"""Default Device with ON / OFF Functions"""
	deviceID = None

	def __init__(self, deviceID):
		if deviceID is None:
			print("Provide a Device ID")
			return
		self.deviceID = deviceID

	def on(self):
		pass

	def off(self):
		pass

	def getPowerStatus(self):
		pass
