__author__ = 'Tim'

class Config:

    def __init__(self):
        self.effect1 = None
        self.effect2 = None

    def getEffectOptions(self):
        return ["None", "Lowpass", "Highpass", "Bandpass", "Notch", "Delay", "Delay/Echo", "Decimator/Bitcrusher", "Bitwise KO"]

