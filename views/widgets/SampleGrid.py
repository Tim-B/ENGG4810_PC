from views.widgets.SampleButton import *

__author__ = 'Tim'


class SampleGrid:
    def __init__(self, controller, parent):
        self.parent = parent
        self.controller = controller
        self.container = Frame(self.parent)
        Frame(self.parent)
        self.samples = []
        self.x = 0
        self.y = 0

        for x in range(0, 16):
            self.__addSample()

        self.container.pack()

    def __addSample(self):
        sample = SampleButton(self.controller, self.container)
        self.samples.append(sample)
        sample.grid(self.x, self.y)
        self.x += 1
        if self.x > 3:
            self.x = 0
            self.y += 1
            if self.y > 3:
                self.y = 0


