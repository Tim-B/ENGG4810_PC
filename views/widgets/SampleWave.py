__author__ = 'Tim'
from Tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.lines import Line2D
from numpy import arange, cos, sin, pi

class SampleWave:

    def __init__(self, controller, parent):
        self.parent = parent
        self.controller = controller
        self.startLine = None
        self.endLine = None
        self.container = Frame(self.parent, width = 800, height = 300)
        self.sample = None
        self.displayed = False
        self.startScale = Scale(self.container, from_=1, to=10000, orient=HORIZONTAL, command=self.line, label="Start cursor", showvalue=0)
        self.startScale.grid(row=1, column=0)
        self.endScale = Scale(self.container, from_=1, to=10000, orient=HORIZONTAL, command=self.line, label="End cursor", showvalue=0)
        self.endScale.grid(row=1, column=1)
        self.endScale.set(10000)
        self.figure = Figure(figsize=(5,1), dpi=120)
        #self.figure.tight_layout()
        self.plot = self.figure.add_subplot(111)
        t = arange(0.0,3.0,0.01)
        s = sin(2*pi*t)

        self.plot.plot(t,s)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.container)
        self.canvas._tkcanvas.config(background="white")

        self.canvas.get_tk_widget().grid(row=2, column = 0, columnspan=2)

        #self.container.pack()


    def line(self, val):
        if self.startLine is None or self.endLine is None:
            return
        self.plot.lines.remove(self.startLine)
        self.plot.lines.remove(self.endLine)
        startVal = self.startScale.get()
        endVal = self.endScale.get()

        if startVal >= endVal :
            startVal = endVal - 1;
            self.startScale.set(startVal)
            self.endScale.set(endVal)

        startVal = float(startVal) / float(10000)
        endVal = float(endVal) / float(10000)

        self.sample.startCut = startVal
        self.sample.endCut = endVal

        #print self.sample.plotPoints
        startVal = startVal * self.sample.plotPoints
        endVal = endVal * self.sample.plotPoints
        valX = [startVal, startVal]
        valY = [-1, 1]
        self.startLine = Line2D(valX, valY, color='red');
        self.plot.add_line(self.startLine)
        valX = [endVal, endVal]
        self.endLine = Line2D(valX, valY, color='red');
        self.plot.add_line(self.endLine)
        self.canvas.draw()

    def loadSample(self, sample):
        if not self.displayed:
            self.container.pack()
            self.displayed = True
        self.sample = sample
        self.figure.clf()
        #self.figure.tight_layout()
        self.plot = self.figure.add_subplot(111, frameon=False)
        self.plot.axis('off')
        t = sample.getSoundPoints()
        #print t
        self.plot.plot(t)

        self.startScale.set(self.sample.startCut * 10000)
        self.endScale.set(self.sample.endCut * 10000)

        startVal = self.sample.plotPoints * self.sample.startCut
        endVal = self.sample.plotPoints * self.sample.endCut

        valX = [startVal, startVal]
        valY = [-1, 1]
        self.startLine = Line2D(valX, valY, color='red');
        self.plot.add_line(self.startLine)

        valX = [endVal, endVal]
        self.endLine = Line2D(valX, valY, color='red');
        self.plot.add_line(self.endLine)

        self.canvas.show()
        self.canvas.draw()



