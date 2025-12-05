from flask import Flask

app = Flask(__name__)

#@app.route("/")
#gamestate = {"hello": "welcome", "bird1": "bird one"}
@app.route('/birdgame')
def game():
    return "<a href='https://classes.codeatlang.com/code-toolkit/2025-fall/week13.html#introducing-flask'>click</a>"

#def hello_world():
    #return "<p>Hello, World!</p>"