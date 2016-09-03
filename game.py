#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###
from direct.showbase.ShowBase import ShowBase

### Net Core ###
from NetworkServer.server import Server
from NetworkClient.client import Client
from gui_test import MainMenu

########################################################################

## Simple Network Server ##

class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        
        # Server
        self.server = None
        self.client = None

        ### Fake sending packet <hide when not faking packet sending calls>
        #base.accept('s', self.server.sendPacket, [0, ["something", 1.5, "means", 0]])

        #print ("Press 's' to send fake packet...")

        # Test with gui
        self.mainmenu = MainMenu(self)
        self.mainmenu.frameMain.show()

    def startServer(self):
    	self.server = Server()
    	self.server.start()
    	self.mainmenu.btnStartHost['state'] = "DISABLED"
    	self.mainmenu.btnStartClient['state'] = "DISABLED"

    def startClient(self):
    	self.client = Client()
    	self.client.start()
    	self.mainmenu.btnStartHost['state'] = "DISABLED"
    	self.mainmenu.btnStartClient['state'] = "DISABLED"



game = Game()
game.run()