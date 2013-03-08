from controllers.HomeController import *
from pyo import *

pyoInstance = None;

def getPyo():
    return pyoInstance;


def main():
    pyoInstance = Server().boot()
    pyoInstance.start()

    #snd = "C:\Users\Tim\Downloads\SamplesWav - All in one\SamplesWav - All in one\Bass & Synth\Bass1.wav"
    #sf = SfPlayer(snd, speed=[.75,.8], loop=True, mul=.3).out()
    HomeController.homeAction()

#Invoke the main function    
main()