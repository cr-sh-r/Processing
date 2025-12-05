def setup():
    size(600,400)
    rectMode(CENTER)

rectW = 30
center_Y = height
r = 58
g = 52
b = 74


def draw():
    background(255)
    
    for i in range(rectW/2, width, 30):
        
        for j in range(0, height, 30):
            pmousedist = width-(rectW/2)
            Distance = dist(mouseX,center_Y, i, center_Y)
            rectHeight = map(Distance,0,pmousedist,300,50)
            if j >= 390:
                r = 58
                g = 52
                b = 74
            else: 
                r = 51
                g = 71
                b = 128
            
      
            fill(r, g, b)
            rect(i,j,rectW,rectHeight*2)
                
        
        
