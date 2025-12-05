def setup():
    size(600,600)
    frameRate(50)

count = 0
    
    
def draw():
    background(255)
    global count
    prevMillis = millis() 
    
    if millis() >= prevMillis:
        if count <= 10000:
            count = count + 10
  
        else:
            count = 0
    m = count
    xs = [m, m+30, 60+m, m+120, m+240]
    ys = [m,m,m,m,m]
    for i in range(0,5): 
        line(300, 300, xs[i], ys[i])
        
"""  if millis() >= 300 and millis() <= 10000:
        for i in range(300,10000):
            m = map(millis(), 300, 10000, 0,600)
    else:
        for j in range(300,10000):
            m = map(millis()/9700, 300, millis(), 0,600) """

   
    ###print('mili', millis(), 'prev', prevMillis, 'count' , count)
    
