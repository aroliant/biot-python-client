from socketIO_client import SocketIO, LoggingNamespace
from biot.utils.logger import log


class BIoTClient:
	connected = False

	def __init__(self, host=False, port=False, params={}):

		self.connected = False
		self.param_call = {}
		self.param_functions = {}

		if host is False:
			log("Host not specified")

		elif port is False:
			log("Port not specified")
		elif params is None:
			log("Access Token not specified")

		else:
			log("Trying to connect " + host + " via port " + str(port))

			self.IO = SocketIO(host, port, params=params)
			self.IO.on('connect', self.on_connect)
			self.IO.on('disconnect', self.on_disconnect)
			self.IO.on('param:change', self.param_change)

	def on_connect(self):
		self.connected = True
		log('Connected to Server')

	def on_disconnect(self):
		self.connected = False
		log('Disconnected from Server')

	def on_reconnect(self):
		log('Trying to Reconnect')

	def param_change(self, device):
		for device_id, params in self.param_call.items():
			for key, function in params.items():
				print(dict(device))
				if device['id'] == int(device_id) and device['param'].encode("utf-8") == key.encode("utf-8"):
					self.param_functions[device_id][key](device['value'])

	def wait(self, time=None):
		if not time:
			self.IO.wait()
		else:
			self.IO.wait(time)

	def on_update(self, device_id, param, callback):
		try:
			self.param_call[str(device_id)][param] = callback.__name__
		except:
			self.param_call[str(device_id)] = {}
			self.param_call[str(device_id)][param] = callback.__name__

		try:
			self.param_functions[str(device_id)][param] = callback
		except:
			self.param_functions[str(device_id)] = {};
			self.param_functions[str(device_id)][param] = callback	
		

		log("Callback to " + callback.__name__ + " registered on " + param + " change")

	def setState(self, id, param, value):
		message = {'id': id, 'param': param, 'value': value}
		self.IO.emit("device:set:state", message)

	def getState(self, param):
		pass
