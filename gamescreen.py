###Michelle Lim TP2
###Code citations

#retrieved initial animation framework from 112 notes
#retrieved play functions from pyaudio tutorial homepage 
#retrieved all images from google

from tkinter import *
import random
import threading
import module_manager
module_manager.review()
import pyaudio
import wave
from array import array
from struct import pack
from tkinter import *
####################################
# init
####################################

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
def init(data):
    # There is only one init, not one-per-mode
    
    data.mode = "splashScreen"
    data.score = 0
    data.song = None
    data.easy = False
    data.med = False
    data.hard = False
    data.submit = False
    data.level = None
    data.timer = 0
    data.cx = 0
    data.cy = 0
    data.r = 30
    data.first = None
    data.t = None
    data.second = None
    data.third = None
    data.four  =None
    data.firstkeyTimer = 0
    data.secondkeyTimer = 0
    data.thirdkeyTimer= 0
    data.fourkeyTimer = 0
    data.firstCircles = []
    data.secondCircles = []
    data.thirdCircles = []
    data.fourCircles = []
    data.background = PhotoImage(file = "pictures/background.gif")
    data.startPic = PhotoImage(file='pictures/start.v1.gif')
    data.end=False
####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "splashScreen"): splashScreenMousePressed(event, data)
    elif (data.mode == "easyGame" or data.mode == "medGame" or data.mode == "hardGame"): 
       
        playGameMousePressed(event,data)
    if data.end == True: endGameMousePressed(event,data)
    

def keyPressed(event, data):
    
    if (data.mode == "splashScreen"): splashScreenKeyPressed(event, data)
    elif (data.mode == "easyGame" or data.mode == "medGame" or data.mode == "hardGame"): 
        
        playGameKeyPressed(event,data)
    if data.end == True: endGameKeyPressed(event,data)
    

def timerFired(data):
    if (data.mode == "splashScreen"): splashScreenTimerFired(data)
    elif (data.mode == "easyGame" or data.mode == "medGame" or data.mode == "hardGame"): 
        
        playGameTimerFired(data)
    if data.end == True: endGameTimerFired(data)
    

def redrawAll(canvas, data):
    if (data.mode == "splashScreen"): splashScreenRedrawAll(canvas, data)
    elif (data.mode == "easyGame" or data.mode == "medGame" or data.mode == "hardGame"): 
        
        playGameRedrawAll(canvas,data)
    if data.end == True: endGameRedrawAll(canvas,data)

####################################
# splashScreen mode
####################################

def splashScreenMousePressed(event, data):
    
    if event.x >= 30 and event.x <= 160 and event.y <= data.height/2 -80 and event.y>= data.height/2-100:
        
        data.easy = True
        data.med = False
        data.hard = False
    elif event.x >= 175 and event.x <= 305 and event.y <= data.height/2-80 and event.y >= data.height/2 - 100:
        
        data.med = True
        data.easy = False
        data.hard = False
    elif event.x >= 325 and event.x <= 450 and event.y <= data.height/2-80 and event.y >= data.height/2 - 100:
        data.easy = False
        data.med = False
        data.hard = True
     
    if event.x >= 150 and event.x <= 280 and event.y >= data.height/2 + 40 and event.y <= data.height/2 +80:
        
        
        data.song = 'attention'
    elif event.x >= 150 and event.x <= 280 and event.y >= data.height/2 + 90 and event.y <= data.height/2 +130:
     
        data.song = 'perfect'
    elif event.x >= 150 and event.x <= 280 and event.y >= data.height/2 + 140 and event.y <= data.height/2 +180:
    
        data.song = 'havanna'
    elif event.x >= 150 and event.x <= 280 and event.y >= data.height/2 + 190 and event.y <= data.height/2 +230:
 
        data.song = 'compose'
    if event.x >= 150 and event.x <=280 and event.y >= data.height/2 + 250 and event.y <= data.height/2 + 300:
       
        data.submit = True
        
    
    if data.submit == True and data.song != None and (data.easy == True or data.med == True or data.hard == True) and data.song=='attention': 
        data.t=threading.Thread(target=lambda:play('sounds/attention.wav'))
        if data.end != True:data.t.start()
        if data.easy == True: data.mode = "easyGame"
        elif data.med == True: data.mode="medGame"
        elif data.hard == True: data.mode="hardGame"
        
    elif data.submit == True and data.song != None and (data.easy == True or data.med == True or data.hard == True) and data.song=='perfect': 
        data.t=threading.Thread(target=lambda:play('sounds/perfect.wav'))
        data.t.start()
        if data.easy == True: data.mode = "easyGame"
        elif data.med == True: data.mode="medGame"
        elif data.hard == True: data.mode="hardGame" 
    elif data.submit == True and data.song != None and (data.easy == True or data.med == True or data.hard == True) and data.song=='havanna': 
        data.t=threading.Thread(target=lambda:play('sounds/havanna.wav'))
        data.t.start()
        if data.easy == True: data.mode = "easyGame"
        elif data.med == True: data.mode="medGame"
        elif data.hard == True: data.mode="hardGame"
        
