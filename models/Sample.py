from pyo import *
import ntpath
import copy

__author__ = 'Tim'


class Sample:
    def __init__(self, path):
        self.path = path
        self.name = ntpath.basename(path)
        self.player = SfPlayer(path)
        self.table = SndTable(self.path, chnl=0)
        self.length = self.table.getDur()
        self.effect = 'None'
        self.latch = False
        self.effectStrength = float(0)
        print(path)

    def getName(self):
        return self.name

    def getSoundPoints(self):
        size = self.table.getSize();
        data = self.table.getEnvelope(size)[0]
        if size > (44100 * 10) :
            dS = []
            for i in xrange(0,size,500):
                dS.append(data[i])
            return dS
        return data

    def export(self, controller, sampleIndex, path):
        dir = path + '/mpc/'
        samplePath = dir + str(sampleIndex) + '.wav'
        data = self.applyEffect()
        if not os.path.isdir(dir) :
             os.makedirs(dir)

        if os.path.isfile(samplePath):
            os.remove(samplePath)

        controller.pyo.recordOptions(dur=self.length, filename=samplePath, fileformat=0, sampletype=3)
        data.out()
        controller.pyo.start()
        self.length = self.table.getDur()

    def applyEffect(self):
        print self.effect
        if self.effect == 'Delay':
            print 'Applying delay'
            return self.applyDelay()

        if self.effect == 'Decimator':
            print 'Applying decimator'
            return self.applyDecimate()

        if self.effect == 'Bitcrusher':
            print 'Apply bitcrush'
            return self.applyBitcrush()

        if self.effect == 'Pitch Shift':
            print 'Pitch shift'
            return self.applyPitch()

        return self.player

    def applyDecimate(self):
        return Degrade(self.player, srscale=self.effectStrength)

    def applyBitcrush(self):
        depth = self.effectStrength * 16;
        depth = int(depth)
        return Degrade(self.player, bitdepth=depth)

    def applyDelay(self):
        delay = float(1) * self.effectStrength
        print delay
        print self.effectStrength
        return Delay(self.player, delay=[delay, 0], feedback=0.5)

    def applyPitch(self):
        data = copy.copy(self.player)
        speed = 2 * self.effectStrength
        self.length = self.length * (1 / speed)
        data.setSpeed(speed)
        return data

    def setEffect(self, effect):
        self.effect = effect
        print effect
        print self.getName()

    def setEffectStrength(self, val):
        val = float(val)
        self.effectStrength = val / 100
        print self.effectStrength

    def setLatch(self, value):
        self.latch = value
        print value


