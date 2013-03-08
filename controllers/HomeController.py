from views.HomeView import *
from models.ButtonTrack import *

#This class handles all the main controllers of the program
class HomeController:

    #Called to generate the first window of the program
    @staticmethod
    def homeAction():
        root = Tk()
        view = HomeView(root)
        for i in range(0, 12):
            track = ButtonTrack(i)
            view.addButtonTrack(track)
        root.mainloop()