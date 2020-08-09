import module_manager
module_manager.review()

from tkinter import *
import random
import string
import pyaudio
import wave
import sys
import time
from array import array
from struct import pack

def init(data):
    data.note = 'C1'
    data.duration = 10
    data.sound = str(data.note)+ '.wav'
def playSpecificNote(note,duration):
    
    sound = str(note)+ '.wav'
    
    print('hi')
    play('sounds/'+ sound)

def play(file):
    CHUNK = 1024 #measured in bytes

    wf = wave.open(file, 'rb')
    
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(CHUNK)
    

    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    
    stream.stop_stream()
    stream.close()

    p.terminate()
    
def timerFired(data):
    data.duration -=1
    while data.duration > 0:
        playSpecificNote(data.note,data.duration)
        
def keyPressed(event,data):
    pass
           
def mousePressed(event,data):
    pass
def redrawAll(canvas,data):
    pass
    

###default run-function
def run(width, height):
    # def redrawAllWrapper(canvas, data):
    #     canvas.delete(ALL)
    #     canvas.create_rectangle(0, 0, data.width, data.height,
    #                             fill='white', width=0)
    #     redrawAll(canvas, data)
    #     canvas.update()    

    # def mousePressedWrapper(event, canvas, data):
    #     mousePressed(event, data)
    #     redrawAllWrapper(canvas, data)

   ##   def keyPressedWrapper(event, canvas, data):
    #     keyPressed(event, data)
    #     redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    # canvas = Canvas(root, width=data.width, height=data.height)
    # canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")




#characters that map to certain notes on piano

    
  