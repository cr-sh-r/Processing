"""
Clem Hecker
Homework week 1
"""
size(600,600)
img = loadImage("fruit_bowl.jpg")
noStroke()
#creates window 
background(0)
#one parameter for color takes grayscale
#background paramaters RGB
rect(200,500,200,30)
#draws rectangle paramaters: x coordinate, y coordinate,(of top left corner?) width, height, 
ellipse(300,327,405,405)
image(img,170,270,250,200)
# paramaters x, y (from center), width, height

fill(0)
rect(100,85,400,200)

fill(200,10,10)
ellipse(150,185,170,200)
fill(200,40,10)
ellipse(200,185,170,200)
fill(1,200,100)
rect(150,50,25,60)

fill(200,10,100)
ellipse(400,185,170,200)
fill(200,10,200)
ellipse(450,185,170,200)
fill(80,50,50)
rect(400,50,25,60)



#python convention for variable names uses underscore instead of mixed caps
