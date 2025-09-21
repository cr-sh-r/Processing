"""Clem Hecker 
Week 04 Homework 


Fish Game
mouse moves fish
press mouse while hovering over shrimp to eat it
avoid eels who will eat you, if you eat their shrimps they will start hunting you
Q increases visibilty, A reduces visibility. 
The visibily also increases the eels danger zone
"""


rectH = 500
rectW = 30
center_Y = 400



def setup():
    size(600, 400)
    noStroke()
    fill(155, 155, 255, 50)
    rectMode(CENTER)
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
    
    global eaten1
    eaten1 = False 
    global eaten2
    eaten2 = False
    global eaten3
    eaten3 = False
    global eat
    eat = 255
    global last_image
    last_image = fishimage

    global dead
    dead = False
    
    global aggrivate
    aggrivate = False

    global predatorX
    predatorX = 150
    global predatorX2
    predatorX2 = 350
    global predatorX3
    predatorX3 = 550
    global predatorY
    predatorY = height-25
    global predator_direction
    predator_direction = 0.5
    
    global darkness
    darkness = 1.5
    
    global dx
    dx = 100
    
def keyPressed():
    global darkness
    if key == 'q' and darkness > 1.2:
        darkness = darkness - 0.05
    elif key == 'a' and darkness < 1.5:
        darkness = darkness + 0.05


def draw():

    background(25, 80, 97)
    imageMode(CORNER)
    noTint()
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
    
    
    noStroke()
   
    
        
###  rectangle 1
    center_X = 15
    pmousedist = width-(rectW/2)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    #print("distance" , Distance, "height", rectHeight)
    
    
        
### rectangle 2
    center_X = 15 + rectW
    pmousedist = width-(rectW/2)-(rectW)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)

    
### rectangle 3
    center_X = 15 + rectW*2
    pmousedist = width-(rectW/2)-(rectW*2)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 4
    center_X = 15 + rectW*3
    pmousedist = width-(rectW/2)-(rectW*3)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 5
    center_X = 15 + rectW*4
    pmousedist = width-(rectW/2)-(rectW*4)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 6
    center_X = 15 + rectW*5
    pmousedist = width-(rectW/2)-(rectW*5)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 7
    center_X = 15 + rectW*6
    pmousedist = width-(rectW/2)-(rectW*6)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 8
    center_X = 15 + rectW*7
    pmousedist = width-(rectW/2)-(rectW*7)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 9
    center_X = 15 + rectW*8
    pmousedist = width-(rectW/2)-(rectW*8)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 10
    center_X = 15 + rectW*9
    pmousedist = width-(rectW/2)-(rectW*9)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 11
    center_X = 15 + rectW*10
    pmousedist = width-(rectW/2)-(rectW*9)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
    
### rectangle 12
    center_X = 15 + rectW*11
    pmousedist = width-(rectW/2)-(rectW*8)
    color_dist = dist(mouseX, mouseY, center_X, 0)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 13
    center_X = 15 + rectW*12
    pmousedist = width-(rectW/2)-(rectW*7)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 14
    center_X = 15 + rectW*13
    pmousedist = width-(rectW/2)-(rectW*6)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 15
    center_X = 15 + rectW*14
    pmousedist = width-(rectW/2)-(rectW*5)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 16
    center_X = 15 + rectW*15
    pmousedist = width-(rectW/2)-(rectW*4)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 17
    center_X = 15 + rectW*16
    pmousedist = width-(rectW/2)-(rectW*3)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 18   
    center_X = 15 + rectW*17
    pmousedist = width-(rectW/2)-(rectW*2)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 19
    center_X = 15 + rectW*18
    pmousedist = width-(rectW/2)-(rectW)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
