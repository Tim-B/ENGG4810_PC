from Tkinter import *
from ttk import *

from models.SampleWorkspace import *

class ButtonTrackLine:

    #This function is called when the class is made
    def __init__(self, panel, buttonTrack):
        print buttonTrack.getName()
        self.parent = panel
        self.buttonTrack = buttonTrack
        self.container = Frame(self.parent)
        w = Label(self.container, text=buttonTrack.getName())
        w.pack(side = LEFT)
        self.trackVar = StringVar(self.container)
        self.trackVar.set("None")
        self.trackVar.trace("w", self.updateTrack)
        option = Combobox(self.container, textvariable=self.trackVar, state='readonly')
        option.pack(side = LEFT)
        self.trackList = option

        play = Button(self.container, text="Play")
        play.bind("<Button-1>", self.startTrack)
        play.bind("<ButtonRelease-1>", self.stopTrack)
        play.pack()

        self.container.pack()

    def startTrack(self, event):
        self.buttonTrack.start()

    def stopTrack(self, event):
        self.buttonTrack.stop()

    def updateTrack(self, *args):
        index = self.trackList.current()
        sample = SampleWorkspace.getInstance().getSampleIndex(index)
        self.buttonTrack.setPlayer(sample.getPlayer())

    def updateList(self):
        self.trackList['values'] = tuple(SampleWorkspace.getInstance().getSampleList())
