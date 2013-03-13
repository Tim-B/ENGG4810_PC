from models.LoopTrack import *

class LoopController:

    loopTrackList = []
    currentLoopSlot = 0
    loopOn = False

    @classmethod
    def setupLoops(self, target):
        self.view = target
        for i in range(0, 5):
            track = LoopTrack(i)
            self.view.addLoopTrack(track)
            self.loopTrackList.append(track)

    @classmethod
    def loopAction(cls):
        track = LoopController.loopTrackList[LoopController.currentLoopSlot]
        if LoopController.loopOn:
            track.stopCapture()
            LoopController.loopOn = False
            LoopController.currentLoopSlot += 1
        else:
            track.startCapture()
            LoopController.loopOn = True
1


