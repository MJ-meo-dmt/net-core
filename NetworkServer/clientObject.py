#!/usr/bin/python
#----------------------------------------------------------------------#

## IMPORTS ##

### PANDA Imports ###

### Net Core ###

########################################################################

## Simple Network Serverside ClientObject ##

class ClientObject():

    def __init__(self, _id, _connection):

        self.ID = _id
        self.connection = _connection

        print("Client Object created:", self.ID, self.connection)