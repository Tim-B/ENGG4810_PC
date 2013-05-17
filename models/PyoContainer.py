from pyo import *


class PyoContainer:

    INSTANCE = None

    @classmethod
    def start(cls):
        cls.INSTANCE = Server(audio="offline").boot()
        cls.INSTANCE.start()
        cls.INSTANCE.recordOptions(dur=1, filename=None, fileformat=0, sampletype=0)


    @classmethod
    def starRec(cls, file):
        cls.INSTANCE.recstart(file)

    @classmethod
    def stopRec(cls) :
        cls.INSTANCE.recstop()
