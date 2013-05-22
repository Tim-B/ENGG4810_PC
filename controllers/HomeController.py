from views.HomeView import *
from models.Config import *
import tkFileDialog
from struct import *

#This class handles all the main controllers of the program
class HomeController:

    homeView = None

    #Called to generate the first window of the program
    def homeAction(self):

        self.pyo = Server(audio="offline", nchnls=1, sr=44100).boot()
        self.pyo.recordOptions(dur=5, filename=None, fileformat=0, sampletype=3)

        self.config = Config()
        root = Tk()
        self.samples = []
        self.sampleCnt = 0
        HomeController.homeView = HomeView(root, self)
        self.effect1 = 'None'
        self.effect2 = 'None'
        self.tempo = 10
        root.mainloop()

    def loadSample(self, sample):
        self.homeView.loadSample(sample)

    def getConfig(self):
        return self.config

    def startRec(self, file):
        self.pyo.recstart(file)

    def stopRec(self) :
        self.pyo.recstop()

    def upload(self):
        dirName = tkFileDialog.askdirectory(title="Please select the root directory of the MPC device")
        if not dirName:
            print 'None selected'
            return
        cnt = 0
        for sample in self.samples :
            sampleModel = sample.getSample()
            if sampleModel is not None :
                sampleModel.export(self, cnt, dirName)
            cnt += 1
        self.generateConfig(dirName)


    def registerUISample(self, sample):
        self.samples.append(sample)

    def generateConfig(self, path):
        data = []
        sActive = 0
        val = 0
        for sample in self.samples:
            val = 0
            sampleModel = sample.getSample()
            if sampleModel is not None:
                val = 1
                if sampleModel.latch is True:
                    val = val | 2
            data.append(val)


        other = 0
        if self.config.lfo:
            other = other | 1

        data.append(int(self.tempo))
        data.append(self.getEffectIndex(self.effect1))
        data.append(self.getEffectIndex(self.effect2))
        data.append(other)

        print data

        filePath = path + '/mpc/mpc.txt'

        f = open(filePath, 'w+')
        f.write(pack('20B', *data))
        f.close()

    def setEffect(self, pos, value):
        if pos == 0:
            self.effect1 = value

        if pos == 1:
            self.effect2 = value

    def getEffectIndex(self, value):
        cnt = 0
        for effect in self.config.getEffectOptions():
            if effect == value:
                return cnt
            cnt += 1
        return 0

















