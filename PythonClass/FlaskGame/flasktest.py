from flask import Flask
import json
app = Flask(__name__)

f = open("flasktest.json","r")
file_contents = f.read()
game_tree = json.loads(file_contents)

@app.route("/game/")

def game():
    
    state = game_tree["hello"]
    
    output = state["message"]
    for c in ["A", "B", "C"]:
        if c in state["choices"]:
            choice = state["choices"][c]
            output = output + choice[0]

    return output