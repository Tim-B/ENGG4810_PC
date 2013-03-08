from models.SampleTrack import *

class SampleWorkspace:
    samples = []

    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")

    @classmethod
    def getInstance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = SampleWorkspace()
        return cls.INSTANCE

    def addSample(self, sample):
        sampleTrack = SampleTrack(sample)
        self.samples.append(sampleTrack)

    def getSampleList(self):
        return self.samples

    def getSampleIndex(self, index):
        return self.samples[index]