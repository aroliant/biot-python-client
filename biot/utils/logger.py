from biot.globals import *
def log(message):
	if LOGGING is True:
		print("[",APP_NAME,"]: ", message)