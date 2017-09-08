class TV():
	"""Default Device with ON / OFF Functions"""
	deviceID = None

	def __init__(self, deviceID):
		if deviceID is None:
			print("Provide a Device ID")
			return
		self.deviceID = deviceID

	def setChannelnext(self):
		pass

	def setChannelprevious(self):
		pass

	def setVolumeup(self):
		pass

	def setVolumedown(self):
		pass

	def mute(self):
		pass

	def setmenu(self):
		pass

	def getmenu(self):
		pass
