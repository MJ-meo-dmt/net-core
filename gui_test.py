""" simple method and hints to set dgui elements according
to the windows aspect ratio """

import sys
#from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import DirectFrame
from direct.gui.DirectGui import DirectLabel
from direct.gui.DirectGui import DirectButton
from direct.gui.DirectGui import DirectEntry
from panda3d.core import TextNode

class MainMenu():#ShowBase):
    def __init__(self, _parent):
        """Default constructor"""
        #ShowBase.__init__(self)
        self.parent = _parent

        # create a main frame as big as the window
        self.frameMain = DirectFrame(
            # set framesize the same size as the window
            frameSize = (base.a2dLeft, base.a2dRight,
                         base.a2dTop, base.a2dBottom),
            # position center
            pos = (0, 0, 0),
            # set tramsparent background color
            frameColor = (0, 0, 0, 1))

        # create a sample title
        self.textscale = 0.12
        self.title = DirectLabel(
            scale = self.textscale,
            pos = (0.0, 0.0, base.a2dTop - self.textscale),
            frameColor = (0, 0, 0, 0),
            text = "Main Menu",
            text_align = TextNode.ACenter,
            text_fg = (1,1,1,1))
        self.title.setTransparency(1)
        self.title.reparentTo(self.frameMain)

        # create a sample exit button
        self.btnStartHost = DirectButton(
            scale = (0.1, 0.1, 0.1),
            text = "Start Host",
            # position on the window
            pos = (-1, 0, .65),
            # the event which is thrown on clickSound
            command = self.parent.startServer,
            # sounds that should be played
            rolloverSound = None,
            clickSound = None)
        self.btnStartHost.setTransparency(1)
        self.btnStartHost.reparentTo(self.frameMain)

        # create a sample exit button
        self.btnStartClient = DirectButton(
            scale = (0.1, 0.1, 0.1),
            text = "Start Client",
            # position on the window
            pos = (-1, 0, .53),
            # the event which is thrown on clickSound
            command = self.parent.startClient,
            # sounds that should be played
            rolloverSound = None,
            clickSound = None)
        self.btnStartClient.setTransparency(1)
        self.btnStartClient.reparentTo(self.frameMain)

        # create a sample exit button
        self.inputIP = DirectEntry(
            scale = (0.05, 0.05, 0.05),
            text = "",
            # position on the window
            pos = (-1.24, 0, .43),
            initialText="127.0.0.1",
            numLines = 1,
            # sounds that should be played
            rolloverSound = None,
            clickSound = None)
        self.btnStartClient.setTransparency(1)
        self.btnStartClient.reparentTo(self.frameMain)

        # create a sample exit button
        self.btnExit = DirectButton(
            scale = (0.1, 0.1, 0.1),
            text = "Exit",
            # position on the window
            pos = (-1, 0, .30),
            # the event which is thrown on clickSound
            command = lambda: sys.exit(),
            # sounds that should be played
            rolloverSound = None,
            clickSound = None)
        self.btnExit.setTransparency(1)
        self.btnExit.reparentTo(self.frameMain)

        self.frameMain.hide()

#s = Sample()
#s.run()