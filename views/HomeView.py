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
        w.grid(column=4, row=1)
        self.effect1Value = StringVar(self.controlPanel)
        self.effect1Value.set("None")
        self.effect1Value.trace('w', self.effectChanged)
        w = OptionMenu(self.controlPanel, self.effect1Value, *config.getEffectOptions())
        w.config(width=20)
        w.grid(column=0, row=1)

        w = Label(self.controlPanel, text="Effect one:")
        w.grid(column=0, row=0)

        self.effect2Value = StringVar(self.controlPanel)
        self.effect2Value.set("None")
        self.effect2Value.trace('w', self.effectChanged)
        w = OptionMenu(self.controlPanel, self.effect2Value, *config.getEffectOptions())
        w.config(width=20)
        w.grid(column=1, row=1)

        w = Label(self.controlPanel, text="Tempo:")
        w.grid(column=3, row=0)

        self.tempo = Spinbox(self.controlPanel, from_=10, to=240, command = self.setTempo)
        self.tempo.grid(column=3, row=1)

        w = Label(self.controlPanel, text="Effect two:")
        w.grid(column=1, row=0)

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

    def effectChanged(self, one, two, three):
        self.controller.setEffect(0, self.effect1Value.get())
        self.controller.setEffect(1, self.effect2Value.get())

    def setTempo(self):
        self.controller.tempo = self.tempo.get()
        print self.controller.tempo





