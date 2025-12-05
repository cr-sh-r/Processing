"""
Clem Hecker
Homework week 2
"""
size(1000,1000)
windowW = 1000
windowH = 1000
noStroke()
background(0)

bowl_width = 800
bowlmouth_height = bowl_width/2
fruit_width = bowl_width/3
fruit_height = fruit_width*1.2
stem_height = fruit_height/5
stem_width = stem_height/2.5
fruit_creasex =(windowW/2)+((fruit_width/6)/3)
fruit_creasey = (windowH/2) - (fruit_height/2) - stem_height/2


fill(45)
circle(500,500, bowl_width)
fill(0)
rect(500-bowl_width/2, 500-bowl_width/2, bowl_width, bowl_width/2)
fill(1,200,100)
ellipse(500,500,bowl_width, bowlmouth_height)

fill(200,10,10)
ellipse((windowW/2)+(fruit_width/6),windowH/2,fruit_width,fruit_height)


fill(80,50,50)
rect(fruit_creasex, fruit_creasey, stem_width, stem_height)

fill(200,40,10)
ellipse((windowW/2)-fruit_width/6,windowH/2,fruit_width,fruit_height)