def splashScreenKeyPressed(event, data):
    pass
    

def splashScreenTimerFired(data):
    pass

def splashScreenRedrawAll(canvas, data):
    canvas.create_image(data.width//2,data.height//2,image = data.startPic) 
    
    if data.easy == True:
        canvas.create_rectangle(30, data.height/2-80 ,160,data.height/2 - 100,fill="yellow")
    if data.med == True:
        canvas.create_rectangle(175, data.height/2-80 ,305,data.height/2 - 100,fill="yellow")
    if data.hard == True:
        canvas.create_rectangle(325, data.height/2-80 ,450,data.height/2 - 100,fill="yellow")
    if data.song == 'attention':
        canvas.create_rectangle(150, data.height/2 + 40 ,280,data.height/2 +80,fill="yellow")
    if data.song == 'perfect':
        canvas.create_rectangle(150, data.height/2 + 90 ,280,data.height/2 +130,fill="yellow")
    if data.song == 'havanna':
        canvas.create_rectangle(150, data.height/2 + 140 ,280,data.height/2 +180,fill="yellow")
    if data.song == 'compose':
        canvas.create_rectangle(150, data.height/2 + 190 ,280,data.height/2 +230,fill='yellow')
    
    canvas.create_text(data.width/2-100, data.height/2-250,
                       text="Play Guitar Hero Composed ", font="Impact 26 bold",fill="white")
    canvas.create_text(data.width/2-150, data.height/2-200,
                       text="Select a level and choose your song, then press play!", font="Arial 18",fill="white")
    canvas.create_rectangle(30, data.height/2-80 ,160,data.height/2 - 100,outline="white")
    canvas.create_text(95, data.height/2 - 90,text = 'Easy',fill="white")
    canvas.create_rectangle(175, data.height/2-80 ,305,data.height/2 - 100,outline="white")
    canvas.create_text(240, data.height/2 - 90,text = 'Medium',fill="white")
    canvas.create_rectangle(325, data.height/2-80 ,450,data.height/2 - 100,outline="white")
    canvas.create_text(387, data.height/2 - 90,text = 'Hard',fill="white")
    
    canvas.create_rectangle(150, data.height/2 + 40 ,280,data.height/2 +80,outline="white")
    canvas.create_text(215, data.height/2 +60,text = 'Song 1: Attention',fill="white")
    canvas.create_rectangle(150, data.height/2 + 90 ,280,data.height/2 +130,outline="white")
    canvas.create_text(215, data.height/2 +110,text = 'Song 2:Perfect ',fill="white")
    canvas.create_rectangle(150, data.height/2 + 140 ,280,data.height/2 +180,outline="white")
    canvas.create_text(215, data.height/2 +160,text = 'Song 3: Havanna ',fill="white")
    canvas.create_rectangle(150, data.height/2 + 190 ,280,data.height/2 +230,outline="white")
    canvas.create_text(215, data.height/2 +210,text = 'Compose your own ',fill="white")
    canvas.create_rectangle(150, data.height/2 + 250 ,280,data.height/2 +300,outline="white")
    canvas.create_text(215, data.height/2 +275,text = 'Submit',fill="white")
    
    
    

####################################
# playGame mode
####################################

    
def playGameMousePressed(event, data):
    pass

def playGameKeyPressed(event, data):
    if event.keysym == '1':
        
        data.first = True
    if event.keysym == '2':
        data.second = True
    if event.keysym == '3':
        data.third = True
    if event.keysym == '4':
        data.four = True
    
    if event.keysym == 'e':
        data.end = True 
        
        
        
    if data.first == True and data.firstCircles[0][1] >=600-data.r and data.firstCircles[0][1] <= 600+data.r and \
    data.firstCircles[0][1] >=200-data.r and data.firstCircles[0][1] <= 200+data.r:
        data.firstCircles.pop(0)
        data.score +=1
    elif data.firstCircles[0][0] >=600-data.r and data.firstCircles[0][0] <= 600+data.r and \
    data.firstCircles[0][1] >=200-data.r and data.firstCircles[0][1] <= 200+data.r:
        print('hi')
        data.firstCircles.pop(0)
    elif data.second == True and data.secondCircles[0][1] >=600-data.r and data.secondCircles[0][1] <= 600+data.r and \
    data.secondCircles[0][1] >=350-data.r and data.secondCircles[0][1] <= 350+data.r:
        data.secondCircles.pop(0)
        data.score +=1
    elif data.secondCircles[0][1] >=600-data.r and data.secondCircles[0][1] <= 600+data.r and \
    data.secondCircles[0][1] >=350-data.r and data.secondCircles[0][1] <= 350+data.r:
        data.secondCircles.pop(0)
    elif data.third == True and data.thirdCircles[0][1] >=600-data.r and data.thirdCircles[0][1] <= 600+data.r and \
    data.thirdCircles[0][1] >=500-data.r and data.thirdCircles[0][1] <= 500+data.r:
        data.thirdCircles.pop(0)
        data.score +=1
    elif data.thirdCircles[0][1] >=600-data.r and data.thirdCircles[0][1] <= 600+data.r and \
    data.thirdCircles[0][1] >=500-data.r and data.thirdCircles[0][1] <= 500+data.r:
        data.thirdCircles.pop(0)
    elif data.four == True and data.fourCircles[0][1] >=600-data.r and data.fourCircles[0][1] <= 600+data.r and \
    data.fourCircles[0][1] >=650-data.r and data.fourCircles[0][1] <= 650+data.r:
        data.fourCircles.pop(0)
        data.score +=1
    elif data.fourCircles[0][1] >=600-data.r and data.fourCircles[0][1] <= 600+data.r and \
    data.fourCircles[0][1] >=650-data.r and data.fourCircles[0][1] <= 650+data.r:
        data.fourCircles.pop(0)
        
    

def playGameTimerFired(data):
    
    if data.first == True:
        data.firstkeyTimer +=1
    if data.firstkeyTimer %3 == 0: 
        data.first = False
    if data.second == True:
            data.secondkeyTimer +=1
    if data.secondkeyTimer %3 == 0: 
        data.second = False
    if data.third == True:
            data.thirdkeyTimer +=1
    if data.thirdkeyTimer %3 == 0: 
        data.third = False
    if data.four == True:
            data.fourkeyTimer +=1
    if data.fourkeyTimer %3 == 0: 
        data.four = False
    data.timer += 1 
    if data.easy == True:
        for circles in data.firstCircles:
            circles[1] += 5
        for circles in data.secondCircles:
            circles[1] +=5
        for circles in data.thirdCircles:
            circles[1] +=5
        for circles in data.fourCircles:
            circles[1] +=5
    elif data.med == True:
        for circles in data.firstCircles:
            circles[1] += 10
        for circles in data.secondCircles:
            circles[1] +=10
        for circles in data.thirdCircles:
            circles[1] +=10
        for circles in data.fourCircles:
            circles[1] +=10
    elif data.hard == True:
        for circles in data.firstCircles:
            circles[1] += 10
        for circles in data.secondCircles:
            circles[1] +=10
        for circles in data.thirdCircles:
            circles[1] +=10
        for circles in data.fourCircles:
            circles[1] +=10 
def playGameRedrawAll(canvas, data):
    cy = data.cy
    
    canvas.create_image(data.width//2,data.height//2,image = data.background) 
    canvas.create_oval(200-data.r,600-data.r,200+data.r,600+data.r,outline="yellow2", width=5)
    canvas.create_oval(350-data.r,600-data.r,350+data.r,600+data.r,outline="green2", width=5)
    canvas.create_oval(500-data.r,600-data.r,500+data.r,600+data.r,outline = "DeepSkyBlue2", width = 5)
    canvas.create_oval(650-data.r,600-data.r,650+data.r,600+data.r,outline="RoyalBlue3",width=5)
    canvas.create_rectangle(10,70,120,130,fill="white")
    canvas.create_text(70,100,text='Score:\n %d'%data.score,font='Arial 24 bold')
    canvas.create_text(70,140,text='Press e to end',fill='white')
    # play('sounds/attention.wav')
    
    
    if data.end == False:
        if data.easy == True:
            
            if data.timer %15 == 0:
                
                data.cx = random.choice([200,350,500,650])
                if data.cx == 200: 
                    data.firstCircles.append([data.cx,0])
                elif data.cx == 350:
                    data.secondCircles.append([data.cx,0])
                elif data.cx== 500:
                    data.thirdCircles.append([data.cx,0])
                elif data.cx == 650:
                    data.fourCircles.append([data.cx,0])
        elif data.med == True:
            if data.timer %10 == 0:
                
                data.cx = random.choice([200,350,500,650])
                if data.cx == 200: 
                    data.firstCircles.append([data.cx,0])
                elif data.cx == 350:
                    data.secondCircles.append([data.cx,0])
                elif data.cx== 500:
                    data.thirdCircles.append([data.cx,0])
                elif data.cx == 650:
                    data.fourCircles.append([data.cx,0])
        elif data.hard == True:
            if data.timer %5 == 0:
                
                data.cx = random.choice([200,350,500,650])
                if data.cx == 200: 
                    data.firstCircles.append([data.cx,0])
                elif data.cx == 350:
                    data.secondCircles.append([data.cx,0])
                elif data.cx== 500:
                    data.thirdCircles.append([data.cx,0])
                elif data.cx == 650:
                    data.fourCircles.append([data.cx,0])
        for circles in data.firstCircles:
            canvas.create_oval(circles[0]-data.r,circles[1]-data.r,circles[0]+data.r,circles[1]+data.r,fill="yellow2")
            if data.firstCircles[0][1] >600+data.r+20 and data.firstCircles[0][1] <data.height and \
            data.firstCircles[0][0] >=200-data.r and data.firstCircles[0][0] <= 200+data.r and data.first != True:
                data.firstCircles.pop(0)
                canvas.create_text(200,600,text="Miss",fill="white")
            elif data.firstCircles[0][1] >600-data.r+20 and data.firstCircles[0][1] <600+data.r+20 and \
            data.firstCircles[0][0] >=200-data.r and data.firstCircles[0][0] <= 200+data.r and data.first == True:
                data.firstCircles.pop(0)
                data.score +=1
                canvas.create_text(200,600,text="Perfect!",fill="white")
                data.first = False
                
        for circles in data.secondCircles:
            canvas.create_oval(circles[0]-data.r,circles[1]-data.r,circles[0]+data.r,circles[1]+data.r,fill="green2")
            if data.secondCircles[0][1] >600+data.r+20 and data.secondCircles[0][1] <data.height and \
            data.secondCircles[0][0] >=350-data.r and data.secondCircles[0][0] <= 350+data.r and data.second != True:
                data.secondCircles.pop(0)
                canvas.create_text(350,600,text="Miss",fill="white")
            elif data.secondCircles[0][1] >600-data.r+20 and data.secondCircles[0][1] <600+data.r+20 and \
            data.secondCircles[0][0] >=350-data.r and data.secondCircles[0][0] <= 350+data.r and data.second == True:
                data.secondCircles.pop(0)
                canvas.create_text(350,600,text="Perfect!",fill="white")
                data.score +=1
                data.second = False
                
        for circles in data.thirdCircles:
            canvas.create_oval(circles[0]-data.r,circles[1]-data.r,circles[0]+data.r,circles[1]+data.r,fill="DeepSkyBlue2")
            if data.thirdCircles[0][1] >600+data.r+20 and data.thirdCircles[0][1] <data.height and \
            data.thirdCircles[0][0] >=500-data.r and data.thirdCircles[0][0] <= 500+data.r and data.third != True:
                data.thirdCircles.pop(0)
                canvas.create_text(500,600,text="Miss",fill="white")
            elif data.thirdCircles[0][1] >600-data.r+20 and data.thirdCircles[0][1] <600+data.r+20 and \
            data.thirdCircles[0][0] >=500-data.r and data.thirdCircles[0][0] <= 500+data.r and data.third == True:
                data.thirdCircles.pop(0)
                canvas.create_text(500,600,text="Perfect!",fill="white")
                data.score +=1
                data.third = False
            
            
        for circles in data.fourCircles:
            canvas.create_oval(circles[0]-data.r,circles[1]-data.r,circles[0]+data.r,circles[1]+data.r,fill="RoyalBlue3")
            if data.fourCircles[0][1] >600+data.r+20 and data.fourCircles[0][1] <data.height and \
            data.fourCircles[0][0] >=650-data.r and data.fourCircles[0][0] <= 650+data.r and data.four != True:
                data.fourCircles.pop(0)
                canvas.create_text(650,600,text="Miss",fill="white")
            elif data.fourCircles[0][1] >600-data.r+20 and data.fourCircles[0][1] <600+data.r+20 and \
            data.fourCircles[0][0] >=650-data.r and data.fourCircles[0][0] <= 650+data.r and data.four == True:
                data.fourCircles.pop(0)
                canvas.create_text(650,600,text="Perfect!",fill="white")
                data.score +=1
                data.four = False
####################################
# endGame mode
####################################
def endGameMousePressed(event, data):
    pass

def endGameKeyPressed(event, data):
    pass

def endGameTimerFired(data):
    pass

def endGameRedrawAll(canvas, data):
    canvas.create_text(data.width//2,data.height//2, text='Game stopped: Score: %d' %data.score, font="Arial 20", fill="white")
    data.t._stop()
   
   
###built in run function from 112 website


def run(width=300, height=300):
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
    data.timerDelay = 100 # milliseconds
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

def playGame():
    play('sounds/C1.wav')
    for i in range (10):
        print(i)
run(800,700)
# threading.Thread(target=playGame).start()
