class ButtonTrack:

    name = None
    player = None

    def __init__(self, name):
        self.name = "Button " + str(name)

    def getName(self):
        return self.name

    def setPlayer(self, player):
        self.player = player

    def start(self):
        if self.player == None:
            return
        self.player.out()

    def stop(self):
        if self.player == None:
            return
        self.player.stop()