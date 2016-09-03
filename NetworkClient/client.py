#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###

### Net Core ###
from Sockets.TCP_Socket_Client import SocketTCPClient
from .manager import Manager

########################################################################

## Simple Network Client ##

class Client():

    def __init__(self, _parent=None):
        self.parent = _parent

        # Sockets
        self.socketTCP = None
        self.manager = None

    def start(self):
        self.setSocket()
        self.socketTCP.start()

        # Manager
        self.manager = Manager(self)
        self.manager.start()

        # Connect to server
        self.socketTCP.connectToServer()

    def setSocket(self):
        self.socketTCP = SocketTCPClient()

    def sendPacket(self, _type, _data, _connection, _channel=0): #0=tcp, 1=udp
        self.manager.buildPacket(_type, _data, _connection, _channel)