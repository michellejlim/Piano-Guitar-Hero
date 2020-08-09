# Michelle Lim
from tkinter import *
import random
import string
import threading
import pyaudio
import wave
import sys
import time
from array import array
from struct import pack

####################################
# init
####################################
def init(data):
    #downloaded the images from jesse kuntz github piano images
    data.whiteKey = PhotoImage(file = "pictures/white_key.gif")
    data.whiteKeyPressed = PhotoImage(file = "pictures/white_key_pressed.gif")
    data.blackKey = PhotoImage(file = "pictures/black_key.gif")
    data.blackKeyPressed = PhotoImage(file = "pictures/black_key_pressed.gif")
    
    #downloaded the sounds of piano from jesse kuntz github piano sounds
    data.sound = None
    data.keyIndex = 0
    data.whiteKeySize = 50
    data.blackKeySize = 30
    data.whiteKeyStart = 0
    data.whiteKeyEnd = 0
    data.blackKeyStart = 80
    data.blackKeyEnd = 0
    data.note = 'C1'
    data.currKey = None
    data.duration = 5
    data.noteLength = 0
    data.startPressed = 0
    data.notePressed = False
    data.noteKey = {
    'z': 'C1',
    'x': 'D1',
    'c': 'E1',
    'v': 'F1',
    'b': 'G1',
    'n': 'A1',
    'm': 'B1',
    's': 'C#1',
    'd': 'D#1',
    'g': 'F#1',
    'h': 'G#1',
    'j': 'A#1',
    'Z': 'C2',
    'X': 'D2',
    'C': 'E2',
    'V': 'F2',
    'B': 'G2',
    'N': 'A2',
    'M': 'B2',
    'S': 'C#2',
    'D': 'D#2',
    'G': 'F#2',
    'H': 'G#2',
    'J': 'A#2',
}
    data.noteTime = {
     'C1':2,
     'D1':2,
    'E1':2,
     'F1':2,
     'G1':2,
     'A1':2,
     'B1':2,
     'C#1':2,
     'D#1':2,
     'F#1':2,
     'G#1':2,
     'A#1':2,
     'C2':2,
     'D2':2,
     'E2':2,
     'F2':2,
     'G2':2,
     'A2':2,
     'B2':2,
     'C#2':2,
     'D#2':2,
     'F#2':2,
     'G#2':2,
     'A#2':2,
}
    data.keyPos = {
            50: 'C1',
            80: 'C#1',
            100: 'D1',
            125: 'D#1',
            150: 'E1',
            200: 'F1',
            230: 'F#1',
            250: 'G1',
            275: 'G#1',
            300: 'A1',
            320: 'A#1',
            350: 'B1',
            400: 'C2',
            425: 'C#2',
            450: 'D2',
            470: 'D#2',
            500: 'E2',
            550: 'F2',
            575: 'F#2',
            600: 'G2',
            620: 'G#2',
            650: 'A2',
            665: 'A#2',
            700: 'B2'
        }
        

    # play('sounds/'+str(note)+'.wav')
def playSpecificNote(note,duration):
    sound = str(note)+ '.wav'
    duration -=1
    while duration >0:
        print('hello')
        play('sounds/'+ sound)
#got play and record functions from pyaudio tutorial homepage
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


###########################################################################
######################### Recording a WAV file ############################
###########################################################################
def record(outputFile):
    CHUNK = 1024 #measured in bytes
    FORMAT = pyaudio.paInt16
    CHANNELS = 2 #stereo
    RATE = 44100 #common sampling frequency
    RECORD_SECONDS = 5 #change this record for longer or shorter!

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(outputFile, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
def timerFired(data):
    data.duration -=1
    data.noteLength -=1
    # while data.notePressed == True and data.currKey != None:
    #     data.sound = str(data.currKey)+ '.wav'
    #     play('sounds/'+data.sound)
def keyPressed(event,data):
    for key in data.noteKey:
        if event.keysym == key:
            data.notePressed = True
            data.currKey = data.noteKey[key]
            
    for key in data.noteTime:
        
        
        if data.currKey == key:
            data.noteLength = data.noteTime[key]
            
           
def mousePressed(event,data):
    pass
    
    
def redrawAll(canvas,data):
     
    whiteKeyStart = data.whiteKeyStart+data.whiteKeySize
    whiteKeyEnd = data.whiteKeyEnd
    blackKeyStart = data.blackKeyStart
    blackKeyEnd = data.blackKeyEnd
    whiteKeySize = data.whiteKeySize
    blackKeySize = data.blackKeySize
    for key in data.noteKey:
        if len(data.noteKey[key]) == 2:
            
            canvas.create_image(whiteKeyStart,whiteKeyEnd,image = data.whiteKey) 
                
            whiteKeyStart += whiteKeySize
            #print('whiteKeyStart',whiteKeyStart)
        elif len(data.noteKey[key]) == 3:
            
            canvas.create_image(blackKeyStart,blackKeyEnd,image = data.blackKey)
            if blackKeyStart == 125 or blackKeyStart == 320 or blackKeyStart == 470: 
                blackKeyStart += 3.5*blackKeySize
            else: blackKeyStart += 1.5*blackKeySize
            #print('blackKeyStart',blackKeyStart)
    
    if data.notePressed == True:
        for key in data.keyPos:
            if data.keyPos[key] == data.currKey:
                
                if len(data.currKey) == 2:
                    whiteKeyStart = key
                    t=threading.Thread(target=lambda:play('sounds/%s.wav'%data.currKey))
                    t.start()
                    canvas.create_image(whiteKeyStart,whiteKeyEnd,image = data.whiteKeyPressed)
                    
    
                elif len(data.currKey) == 3:
                    blackKeyStart = key
                    t=threading.Thread(target=lambda:play('sounds/%s.wav'%data.currKey))
                    t.start()
                    canvas.create_image(blackKeyStart,blackKeyEnd,image = data.blackKeyPressed)
                    
        
        
        
    if data.noteLength == 0: 
        data.notePressed = False
        data.currKey = None
                
                # data.notePressed = False
    
        
###default run-function
def run(width, height):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

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
    data.timerDelay = 10 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


run(800,700)


#characters that map to certain notes on piano

    
