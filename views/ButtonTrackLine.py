from Tkinter import *

class ButtonTrackLine:

    buttonTrack = None
    parent = None
    container = None
    trackVar = None

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
        option = OptionMenu(self.container, self.trackVar, "None")
        option.pack(side = LEFT)

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
        print self.trackVar.get()