#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

### Net Core ###
from NetworkServer.server import Server

########################################################################

## Simple Network Server ##

class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Sockets
        self.socketTCP = None

        
        # Start Server
        self.server = Server()
        self.server.start()

        ### Fake sending packet <hide when not faking packet sending calls>
        base.accept('s', self.server.sendPacket, [0, ["something", 1.5, "means", 0]])



game = Game()
game.run()