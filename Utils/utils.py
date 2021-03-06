import uuid

# tools
def giveUUID():
    return str(uuid.uuid4().fields[-1])[:5]








# Simple queue class
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addToQue(self, item):
        self.items.insert(0,item)

    def removeFromQue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)