from Tkinter import *
from models.SampleWorkspace import *
import tkFileDialog

class WorkspacePanel:

    parent = None
    container = None
    workspace = None
    sampleList = None
    trackList = None

    #This function is called when the class is made
    def __init__(self, panel, trackList):
        self.trackList = trackList
        self.parent = panel
        self.workspace = SampleWorkspace.getInstance()

        self.container = Frame(self.parent)
        sampleList = Listbox(self.container)
        sampleList.pack()
        self.sampleList = sampleList

        addButton = Button(self.container, text="Add track", command=self.findFile)
        addButton.pack()

        self.container.pack()

    def findFile(self):
        fileOptions = {}
        fileOptions['filetypes'] = [('all files', '.*'), ('wave files', '.wav')]
        fname = tkFileDialog.askopenfilename()
        self.workspace.addSample(fname)
        self.reload()

    def reload(self):
        items = self.workspace.getSampleList()
        self.sampleList.delete(0, END)
        for item in items:
            self.sampleList.insert(END, item.getName())
        for track in self.trackList:
            track.updateList()