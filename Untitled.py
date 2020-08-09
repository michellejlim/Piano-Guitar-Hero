# Michelle Lim
from tkinter import *
import random
import string
####################################
# init
####################################
class Piano(object):
    def __init__(self,data):
        self.data = data
def init(data):
    data.mode = "startScreen" #start with the starting screen mode
    data.score = 0
    
    data.squareLeft = 50
    data.squareTop = 50
    data.squareSize = 50
    data.squareSpeed = 20
    data.headingRight = True
    data.headingDown = True
    data.images = []
    data.image = PhotoImage(file = "112.gif") #input gif file 
    data.sizeImage = 50
    data.squareLeft = random.randint(0,data.width-data.sizeImage)
    data.squareTop = random.randint(0,data.height - data.sizeImage)
    data.isGameOver = False
    data.timeLeft = 20
    data.counter = 0
    data.margin = 20 #thickness of the border 
    data.randomX = 0
    data.randomY = 0
    data.fiveScore = 0 
    data.scrollX = 0
    data.scrollY = 0
    data.mult = 1.5 #bottomLeft should be data.mult times, top Left is -0.5times
    
    
####################################
# mode dispatcher
####################################

#change modes depending on whether the mode is called to change
def mousePressed(event, data):
    if (data.mode == "startScreen"): startScreenMousePressed(event, data)
    elif (data.mode == "playGame"):   playGameMousePressed(event, data)
    elif (data.mode == "gameOver"):       gameOverMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "startScreen"): startScreenKeyPressed(event, data)
    elif (data.mode == "playGame"):   playGameKeyPressed(event, data)
    elif (data.mode == "gameOver"):       gameOverKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "startScreen"): startScreenTimerFired(data)
    elif (data.mode == "playGame"):   playGameTimerFired(data)
    elif (data.mode == "gameOver"):       gameOverTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "startScreen"): startScreenRedrawAll(canvas, data)
    elif (data.mode == "playGame"):   playGameRedrawAll(canvas, data)
    elif (data.mode == "gameOver"):       gameOverRedrawAll(canvas, data)
   

####################################
# startScreen mode
####################################
def doStep(data):
    # Move vertically
   
    border = 10
    if (data.headingRight == True):
        if (data.squareLeft + data.sizeImage > data.width-2*border):
            data.headingRight = False
        else:
            data.squareLeft += data.squareSpeed
    else:
        if (data.squareLeft <= 2*border):
            data.headingRight = True
        else:
            data.squareLeft -= data.squareSpeed
    
    # Move horizontally
    if (data.headingDown == True):
        if (data.squareTop + data.sizeImage > data.height-border):
            data.headingDown = False
        else:
            data.squareTop += data.squareSpeed
    else:
        if (data.squareTop <= 2*border):
            data.headingDown = True
        else:
            data.squareTop -= data.squareSpeed
            
def startScreenMousePressed(event, data):
    pass

def startScreenKeyPressed(event, data):
   
    if event.keysym == "p":
        data.mode = "playGame" #change mode to play

def startScreenTimerFired(data):
    doStep(data) #makes the image move randomly throughout the screen

def startScreenRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2-data.margin,
                       text="112 Clicker Game!", font="Arial 26 bold")
    canvas.create_text(data.width/2, data.height/2+data.margin,
                       text="Press 'p' to play!", font="Arial 20")
    canvas.create_image(data.squareLeft,data.squareTop,image = data.image,
    anchor = NW) 



####################################
# playGame mode
####################################


def playGameMousePressed(event, data):
    for i in range (len(data.images)-1,-1,-1): #for loop going down
        posX = data.images[i][0] 
        posY = data.images[i][1]
        #check that all conditions are true so that you clicked inside image
        if event.x >= (posX + data.scrollX - data.sizeImage//2) \
        and event.x <= (posX + data.scrollX + data.sizeImage//2) \
        and event.y >= (posY + data.scrollY - data.sizeImage//2)\
        and event.y <= (posY + data.scrollY + data.sizeImage//2):
            data.images.pop(i) #remove this image
            data.score +=1  
            data.fiveScore +=1 
            break 

def moveBox (data,dx,dy):
    data.scrollX += dx  #to scroll around the screen
    data.scrollY += dy

def playGameKeyPressed(event, data):
    tenth = 0.1 
    if not data.isGameOver: #while game is not over
        #change screen by 0.1 width or height when keys pressed
        if event.keysym == "Left":
            moveBox(data,+(tenth*data.width),0)
        elif event.keysym == "Up":
            moveBox(data,0,+(tenth*data.height))
        elif event.keysym == "Down":
            moveBox(data,0,-(tenth*data.height))
        elif event.keysym == "Right":
            moveBox(data,-(tenth*data.height),0)
    

def playGameTimerFired(data):
    data.counter += 1
    if data.counter % 5 == 0: #every 0.5 second
        placeRandImage(data)
    if data.counter % 10 == 0: #every second, timer will decrease
        data.timeLeft -= 1 
    if data.timeLeft == 0: #if no more time left, change mode to gameOver
        data.mode = "gameOver"
    if data.fiveScore == 5: #every five, increment time by 1 sec
        data.timeLeft += 1
        data.fiveScore = 0 

def placeRandImage(data):
    #you want to get a random coordinates within boundaries to place image
    randomX = random.randint(-data.width//2+data.sizeImage,
                                data.mult*data.width-data.sizeImage)
    randomY = random.randint(-data.height//2+data.sizeImage,
                                        data.mult*data.height-data.sizeImage)
    data.images.append([randomX, randomY])
    
        
def playGameRedrawAll(canvas, data):
    for i in range (len(data.images)):
        #create image from random coordinates in images list
        canvas.create_image(data.scrollX+data.images[i][0],
        data.scrollY + data.images[i][1], image = data.image)
        
    canvas.create_text(0,0,text = "Time Remaining: %s" %data.timeLeft, 
                    font="Arial 26 bold",anchor = NW)
    canvas.create_text(0,data.height,text = "Score: %s" %data.score,
                    font="Arial 26 bold",anchor = SW)
                    
    #this is the thick rectangle 
    canvas.create_rectangle(data.scrollX-data.width//2,
    data.scrollY-data.height//2, data.scrollX + data.mult*data.width, 
    data.scrollY + data.mult*data.height, width = data.margin)
    
    
    
        

####################################
# gameOver mode
####################################

def gameOverMousePressed(event, data):
    pass

def gameOverKeyPressed(event, data):
    if event.keysym == 's':
        init(data) #go to the starting screen

def gameOverTimerFired(data):
    pass

def gameOverRedrawAll(canvas, data):
    #create a filled red rectangle with white words 
    canvas.create_rectangle(0,0,data.width,data.height, fill = "red")
    canvas.create_text(data.width/2, data.height/2-40,
                       text="Game Over!", font="Arial 26 bold", fill = "white")
    canvas.create_text(data.width/2, data.height/2-10,
                        text="Final Score = " + str(data.score), 
                        font="Arial 20", fill="white")
    canvas.create_text(data.width/2, data.height/2+40,
                       text="Press 's' to start again", font="Arial 20",
                       fill = "white")
####################################
# use the run function as-is
####################################

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

run(300, 300)

