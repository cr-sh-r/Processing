"""
Clem Hecker 
Code Toolkit Python, Fall 2025
Fish Game 102/6/25

Fish Game
mouse moves fish
press mouse while hovering over shrimp to eat it
avoid eels who will eat you if you get too close
if you eat their shrimps they will start hunting you
Q increases your visibilty, A reduces visibility. 
Increasing the visibily also increases the eels danger zone


"""
### some global Variables 
rectW = 30
center_Y = 400

eatenL = [False,False,False,False]
foodposXs = [50, 250, 450, 550] 
aggrivates =[False]
predatorXs = [150]
predatorX = 150
startstrike = []
strikeduration = 2000

prevmx = 0
prevmy = 0
state = 0
intro = 0
leveltwo = False



def setup():
    size(600, 400)
    noStroke()
    fill(155, 155, 255, 50)
    rectMode(CENTER)
    noCursor()
    global diagonal
    diagonal = sqrt(pow(width,2)+pow(height,2))
    global fishimage
    fishimage = loadImage("fish.png")
    global fish_reverse
    fish_reverse = loadImage("fishR.png")
    global wavesimage
    wavesimage = loadImage("waves03.png")
    global shrimp
    shrimp = loadImage("shrimp.png")
    global eel
    eel = loadImage("eel.png")
    

    reset()
    
### resets the level 
def reset(): 
    
    global last_image
    last_image = fishimage

    global dead
    dead = False
    global win
    win = False
    
    global aggrivate
    aggrivate = False

    global predatorY
    predatorY = height-25
    global predator_direction
    predator_direction = 0.5
    
    global darkness
    darkness = 1.5
    
    global dx
    dx = 100
    
    global dying
    dying = False
    
    global strikestart
    startstrike = []
    
    
    global grow
    grow = 1
    
    eatenL = [False,False,False,False]
    foodposXs = [50, 250, 450, 550] 
    
    
### controls the intro screens through space bar
def keyPressed():
    
    global intro
    global state
    
    if key == ' ' and state == 0:
        intro = (intro + 1) % 4

        
    if key == 'p' and state == 0:
        state = 1
### makes Q and A change the darkness in the water        
    global darkness
    if key == 'q' and darkness > 1.2:
        darkness = darkness - 0.05
    elif key == 'a' and darkness < 1.5:
        darkness = darkness + 0.05
        
### makes button for playing again        
def mousePressed():
    
    global state
    if mouseX >=260 and mouseX <= 340 and mouseY >= 20 and mouseY <= 100 and state == 3:
        reset()
        state = 1
    
        


def draw():
    imageMode(CORNER)
    noTint()
    global state
### changes background color     
    if state == 2:
        background(4,7,48)
    elif state == 0:
        background(189, 234, 240)
    else:
        background(25, 80, 97)
     
   
### draws waves, should be looped but ran out of time    
    if state == 0 or state == 1:
        wavesx = map(mouseX, 0,width, -20,-200 );
        image(wavesimage, wavesx,50)
        image(wavesimage, wavesx+300,50)
        image(wavesimage, wavesx+600,50)
        
        wavesxfront = map(mouseX, 0,width, -20,-110 );
        image(wavesimage, wavesxfront,100)
        image(wavesimage, wavesxfront+300,100)
        image(wavesimage, wavesxfront+600,100)
        
        wavesxfore = map(mouseX, 0,width, -20,-200 );
        image(wavesimage, wavesxfore,200)
        image(wavesimage, wavesxfore+300,200)
        image(wavesimage, wavesxfore+600,200)
    
    
### delays start screen for a bit
    if millis() >= 700 and state == 0:
        startScreen() 
        
### controls the states & levels        
    if state == 1:
        levelOne()
        
    if state == 2:
        levelOne()
        leveltwo()
        
    if state == 3:
        lose()
    
    print(state)
    
    if dead == True:
        state = 3
        startstrike = []

    
### all the text for the start screen
def startScreen():
    image(fishimage,50, 50, 500, 250)
    textSize(32)
        
    if intro == 0:
        fill(0)
        text("welcome", 10, 30)
        text("to", 10, 60)
        text("the fish game", 10, 90)
        text("press space to continue", 200,300)
    elif intro == 1:
        textSize(25)
        fill(0)
        text("you are a fish swimming in the surf.", 10, 30)
        text("you are hungry for shrimp.", 10, 60)
        text("they like to crawl around on the ocean floor.", 10, 90)
        text("swim around with the cursor.", 10, 120)
        text("hover over shrimp and click down to eat them.", 10, 150)
        text("press space to continue", 200,300)
    elif intro == 2:
        textSize(25)
        fill(0)
        text("watch out for eels who want to eat you.", 10, 30)
        text("They are hungry too.", 10, 60)
        text("if you get too close and eat their shrimp,", 10, 90)
        text("they will come looking for you.", 10, 120)
        text("press space to continue", 200,300)
    elif intro == 3:
        textSize(25)
        fill(0)
        text("you can change your visibility in the water.", 10, 30)
        text("using Q to increase and A to decrease.", 10, 60)
        text("the more you can see,", 10, 90)
        text("the easier the eels can see you", 10, 120)
        text("press P to play", 200,300)