### rectangle 20
    center_X = 15 + rectW*19
    pmousedist = width-(rectW/2)
    fill(94, 183, 194)
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
    global last_image 
    global eaten1
    global eaten2
    global eaten3
    global eat
    global aggrivate
    global dead
    global predatorX
    global predatorY
    global predator_direction
    global dx 
    
    if dead != True:
        if mouseX < pmouseX:
            image(fish_reverse, mouseX-50, mouseY-25, 100, 50)
            last_image = fish_reverse
        elif mouseX > pmouseX:
            image(fishimage, mouseX-50, mouseY-25, 100, 50)
            last_image = fishimage
        elif dead == True:
            print("dead")
        else:
            image(last_image, mouseX-50, mouseY-25, 100, 50)
            #last_image = last_image
    else:
        print("you died")
        
    
    imageMode(CENTER)
    foodposX = 50
    foodposY = height-25
    if mousePressed and mouseX >= foodposX-25 and mouseX <= foodposX+25 and mouseY >= foodposY-25 and mouseY <= foodposY+25:
        eaten1 = True
        
    if eaten1:
        pass
        #eat = 0
        #print('eat')
    else:
        #tint(255, eat)
        image(shrimp, foodposX, foodposY, 50,50)
        
        
        
    foodposX = 250
    foodposY = height-25
    if mousePressed and mouseX >= foodposX-25 and mouseX <= foodposX+25 and mouseY >= foodposY-25 and mouseY <= foodposY+25:
        eaten2 = True
        
    if eaten2:
        pass
        #eat = 0
        #print('eat')
    else:
        #tint(255, eat)
        image(shrimp, foodposX, foodposY, 50,50)
    
    
    foodposX = 450
    foodposY = height-25
    if mousePressed and mouseX >= foodposX-25 and mouseX <= foodposX+25 and mouseY >= foodposY-25 and mouseY <= foodposY+25:
        eaten3 = True
        
    if eaten3:
        pass
        #eat = 0
        #print('eat')
    else:
        #tint(255, eat)
        image(shrimp, foodposX, foodposY, 50,50)
    

    dangerzone = map(darkness,1.2,1.5,125,75)
    danger = dist(mouseX, mouseY, predatorX, predatorY)
    
    ## predator kills fish and moves to mouse coordinates
    if danger <= dangerzone:
        print("danger")
        predatorX = mouseX 
        predatorY = mouseY
        dead = True
        
    if eaten1 == True or eaten2 ==True and danger <= dangerzone+50:
            aggrivate = True


    if aggrivate and predatorY > 200: 
        print("hunting")
        predatorY = predatorY - 0.5
    elif predatorY == 200 and predatorX > width:
        predator_direction = -0.5
    elif predatorY == 200 and predatorX < 0:
        predator_direction = 0.5
    
    if aggrivate and predatorY == 200:
        predatorX = predatorX + predator_direction
    

        predatorX1 = 150

    if predatorX < width/2:
        current_rect = (predatorX/30)-1
    elif predatorX == 15 + rectW*10:
        current_rect = predatorX/30
    else:
        current_rect = 20 -(predatorX/30)

    pred_rect = width - (rectW/2)-(rectW*current_rect)
    Distancep = dist(mouseX,center_Y, predatorX, center_Y)
    waterheight = (map(Distancep,0,pred_rect,400,50))*2

    
    if predatorY <= height - ((waterheight/2)-15):
        visible = 0
    else:
        visible = 255

    tint(255,visible)
    image(eel, predatorX, predatorY, 50, 50 )
    
        
### rectangle 1 cover
    center_X = 15
    pmousedist = width-(rectW/2)   
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)

### rectangle cover 2   
    center_X = 15 + rectW
    pmousedist = width-(rectW/2)-(rectW) 
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)



### rectangle 3 cover   
    center_X = 15 + rectW*2
    pmousedist = width-(rectW/2)-(rectW*2)
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)


### rectangle 4 cover 
    center_X = 15 + rectW*3
    pmousedist = width-(rectW/2)-(rectW*3)  
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    

### rectangle 5 cover  
    center_X = 15 + rectW*4
    pmousedist = width-(rectW/2)-(rectW*4) 
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    

### rectangle 6 cover   
    center_X = 15 + rectW*5
    pmousedist = width-(rectW/2)-(rectW*5)
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    

### rectangle 7 cover   
    center_X = 15 + rectW*6
    pmousedist = width-(rectW/2)-(rectW*6)
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    

### rectangle 8 cover   
    center_X = 15 + rectW*7
    pmousedist = width-(rectW/2)-(rectW*7)
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    

### rectangle 9 cover  
    center_X = 15 + rectW*8
    pmousedist = width-(rectW/2)-(rectW*8) 
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    

### rectangle 10 cover
    center_X = 15 + rectW*9
    pmousedist = width-(rectW/2)-(rectW*9)   
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)


### rectangle 11 cover   
    center_X = 15 + rectW*10   
    pmousedist = width-(rectW/2)-(rectW*9)
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)



### rectangle 12 cover   
    center_X = 15 + rectW*11
    pmousedist = width-(rectW/2)-(rectW*8)
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
 

### rectangle 13 cover   
    center_X = 15 + rectW*12
    pmousedist = width-(rectW/2)-(rectW*7)
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)


### rectangle 14 cover 
    center_X = 15 + rectW*13
    pmousedist = width-(rectW/2)-(rectW*6)  
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    

### rectangle 15 cover   
    center_X = 15 + rectW*14
    pmousedist = width-(rectW/2)-(rectW*5)
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    

### rectangle 16 cover   
    center_X = 15 + rectW*15
    pmousedist = width-(rectW/2)-(rectW*4)
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    

### rectangle 17 cover   
    center_X = 15 + rectW*16
    pmousedist = width-(rectW/2)-(rectW*3)
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    

### rectangle 18 cover 
    center_X = 15 + rectW*17
    pmousedist = width-(rectW/2)-(rectW*2)  
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    

### rectangle 19 cover 
    center_X = 15 + rectW*18
    pmousedist = width-(rectW/2)-(rectW)  
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    

### rectangle 20 cover   
    center_X = 15 + rectW*19
    pmousedist = width-(rectW/2)
    color_dist = dist(mouseX, center_Y, center_X, center_Y)
    opacity = map(color_dist,0,pmousedist,0,255)
    fill(4, 57, 74, pow(opacity,darkness))
    Distance = dist(mouseX,center_Y, center_X, center_Y)
    rectHeight = map(Distance,0,pmousedist,400,50)
    rect(center_X,center_Y,rectW,rectHeight*2)
    
    
    if dead == True:
        imageMode(CENTER)
        image(fishimage, 300, 200, dx,dx/2)
        if dx < 600:
            dx = dx + 10
    
    
    
