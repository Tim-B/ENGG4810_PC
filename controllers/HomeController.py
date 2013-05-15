from views.HomeView import *
from models.Config import *

#This class handles all the main controllers of the program
class HomeController:

    homeView = None

    #Called to generate the first window of the program
    def homeAction(self):
        self.config = Config()
        root = Tk()
        HomeController.homeView = HomeView(root, self)
        root.mainloop()

    def loadSample(self, sample):
        self.homeView.loadSample(sample)

    def getConfig(self):
        return self.config

