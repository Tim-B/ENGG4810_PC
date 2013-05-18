__author__ = 'Tim'
from Tkinter import *


class SampleProperties:
    def __init__(self, controller, parent):
        self.parent = parent
        self.controller = controller
        self.displayed = False

        self.outer = Frame(self.parent, width=250, height=200)

        self.container = Frame(self.outer)
        self.nameLabel = Label(self.container, text="Effect")
        self.nameLabel.grid(row=0, column=0)

        self.effectValue = StringVar(self.container)
        self.effectSelect = OptionMenu(self.container, self.effectValue, "None", "Delay", "Echo", "Pitch Shift", "Decimator", "Bitcrusher", command=self.setEffect)
        self.effectSelect.config(width=20)
        self.effectSelect.grid(row=1, column=0)
        self.effectValue.set("None")

        w = Label(self.container, text="Effect Strength")
        w.grid(row=5, column=0)
        self.effectSlider = Scale(self.container, from_=0, to=100, orient=HORIZONTAL, command=self.setEffectStrength)
        self.effectSlider.grid(row=6, column=0)

        w = Label(self.container, text="Mode")
        w.grid(row=7, column=0)
        self.modeValue = StringVar(self.container)
        self.modeSelect = OptionMenu(self.container, self.modeValue, "Hold", "Latch", command=self.setMode)
        self.modeSelect.config(width=20)
        self.modeSelect.grid(row=8, column=0)

        self.modeValue.set("Hold")
        self.sample = None

        self.helpLabel = Label(self.outer, text="Load sample then click properties")
        self.helpLabel.pack()
        self.outer.pack()

    def loadSample(self, sample):
        if not self.displayed:
            self.helpLabel.pack_forget()
            self.container.pack()
            self.displayed = True
        self.sample = sample
        self.effectValue.set(self.sample.effect)
        print self.sample.effectStrength
        self.effectSlider.set(self.sample.effectStrength * 100)
        if(self.sample.latch):
            self.modeValue.set("Latch")
        else:
            self.modeValue.set("Hold")

    def setEffect(self, value):
        if self.sample != None :
            self.sample.setEffect(self.effectValue.get())

    def setEffectStrength(self, value):
        if self.sample != None :
            self.sample.setEffectStrength(self.effectSlider.get())

    def setMode(self, value):
        if self.sample is not None:
            if self.modeValue.get() == 'Hold':
                self.sample.setLatch(False)
            else:
                self.sample.setLatch(True)


