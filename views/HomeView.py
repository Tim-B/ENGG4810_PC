from Tkinter import *
from views.ButtonTrackLine import *
from views.WorkspacePanel import *
from views.LoopTrackPanel import *
from controllers.LoopController import *

#This class generates the UI of home (the first) page of the program
class HomeView:

    #This function is called when the class is made
    def __init__(self, window):

        self.buttonTrackList = []

        self.window = window

        self.controlPanel = Frame(self.window)
        self.controlPanel.grid(row=0, column=0, columnspan=2)

        w = Button(self.controlPanel, text="Play")
        w.pack(side = LEFT)

        w = Button(self.controlPanel, text="Stop")
        w.pack(side = LEFT)

        w = Button(self.controlPanel, text="Loop", command=LoopController.loopAction)
        w.pack(side = LEFT)

        self.buttonTrackPanel = Frame(self.window)
        self.buttonTrackPanel.grid(row=1, column=0)

        self.workspacePanel = Frame(self.window)
        self.workspacePanel.grid(row=1, column=1)

        self.timeLinePanel = Frame(self.window)
        self.timeLinePanel.grid(row=2, column=0, columnspan=2)

        workspacePanel = WorkspacePanel(self.workspacePanel, self.buttonTrackList)

        self.createMenu()

    #Add the menu at the top with quit and load file
    def createMenu(self):
        self.menu = Menu(self.window)
        self.menu.add_command(label="Quit", command=self.window.quit)
        self.window.config(menu=self.menu)

    def addButtonTrack(self, track):
        buttonTrack = ButtonTrackLine(self.buttonTrackPanel, track)
        self.buttonTrackList.append(buttonTrack)

    def addLoopTrack(self, track):
        loopTrack = LoopTrackPanel(self.timeLinePanel, track)


