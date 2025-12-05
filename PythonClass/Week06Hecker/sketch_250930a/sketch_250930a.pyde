""" Hecker week 5 homework 
part 1 & 2
"""

size(600,600)
background(255)

noStroke()

for i in range(25, width, 50):
    for j in range(25, height, 50):
        fill(map(i, 25, width, 0, 255),map(j,25, height, 0, 255), map(i,25,height,0,255),50)
        ellipse(i, j, 60, 60)

l = 100
while l <= 600:
    fill(29,32,100, 10)
    ellipse(300,300,l,l)
    l = l+10
    
