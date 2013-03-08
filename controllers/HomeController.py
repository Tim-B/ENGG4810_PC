from views.HomeView import *

import tkFileDialog
import tkMessageBox

#This class handles all the main controllers of the program
class HomeController:

    #Called to generate the first window of the program
    @staticmethod
    def homeAction():
        root = Tk()
        view = HomeView(root)
        root.mainloop()