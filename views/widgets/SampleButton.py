from Tkinter import *
from models.Sample import *
import tkFileDialog

__author__ = 'Tim'


class SampleButton:
    def __init__(self, controller, parent):
        self.parent = parent
        self.controller = controller
        self.container = Frame(self.parent, bd=1, relief=SUNKEN, padx=5, pady=5)
        Frame(self.parent)
        self.fileName = StringVar()
        self.fileNameLabel = Label(self.container, textvariable = self.fileName)
        self.addButton = Button(self.container, text="Load sample", command=self.loadSample)
        self.propertiesButton = Button(self.container, text="Properties", command=self.sampleProperties, state=DISABLED)
        self.active = IntVar()
        active = Checkbutton(self.container, text="Sample active", variable=self.active)
        self.latch = IntVar()
        latch = Checkbutton(self.container, text="Latch", variable=self.latch)
        self.fileNameLabel.pack()
        self.propertiesButton.pack()
        self.addButton.pack()
        active.pack()
        latch.pack()
        self.container.pack()
        self.sample = None
        self.refresh()
        controller.registerUISample(self)

    def grid(self, x, y):
        self.container.grid(row=x, column=y)

    def setSample(self, sample):
        self.sample = sample
        self.active.set(1)
        self.refresh()


    def loadSample(self):
        fileOptions = {}
        fileOptions['filetypes'] = [('all files', '.*'), ('wave files', '.wav')]
        fname = tkFileDialog.askopenfilename()
        print fname
        if not fname:
            print 'None selected'
            return
        sample = Sample(fname)
        self.setSample(sample)


    def refresh(self):
        if self.sample is not None:
            print "not one"
            self.fileName.set(self.sample.getName())
            self.propertiesButton.config(state=NORMAL);
        else:
            print "none"
            self.propertiesButton.config(state=DISABLED);
            self.fileName.set("None set")

    def sampleProperties(self):
        self.controller.loadSample(self.sample)

    def getSample(self):
        return self.sample

    def getActive(self):
        return self.active.get()

    def getLatch(self):
        return self.latch.get()

    def setLatch(self, value):
        self.latch.set(value)

    def setActive(self, value):
        self.active.set(value)