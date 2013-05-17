from pyo import *
import ntpath

__author__ = 'Tim'


class Sample:
    def __init__(self, path):
        self.path = path
        self.name = ntpath.basename(path)
        self.player = SfPlayer(path)
        self.player = Delay(self.player, delay=1, feedback=0.5)
        self.table = SndTable(self.path, chnl=0)
        self.length = self.table.getDur()
        self.effect = None
        print(path)

    def getName(self):
        return self.name

    def getSoundPoints(self):
        self.table.view()
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
        #data = self.applyEffect()
        if not os.path.isdir(dir) :
             os.makedirs(dir)

        controller.pyo.recordOptions(dur=self.length, filename=samplePath, fileformat=0, sampletype=3)
        self.player.out()
        controller.pyo.start()

    def applyEffect(self):
        sound = TableRead(self.table)
        # self.applyDelay(sound)
        return sound

    def applyDelay(self, sound):
        Delay(sound, delay=1, feedback=0)

    def setEffect(self, effect):
        self.effect = effect
        print effect
        print self.getName()


