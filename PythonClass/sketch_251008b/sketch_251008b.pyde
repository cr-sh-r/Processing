

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
    while i <= zonesize * herdcount:
        x.append(int(random( (i+5), (i+35) )))
        y.append(int(random( (i+5), (i+35) )))
        i = i + zonesize
        print('x',x)
        print('y',y)
        
           
def draw():
    background(255)
    
    z = 0
    u = 0
    for z in range(0, int(sqrt(herdcount))-1,1):       # 0,1,2,3  grid zones
        for u in range(0, int(sqrt(herdcount)-1),1):
            rect(mouseX + x[z], mouseY + y[u], 10, 10)
            z = z + 1
            u = u + 1
         
    
    

      
