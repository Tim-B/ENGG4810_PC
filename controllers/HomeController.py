from views.HomeView import *
from models.Config import *
import tkFileDialog
from pyo import *

#This class handles all the main controllers of the program
class HomeController:

    homeView = None

    #Called to generate the first window of the program
    def homeAction(self):

        self.pyo = Server(audio="offline").boot()
        self.pyo.recordOptions(dur=5, filename=None, fileformat=0, sampletype=3)

        self.config = Config()
        root = Tk()
        self.samples = []
        self.sampleCnt = 0
        HomeController.homeView = HomeView(root, self)
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
        print dirName
        cnt = 0
        for sample in self.samples :
            sampleModel = sample.getSample()
            if sampleModel != None :
                sampleModel.export(self, cnt, dirName)
            cnt += 1


    def registerUISample(self, sample):
        self.samples.append(sample)

