# IoT Python Client

## Prerequisites

First you need to install socket.io python client

``pip install socketio-client``

## Usage

Now download the biot.py file and include that in your python file/project

```python
from biot.client import BIoTClient

DEVICE_ID = 1 		# Your Device ID
DEVICE_TOKEN = "" 	# Your Access Token

client = BIoTClient("<Server IP Address>", <port>, params={'token': DEVICE_TOKEN})

client.wait(2) # Give some time to connect to Server

def lightUpdate(status):
    print("Light update received" ,status);
    if status == 'true':
        # Turn your Device ON
        pass
    else:
        # Turn your Device ON
        pass
	

client.on_update(1, 'status', lightUpdate)

client.wait()

```

Run the program using ``python -u sample.py``

