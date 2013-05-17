__author__ = 'Tim'
from Tkinter import *


class SampleProperties:
    def __init__(self, controller, parent):
        self.parent = parent
        self.controller = controller
        self.container = Frame(self.parent, width=200, height=200)
        self.nameLabel = Label(self.container, text="Effect")
        self.nameLabel.grid(row=0, column=0)

        self.effectValue = StringVar(self.container)
        self.effectSelect = OptionMenu(self.container, self.effectValue, "None", "Delay", "Echo", "Pitch Shift", "Decimator", "Bitcrusher", command=self.setEffect)
        self.effectSelect.config(width=20)
        self.effectSelect.grid(row=1, column=0)
        self.effectValue.set("None")

        w = Label(self.container, text="Mode")
        w.grid(row=5, column=0)
        self.modeValue = StringVar(self.container)
        self.modeSelect = OptionMenu(self.container, self.modeValue, "Hold", "Latch")
        self.modeSelect.config(width=20)
        self.modeSelect.grid(row=6, column=0)

        self.modeValue.set("Hold")
        self.sample = None

        self.container.pack()

    def loadSample(self, sample):
        self.sample = sample

    def setEffect(self, value):
        if self.sample != None :
            self.sample.setEffect(self.effectValue.get())

