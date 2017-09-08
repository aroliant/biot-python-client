from biot.client import BIoTClient

DEVICE_ID = 1 			# Your Device ID
DEVICE_TOKEN = "12345" 	# Your Access Token

client = BIoTClient("127.0.0.1",5000,params={'token': DEVICE_TOKEN})

client.wait(2)

def lightUpdate(status):
	print("Light update" ,status);

client.on_update(1, 'status', lightUpdate)

client.wait()
