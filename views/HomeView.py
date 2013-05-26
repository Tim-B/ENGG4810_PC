from Tkinter import *
from views.widgets.SampleGrid import *
from views.widgets.SampleProperties import *
from views.widgets.SampleWave import *
from views.widgets.WavePanel import *
from threading import Thread

#This class generates the UI of home (the first) page of the program
class HomeView:
    #This function is called when the class is made
    def __init__(self, window, controller):
        self.window = window
        self.controller = controller

        self.controlPanel = Frame(self.window)
        self.controlPanel.grid(row=0, column=0, columnspan=2, pady=10)
        self.waveShown = False

        config = self.controller.getConfig()

        self.uploadBtn = Button(self.controlPanel, text="Upload to board", command=self.upload)
        self.uploadBtn.grid(column=5, row=1)

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

        self.tempo = Spinbox(self.controlPanel, from_=10, to=240, command=self.setTempo)
        self.tempo.grid(column=3, row=1)

        w = Label(self.controlPanel, text="Effect two:")
        w.grid(column=1, row=0)

        self.buttonTrackPanel = Frame(self.window)
        self.buttonTrackPanel.grid(row=1, column=0)
        self.sampleGrid = SampleGrid(controller, self.buttonTrackPanel)

        self.workspacePanel = Frame(self.window, bd=1, relief=GROOVE)
        self.workspacePanel.grid(row=1, column=1, sticky=W+E+N+S)
        self.sampleProperties = SampleProperties(controller, self.workspacePanel)

        self.timeLinePanel = Frame(self.window, bd=1, relief=GROOVE)
        self.timeLinePanel.grid(row=2, column=0, columnspan=2, sticky=W+E)
        self.sampleWave = SampleWave(controller, self.timeLinePanel)

        self.waveViewPanel = Frame(self.window, width=400, bd=1, relief=GROOVE)

        for i in range(0, 5):
            w = WavePanel(self.controller, self.waveViewPanel)

        self.createMenu()

    #Add the menu at the top with quit and load file
    def createMenu(self):
        self.menu = Menu(self.window)
        self.menu.add_command(label="Quit", command=self.window.quit)
        self.menu.add_command(label="Load config", command=self.controller.loadConfig)
        self.menu.add_command(label="Toggle wave panel", command=self.showWavePanel)
        self.window.config(menu=self.menu)

    def showWavePanel(self):
        if self.waveShown:
            self.waveViewPanel.grid_forget()
            self.waveShown = False
        else:
            self.waveViewPanel.grid(row=0, column=3, rowspan=3)
            self.waveShown = True


    def upload(self):
        self.uploadBtn.config(state=DISABLED);
        Thread(target=self.controller.upload()).start()
        self.uploadBtn.config(state=NORMAL);

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





