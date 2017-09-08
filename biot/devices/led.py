from biot.device import Device


class LED(Device):
	"""docstring for LED"""
	deviceID = None
	status = None

	def __init__(self, deviceID, statusMap, output):
		Device.__init__(self, deviceID)
		self.deviceID = deviceID
