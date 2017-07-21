# IoT Python Client

## Prerequisites

First you need to install socket.io python client

``pip install socketio-client``

## Usage

Now download the biot.py file and include that in your python file/project

```python
from biot import *


APP_KEY = <YOUR APP KEY>
DEV_KEY = <YOUR DEV KEY>
SECRECT = <YOUR SECRECT KEY>

#Create an IoT Client 

IoT = IoT(APP_KEY,DEV_KEY,SECRECT)

```
Provide the APP,DEV and SECRET Keys

### Functionalities

```python

#Connecting to IoT Server
IoT.connect()

# Setting the State
IoT.setData("YOUR STATE / DATA")

# Retriving the State
IoT.getData("YOUR STATE / DATA")

#Disconnecting from the IoT Server
IoT.disconnect()
```
