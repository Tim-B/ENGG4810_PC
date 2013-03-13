from models.PyoContainer import *
import tempfile

class LoopTrack:

    def __init__(self, index):
        self.listeners = []
        self.name = "Loop track " + str(index)

    def startCapture(self):
        pyo = PyoContainer.INSTANCE
        self.tmpFile = self.__getTempFile()
        pyo.recstart(self.tmpFile)

    def stopCapture(self):
        pyo = PyoContainer.INSTANCE
        pyo.recstop()
        self.player = SfPlayer(self.tmpFile, speed=[.75,.8], loop=True, mul=.3)
        self.player.out()
        self.table = SndTable(self.tmpFile)
        self.notifyListeners()


    def getName(self):
        return self.name

    def __getTempFile(self):
        tf = tempfile.NamedTemporaryFile()
        return tf.name

    def notifyListeners(self):
        for listener in self.listeners:
            listener.loopNotify()

    def registerForUpdate(self, instance):
        self.listeners.append(instance)

    def getSoundPoints(self, number):
        print self.tmpFile
        print self.table
        return self.table.getEnvelope(number)
