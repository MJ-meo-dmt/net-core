#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###
from panda3d.core import NetDatagram
from panda3d.core import DatagramIterator
from direct.task.Task import Task

### Net Core ###
from Utils.utils import Queue

########################################################################
# This will need some re-thinking once I finalized some types of packets and types of data.

class Packer():

    def __init__(self, _parent=None):

        self.parent = _parent

        self.builderQue = Queue()

        self.types = {0: self.general,
                    1: self.movement,
                    2: self.chat,
                    3: self.clientCreation}

    def start(self):

        # Tasks
        taskMgr.add(self.builder, "send_packets_que", 0)

    
    def builder(self, task):

        while not self.builderQue.isEmpty():
            typeData = self.builderQue.removeFromQue()

            if typeData[0] == 0:
                self.general(typeData)

            elif typeData == 1:
                self.movement(typeData)

        return Task.cont

        #### SAmple ####
    # def packPacket(self, _typedata):
    #     pkt = NetDatagram()
    #     pkt.addUint8(_type)
    #     return pkt

    def general(self, _typedata):
        
        _type = _typedata[0]
        _data = _typedata[1]
        _connection = _typedata[2]
        # 
        pkt = NetDatagram()
        pkt.addUint8(_type)

        for dataType in _data:
            print ("For dataType in data: ", dataType)
            print (type(dataType))

            if type(dataType) == int:
                pkt.addUint8(int(dataType))

            elif type(dataType) == float:
                pkt.addFloat32(float(dataType))

            elif type(dataType) == str:
                pkt.addString(str(dataType))

        self.parent.packetsToSend.addToQue([pkt, _connection])



    def movement(self, _typedata):
        # type
        # movement cmd
        # time stamp
        pass

    def chat(self, _typedata):
        pass

    def clientCreation(self, _typedata):
        pass
