from Tkinter import *
from views.ButtonTrackLine import *
from views.WorkspacePanel import *

#This class generates the UI of home (the first) page of the program
class HomeView:
    #This stores an instance of the program window
    window = None
    #This stores an instance of the program menu
    menu = None

    buttonTrackPanel = None
    timeLinePanel = None
    workspacePanel = None
    controlPanel = None

    buttonTrackList = []

#This function is called when the class is made
    def __init__(self, window):
        self.window = window

        self.controlPanel = Frame()
        self.controlPanel.grid(row=1, column=1, columnspan=2);

        w = Button(self.controlPanel, text="Play")
        w.pack(side = LEFT)

        w = Button(self.controlPanel, text="Stop")
        w.pack(side = LEFT)

        w = Button(self.controlPanel, text="Loop")
        w.pack(side = LEFT)

        self.buttonTrackPanel = Frame()
        self.buttonTrackPanel.grid(row=2, column=1);

        self.workspacePanel = Frame()
        self.workspacePanel.grid(row=2, column=2);

        self.timeLinePanel = Frame()
        self.timeLinePanel.grid(row=3, column=1, columnspan=2);

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