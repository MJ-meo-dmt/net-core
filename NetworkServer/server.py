#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###

### Net Core ###
from Sockets.TCP_Socket import SocketTCP
from .manager import Manager

########################################################################

## Simple Network Server ##

class Server():

    def __init__(self, _parent=None):
        self.parent = _parent

        # Sockets
        self.socketTCP = None
        self.manager = None

    def start(self):
    	self.setSocket()

    	# Manager
    	self.manager = Manager(self)
    	self.manager.start()

    def setSocket(self):
    	self.socketTCP = SocketTCP()

    def sendPacket(self, _type, _data, _connection="testConnection", _channel=0): #0=tcp, 1=udp
    	self.manager.buildPacket(_type, _data, _connection, _channel)