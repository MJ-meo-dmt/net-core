#!/usr/bin/python

## IMPORTS ##


### PANDA Imports ###
from panda3d.core import QueuedConnectionManager
from panda3d.core import QueuedConnectionReader
from panda3d.core import QueuedConnectionListener
from panda3d.core import ConnectionWriter
from panda3d.core import PointerToConnection, NetAddress, NetDatagram
from panda3d.core import Datagram
from panda3d.core import DatagramIterator

from direct.task.Task import Task
from utils import Queue
## Server Imports ##
from opcodes import MSG_NONE

########################################################################
########################################################################


### Server Side UDP ###

class SocketUDP():
    
    def __init__(self, _parent):
        self.parent = _parent

        # Tmp
        self.udpPort = 6003
    

    def startAll(self):
        print ("UDP Protocol Startup...")
        self.setupUDP()
        self.startUDPTasks()

    def setupUDP(self):
        self.udpManager = QueuedConnectionManager()
        self.udpReader = QueuedConnectionReader(self.udpManager, 0)
        self.udpWriter = ConnectionWriter(self.udpManager, 0)
        self.udpSocket = self.udpManager.openUDPConnection(self.udpPort)


    def startUDPTasks(self):
        taskMgr.add(self.udpReaderTask, "udpReaderTask", -39)


    def udpReaderTask(self, task):
        """
        Handle any data from udp clients.
        On port <port conf>
        """
        while 1:
            (datagram, data, opcode) = self.udpNonBlockingRead(self.udpReader)
            if opcode is MSG_NONE:
                # Nothing todo
                break 
            else:
                # Got data and handle it.
                #self.udpHandleDatagram(data, opcode, datagram.getConnection())
                print("something")
            
        return Task.cont 
        
        
    def udpNonBlockingRead(self, qcr):
        """
        Return a datagram collection and type if data is available on
        the queued connection udpReader.
        """
        if self.udpReader.dataAvailable():
            datagram = NetDatagram()
            if self.udpReader.getData(datagram):
                data = PyDatagramIterator(datagram)
                opcode = data.getUint16()
            else:
                data = None
                opcode = MSG_NONE
        else:
            datagram = None
            data = None
            opcode = MSG_NONE
            
        # Return the datagram to keep a handle on the data
        return (datagram, data, opcode)