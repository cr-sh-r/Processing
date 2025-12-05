def setup():
    size(500, 500)
    stroke(50, 50, 250)
    fill(150, 150, 250)
    rectMode(CENTER)
    global herdcount
    herdcount = 25
    global zonesize
    zonesize = 40
    
    #start a empty list 
    global x
    x = []
    global y
    y = []
    i = zonesize # i iterating variable
    while i <= zonesize * sqrt(herdcount):
        x.append(i+5)
        x.append(i+35)
        y.append(i+5)
        y.append(i+35)
        i = i + zonesize
        print('x',x)
        print('y',y)
        
           
def draw():
    background(255)
    
    z = 0
    u = 0
    for z in range(0, int(sqrt(herdcount))-1,1):       # 0,1,2,3  grid zones
        for u in range(0, int(sqrt(herdcount)-1),1):
            rect(mouseX + int(random(x[z],x[z+1])), mouseY + int(random(y[u],y[u+1])), 10, 10)
         
    
    

      
