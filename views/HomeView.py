from Tkinter import *
from views.widgets.SampleGrid import *
from views.widgets.SampleProperties import *
from views.widgets.SampleWave import *

#This class generates the UI of home (the first) page of the program
class HomeView:
    #This function is called when the class is made
    def __init__(self, window, controller):
        self.window = window
        self.controller = controller

        self.controlPanel = Frame(self.window)
        self.controlPanel.grid(row=0, column=0, columnspan=2)

        config = self.controller.getConfig()

        w = Button(self.controlPanel, text="Upload to board", command=self.controller.upload)
        w.grid(column=4, row=0)
        self.effectValue = StringVar(self.controlPanel)
        w = OptionMenu(self.controlPanel, self.effectValue, *config.getEffectOptions())
        w.config(width=20)
        w.grid(column=1, row=0)

        w = Label(self.controlPanel, text="Effect one:")
        w.grid(column=0, row=0)

        w = OptionMenu(self.controlPanel, self.effectValue, *config.getEffectOptions())
        w.config(width=20)
        w.grid(column=1, row=1)

        w = Label(self.controlPanel, text="Effect two:")
        w.grid(column=0, row=1)

        self.buttonTrackPanel = Frame(self.window)
        self.buttonTrackPanel.grid(row=1, column=0)
        self.sampleGrid = SampleGrid(controller, self.buttonTrackPanel)

        self.workspacePanel = Frame(self.window)
        self.workspacePanel.grid(row=1, column=1)
        self.sampleProperties = SampleProperties(controller, self.workspacePanel)

        self.timeLinePanel = Frame(self.window)
        self.timeLinePanel.grid(row=2, column=0, columnspan=2)
        self.sampleWave = SampleWave(controller, self.timeLinePanel)

        self.createMenu()

    #Add the menu at the top with quit and load file
    def createMenu(self):
        self.menu = Menu(self.window)
        self.menu.add_command(label="Quit", command=self.window.quit)
        self.window.config(menu=self.menu)

    def loadSample(self, sample):
        self.sampleProperties.loadSample(sample)
        self.sampleWave.loadSample(sample)

    def getController(self):
        return self.controller





