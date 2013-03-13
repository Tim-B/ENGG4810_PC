from pyo import *

class PyoContainer:

    INSTANCE = None

    @classmethod
    def start(cls):
        cls.INSTANCE = Server().boot()
        cls.INSTANCE.start()

