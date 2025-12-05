import json

f = open("data.json","r")

file_contents = f.read()

data = json.loads(file_contents)

def setup():
    size(800,800)

def draw():
    background(255)
    
    i = 0
    while i < len(data):
        d = data[i]
        fill( d["r"], d["g"], d["b"] )
        ellipse( d["x"], d["y"], 50,50 )
        i = i + 1
