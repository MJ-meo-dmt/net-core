#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##
import msgpack

### PANDA Imports ###
from panda3d.core import NetDatagram
from panda3d.core import DatagramIterator

########################################################################
# This will need some re-thinking once I finalized some types of packets and types of data.

class Packer():

    def __init__(self, _parent):

    	self.parent = _parent

    
    def writePacket(self, _type, _data):
        encodedData = str(msgpack.packb(_data))
        pkt = NetDatagram()
        pkt.addUint8(_type)
        pkt.addString(encodedData)

        return pkt

    def readPacket(self, _type, _pkt):
        pType = _pkt.getUint8()
        decodedData = _pkt.getString()

        return decodedData