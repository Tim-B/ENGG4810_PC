__author__ = 'Tim'
from Tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import arange, cos, sin, pi

class SampleWave:

    def __init__(self, controller, parent):
        self.parent = parent
        self.controller = controller
        self.container = Frame(self.parent, width = 800, height = 300)
        self.sample = None

        self.figure = Figure(figsize=(5,1), dpi=120)
        #self.figure.tight_layout()
        self.plot = self.figure.add_subplot(111)
        t = arange(0.0,3.0,0.01)
        s = sin(2*pi*t)

        self.plot.plot(t,s)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.container)
        self.canvas._tkcanvas.config(background="white")

        self.canvas.get_tk_widget().pack()

        self.container.pack()

    def loadSample(self, sample):
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



