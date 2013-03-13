from Tkinter import *
import models.PyoContainer as pyo

class LoopTrackPanel:

    #This function is called when the class is made
    def __init__(self, panel, loopTrack):
        self.loopTrack = loopTrack
        self.parent = panel

        self.container = Frame(self.parent)

        self.controlPanel = Frame(self.container)

        w = Label(self.controlPanel, text="Volume")
        w.pack()

        slide = Scale(self.controlPanel, from_=0, to=100, orient=HORIZONTAL)
        slide.pack()

        self.controlPanel.pack(side = LEFT)

        self.wavePanel = Frame(self.container)

        self.waveGraph = Canvas(self.wavePanel)
        self.waveGraph.pack(fill="both", expand=1)
        self.waveGraph.update()

        self.wavePanel.update()

        self.wavePanel.pack(side = RIGHT)

        self.container.pack()

        self.loopTrack.registerForUpdate(self)

    def loopNotify(self):
        self.waveGraph.delete(ALL)
        data = self.loopTrack.getSoundPoints(300)
        data = data[0]
        count = 0
        point = 0
        prevx = 0
        for i in data:
            point = round(i * 200) + 100
            self.waveGraph.create_line((count, point, count-1, prevx), fill="black")
            print (count, point)
            count += 1
            prevx = point
        self.waveGraph.update()
        pyoInst = pyo.PyoContainer.INSTANCE
        print pyoInst.getSamplingRate()

