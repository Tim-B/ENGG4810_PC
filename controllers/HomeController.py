from views.HomeView import *
from models.Config import *
import tkFileDialog
from struct import *
import win32api
from sys import platform as _platform

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
        self.homeView = HomeView(root, self)
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

    def stopRec(self):
        self.pyo.recstop()

    def upload(self):
        initDir = '/'
        if not _platform == "darwin":
            driveInfo = win32api.GetVolumeInformation("H:\\")
            print driveInfo[0]
        dirName = tkFileDialog.askdirectory(title="Please select the root directory of the MPC device")
        if not dirName:
            print 'None selected'
            return
        cnt = 0
        for sample in self.samples:
            sampleModel = sample.getSample()
            if sampleModel is not None:
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
            if sample.getActive():
                val = 1
                if sample.getLatch():
                    val = val | 2
            data.append(val)

        data.append(int(self.tempo))
        data.append(self.getEffectIndex(self.effect1))
        data.append(self.getEffectIndex(self.effect2))

        print data

        filePath = path + '/mpc/mpc.txt'

        f = open(filePath, 'w+')
        f.write(pack('19B', *data))
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

    def loadConfig(self):
        fileOptions = {}
        fileOptions['filetypes'] = [('MPC config', 'mpc.txt')]
        fname = tkFileDialog.askopenfilename(**fileOptions)
        print fname
        if not fname:
            print 'None selected'
            return
        f = open(fname, 'r')
        data = f.read(19)
        f.close()
        print data
        data = unpack('19B', data)
        cnt = 0

        for sample in self.samples:
            if data[cnt] & 1:
                sample.setActive(1)
            else:
                sample.setActive(0)

            if data[cnt] & 2:
                sample.setLatch(1)
            else:
                sample.setLatch(0)

            cnt += 1

        tempo = int(data[cnt])
        self.homeView.tempo.delete(0,"end")
        self.homeView.tempo.insert(0,tempo)
        self.tempo = tempo
        cnt += 1

        effect1 = self.config.getEffectOptions()[data[cnt]]
        self.homeView.effect1Value.set(effect1)
        self.effect1 = effect1

        cnt += 1
        effect2 = self.config.getEffectOptions()[data[cnt]]
        self.homeView.effect2Value.set(effect2)
        self.effect2 = effect2

















