"""
Clem Hecker
Homework week 2
"""
# TODO 1: Put all your variable assignments here.
#         You should have no indentation here - i.e. no spaces
#         at the beginning of the line
bowl_width = 800
bowlmouth_height = bowl_width/2
fruit_width = bowl_width/3
fruit_height = fruit_width*1.2
stem_height = fruit_height/5
stem_width = stem_height/2.5
windowW = 1000
windowH = 1000
fruit_creasex =(windowW/2)+((fruit_width/6)/3)
fruit_creasey = (windowH/2) - (fruit_height/2) - stem_height/2


def setup():
    # size() goes inside setup() here. Like this:
    size(1000,1000)
    noStroke()
    background(0)


    # Optional: If your sketch from the previous part used background(),
    # put that here. It should have 4 spaces of indentation

   # TODO 2: Put each of your variables here on their own line
    #         and mark each as 'global'. (I will explain what this
    #         means next week.) And assign each one a random value
    #         using a low, high range that works reasonably within
    #         your composition. You should have 4 spaces of indendation.
    #         For example:
    #    global treeHeight
    #    treeHeight = random(50,250)
def draw():
    global bowl_width
    bowl_width = random(100,800)
    global windowW
    windowW = random(500,1000)
    global windowH
    windowH = random(500,1000)

 
    # TODO 3: Now copy/paste all your draw code here (ie, the code
    #         that uses those variables). All of the code here should
    #         have 4 spaces of indentation.
    fill(55,55,10,100)
    circle(500,500, bowl_width)
    fill(0)
    rect(500-bowl_width/2, 500-bowl_width/2, bowl_width, bowl_width/2)
    fill(75,55,10,90)
    ellipse(500,500,bowl_width, bowlmouth_height)

    fill(200,10,10,75)
    ellipse((windowW/2)+(fruit_width/6),windowH/2,fruit_width,fruit_height)


    fill(80,50,50,99)
    rect(fruit_creasex, fruit_creasey, stem_width, stem_height)

    fill(200,40,60)
    ellipse((windowW/2)-fruit_width/6,windowH/2,fruit_width,fruit_height)

    # NOTE: If you are using background(), remove it for now, or move
    #       it into the setup area, above.


    # TODO 4: Go through your code and for every place you are setting
    #         a color, add some transparency. For example, if your code
    #         has this:
    #   fill(255,0,0)
    #         modify it to something like this:
    #   fill(255,0,0,10)


    # TODO 5: run your sketch and see what happens!

  
    # The idea here is that if you do the above, you should hopefully
    # get something that looks like the Idris Khan image compositions.
    # Do you? This is a lead-in to the topic for next week, and I will
    # explain more about it then.
