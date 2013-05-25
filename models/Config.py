__author__ = 'Tim'

class Config:

    def __init__(self):
        self.effect1 = None
        self.effect2 = None
        self.lfo = 0

    def getEffectOptions(self):
        return ["None", "Lowpass", "Highpass", "Bandpass", "Notch", "Delay", "Echo", "Decimator/Bitcrusher", "Bitwise KO"]

