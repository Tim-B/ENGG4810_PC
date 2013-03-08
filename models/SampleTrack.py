from pyo import *
import ntpath

class SampleTrack:

    path = None
    player = None
    name = None

    def __init__(self, path):
        self.path = path
        self.name = ntpath.basename(path)
        self.player = SfPlayer(path, speed=[.75,.8], loop=True, mul=.3)

    def getPlayer(self):
        return self.player

    def getName(self):
        return self.name

    def __str__(self):
        return self.getName()
