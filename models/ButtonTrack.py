class ButtonTrack:

    name = None
    player = None

    def __init__(self, name):
        self.name = "Button " + str(name)

    def getName(self):
        return self.name

    def setPlayer(self, player):
        self.player = player
        print self.player

    def start(self):
        if self.player is None:
            return
        self.player.out()

    def stop(self):
        if self.player is None:
            return
        self.player.stop()