from pyo import *
import ntpath
import copy
import subprocess
import tempfile
from sys import platform as _platform

__author__ = 'Tim'


class Sample:
    def __init__(self, path):
        self.path = path
        self.name = ntpath.basename(path)
        if self.path.lower().endswith('mp3'):
            tf = tempfile.NamedTemporaryFile(mode='r', delete=False)
            ffmpegPath = 'third_party/ffmpeg/ffmpeg.exe'
            if _platform == "darwin":
                ffmpegPath = 'third_party/ffmpeg/ffmpeg'
            mp3Path = tf.name
            print mp3Path
            output = subprocess.Popen([ffmpegPath, '-i', self.path, '-f', 'wav', mp3Path, '-y'],
                                      stdout=subprocess.PIPE).communicate()
            self.path = mp3Path
        self.player = SfPlayer(self.path)
        self.table = SndTable(self.path, chnl=0)
        self.length = self.table.getDur()
        self.effect = 'None'
        self.effectStrength1 = float(0)
        self.effectStrength2 = float(0)
        self.plotPoints = 0
        self.startCut = 0.0
        self.endCut = 1.0
        self.attack = 0.1
        self.decay = 0.2
        self.release = 0.8
        self.sustain = 0.5
        print(path)

    def getName(self):
        return self.name

    def getSoundPoints(self):
        size = self.table.getSize();
        data = self.table.getEnvelope(size)[0]
        if size > (44100 * 10):
            dS = []
            self.plotPoints = 0
            for i in xrange(0, size, 500):
                dS.append(data[i])
                self.plotPoints += 1
            return dS
        self.plotPoints = size
        return data

    def export(self, controller, sampleIndex, path):
        dir = path + '/mpc/'
        samplePath = dir + str(sampleIndex) + '.wav'

        dur = self.length * (self.endCut - self.startCut)
        start = self.length * self.startCut
        smp = copy.copy(self.player)
        smp.setOffset(start)
        data = self.applyEffect(smp)
        if not os.path.isdir(dir):
            os.makedirs(dir)

        if os.path.isfile(samplePath):
            os.remove(samplePath)

        attack = self.attack * dur
        decay = self.decay * dur
        release = self.release * dur
        print attack
        print decay
        print release
        adsr = Adsr(attack=attack, decay=decay, release=release, dur=dur, sustain=self.sustain)
        print data.mul
        data.setMul(adsr * data.mul)
        controller.pyo.recordOptions(dur=dur, filename=samplePath, fileformat=0, sampletype=3)
        print controller.pyo.getSamplingRate()
        print controller.pyo.getNchnls()
        adsr.play()
        if self.effect == 'Delay' or self.effect == 'Echo':
            print 'Playing first'
            self.player.setMul(adsr)
            self.player.out()
        data.out()
        controller.pyo.start()
        self.length = self.table.getDur()
        if self.effect == 'Delay' or self.effect == 'Echo':
            self.player.setMul(1)
            self.player.stop()



    def applyEffect(self, smp):
        print self.effect

        if self.effect == 'Echo':
            print 'Applying Echo'
            return self.applyEcho(smp)

        if self.effect == 'Delay':
            print 'Applying delay'
            return self.applyDelay(smp)

        if self.effect == 'Decimator':
            print 'Applying decimator'
            return self.applyDecimate(smp)

        if self.effect == 'Bitcrusher':
            print 'Apply bitcrush'
            return self.applyBitcrush(smp)

        if self.effect == 'Pitch Shift':
            print 'Pitch shift'
            return self.applyPitch(smp)

        return smp

    def applyDecimate(self, data):
        return Degrade(data, srscale=self.effectStrength1)

    def applyBitcrush(self, data):
        depth = self.effectStrength1 * 16;
        depth = int(depth)
        return Degrade(data, bitdepth=depth)

    def applyEcho(self, data):
        delay = float(4) * self.effectStrength1
        print delay
        return Delay(data, delay=[delay], feedback=self.effectStrength2)

    def applyDelay(self, data):
        delay = float(4) * self.effectStrength1
        feedback = self.effectStrength2
        return SDelay(data, delay=[delay],mul=feedback, maxdelay=self.length + delay)

    def applyPitch(self, data):
        speed = 1.5 * self.effectStrength1 + 0.5
        self.length = self.length * (1 / speed)
        data.setSpeed(speed)
        start = self.length * self.startCut
        data.setOffset(start)
        return data

    def setEffect(self, effect):
        self.effect = effect
        print effect
        print self.getName()

    def setEffectStrength(self, param, val):
        val = float(val)
        val = val / 100
        if param == 0:
            self.effectStrength1 = val
        else:
            self.effectStrength2 = val
        print val