### lose condition
def lose():
    cursor()
    textSize(32)
    fill(100,50,26)
    text("You have been eaten",200,300)
    text("play again? click here ", 200, 200)
    
    fill(255)
    ellipseMode(CENTER)
    ellipse(300, 60, 40, 40)
    
### level one code
def levelOne():
    
    noStroke()
    
### Variables for level one
    global last_image 
    global aggrivate
    global dead
    global dying
    global win
    global predatorX
    global predatorY
    global predator_direction
    global dx 
    global prevmx
    global prevmy
    global strikeclock
    global state
    global strikeduration

    global wr
    wr = 94
    global wg
    wg = 183
    global wb
    wb = 194
    
### Draw wave rectangles
    for i in range(0,20):
        center_X = rectW/2 + rectW*i
        fill(wr,wg,wb)
        Distance = dist(mouseX,center_Y, center_X, center_Y)
        rectHeight = map(cos(PI*pow(Distance/width,.7)), -1, 1, 50, 400)
        rect(center_X,center_Y,rectW,rectHeight*2)

    
### Draw Fish    
    imageMode(CENTER)
    if dead == False and dying == False:
        if mouseX < pmouseX:
            image(fish_reverse, mouseX, mouseY, 100*grow, 50*grow)
            last_image = fish_reverse
            prevmx = mouseX
            prevmy = mouseY
        elif mouseX > pmouseX:
            image(fishimage, mouseX, mouseY, 100*grow, 50*grow)
            last_image = fishimage
            prevmx = mouseX
            prevmy = mouseY
        else:
            image(last_image, mouseX, mouseY, 100*grow, 50*grow)
            #last_image = last_image
            prevmx = mouseX
            prevmy = mouseY
            
    elif dead == True and dying == False:
            print("dead")
    elif dying == True and dead == False:
            image(last_image, prevmx, prevmy, 100, 50)
            print('fish',prevmx,prevmy)
   
    
### Draw shrimp, eat shrimp, aggrivate predator
    imageMode(CENTER)
    foodposY = height-25
    for i in range(0,len(eatenL)):
        foodposX = foodposXs[i]
        if mousePressed and mouseX >= foodposX-25 and mouseX <= foodposX+25 and mouseY >= foodposY-25 and mouseY <= foodposY+25:
            eatenL[i] = True
            if dist(foodposX, foodposY, predatorX, predatorY) < 200:
                aggrivate = True
        if eatenL[i]:
            pass
            #eat = 0
            #print('eat')
        else:
            #tint(255, eat)
            image(shrimp, foodposX, foodposY, 50,50)
        
    if state == 1 and dying == False and eatenL[0] == True and eatenL[1] == True and eatenL[2] == True and eatenL[3] == True:
        reset()
        state = 2
    
### Predator code        
        
    dangerzone = map(darkness,1.2,1.5,125,75)
    danger = dist(mouseX, mouseY, predatorX, predatorY)
    Distance = dist(mouseX,center_Y, predatorX, center_Y)
    waterheight = 400 - (map(cos(PI*pow(Distance/width,.7)), -1, 1, 50, 400))
    
### check if predator is within wave  
    imageMode(CENTER)  
    if predatorY >= waterheight + 10:
        predatorVisible = 255
    else:
        predatorVisible = 0
        
### predator moves to mouse coordinates and kills fish 
   
    if win == False and danger <= dangerzone and dead == False:
        dying = True
        
    if dying == True:
        startstrike.append(millis())
        elapsed = millis() - startstrike[0]
        t = min(1, float(elapsed)/strikeduration)
        currentX = lerp(predatorX, prevmx, t)
        currentY = lerp(predatorY, prevmy, t)
        tint(255, predatorVisible)
        image(eel, currentX, currentY, 50, 50 )
        print('time', float(elapsed))
        if float(elapsed) >= 2000:
            dying = False
            dead = True
    
    else:
        tint(255, predatorVisible)
        image(eel, predatorX, predatorY, 50, 50 )
### makes predator hunt    
    if win == False and aggrivate == True and predatorY > 200 and dying == False: 
        print("hunting")
        predatorY = predatorY - 0.5
    elif predatorY == 200 and predatorX > width:
        predator_direction = -0.5
    elif predatorY == 200 and predatorX < 0:
        predator_direction = 0.5
    
    if aggrivate and predatorY == 200:
        predatorX = predatorX + predator_direction
            

    
### draw cover rectangles
    
    for i in range(0,20):
        center_X = rectW/2 + rectW*i
        Distance = dist(mouseX,center_Y, center_X, center_Y)
        rectHeight = map(cos(PI*pow(Distance/width,.7)), -1, 1, 50, 400)
        opacity = map(cos(PI*pow(Distance/width,.7)), -1, 1, 255, 0)
        fill(4, 57, 74, pow(opacity,darkness))
        rect(center_X,center_Y,rectW,rectHeight*2)
    
    
### level two altering code
def leveltwo():

    global wr
    wr = 29
    global wg
    wg = 35
    global wb
    wb = 130
    
    grow = 2

   
    
    
    
    
