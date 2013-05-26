__author__ = 'Tim'
from Tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.lines import Line2D
from numpy import arange, cos, sin, pi

class WavePanel:

    def __init__(self, controller, parent):
        self.parent = parent
        self.controller = controller
        self.container = Frame(self.parent, width = 800, height=300)
        w = Label(self.container, text="Select sample number")
        w.grid(row=0, column=0)
        self.sampVal = StringVar(self.container)
        self.sampSelect = OptionMenu(self.container, self.sampVal, *range(0, 16), command=self.loadSample)
        self.sampSelect.grid(row=0, column=1)

        self.sample = None
        self.figure = Figure(figsize=(5,1), dpi=120)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.container)
        self.canvas._tkcanvas.config(background="white")

        self.canvas.get_tk_widget().grid(row=2, column = 0, columnspan=2)

        self.container.pack()


    def loadSample(self, val):
        print int(self.sampVal.get())
        sample = self.controller.samples[int(self.sampVal.get())]
        sample = sample.getSample()
        if sample is None:
            print "No sample"
            return
        self.sample = sample
        self.figure.clf()
        #self.figure.tight_layout()
        self.plot = self.figure.add_subplot(111, frameon=False)
        self.plot.axis('off')
        t = sample.getSoundPoints()
        #print t
        self.plot.plot(t)
        self.canvas.show()
        self.canvas.draw()



