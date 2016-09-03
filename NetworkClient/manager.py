#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###
from direct.task.Task import Task

### Net Core ###
from Packets.packer import Packer
from Utils.utils import Queue

########################################################################

## Simple Network Client Manager ##

class Manager():

    def __init__(self, _parent=None):
        self.parent = _parent

        # Tools 
        self.packer = None

        # Packets
        self.packetsToSend = Queue()

        # Rates
        self.sendingRate = 40/1000

        # Connection to server
        self.serverConnection = None


    def start(self):
        self.startTools()

    def startTools(self):
        self.packer = Packer(self)
        self.packer.start()

        # Start tasks
        taskMgr.add(self.sendPackets, "send_packets_que", 0)

    def buildPacket(self, _type, _data, _connection, _channel):
        if _channel == 0:
            # get connection from client object dict.
            print ("Added packet to Builder Que TCP")
            self.packer.builderQue.addToQue((_type, _data, _connection))
            print ("Builder Que: ", self.packer.builderQue.items)

        else:
            print ("use udp socket")

    def sendPackets(self, task):
        if not self.packetsToSend.isEmpty():
            print ("Packets to send Que: ", self.packetsToSend.items)
            pktToSend = self.packetsToSend.removeFromQue()
            print ("Packet to send:", pktToSend[0], pktToSend[1])
            
            self.parent.socketTCP.sendPacket(pktToSend[0], pktToSend[1])

        return Task.cont