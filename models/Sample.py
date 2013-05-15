from pyo import *
import ntpath

__author__ = 'Tim'


class Sample:
    def __init__(self, path):
        self.path = path
        self.name = ntpath.basename(path)
        self.table = SndTable(self.path)
        print(path)

    def getName(self):
        return self.name

    def getSoundPoints(self):
        self.table.view()
        size = self.table.getSize();
        if not isinstance(size, int):
            size = size[0]

        data = self.table.getEnvelope(size)[0]
        if size > (44100 * 10) :
            dS = []
            for i in xrange(0,size,500):
                dS.append(data[i])
            return dS
        return data


