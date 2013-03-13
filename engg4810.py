from models.PyoContainer import *
from controllers.HomeController import *
from pyaudio import *

def main():
    PyoContainer.start()
    p = PyAudio()
    CHUNK = 1024
    FORMAT = paInt16
    CHANNELS = 2
    RATE = 44100
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print stream.read(1024)
    HomeController.homeAction()

#Invoke the main function    
main()