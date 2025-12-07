from flask import Flask, session, request
import json 

app = Flask(__name__) # capital F Flask is the library
app.secret_key = "birdgamecookies"


# Open main bird file, read onto variable birdstring
# convert to json onto variable birds, close main bird json file
f = open("birds.json", "r")
birdsstring = f.read()
birds = json.loads(birdsstring)
f.close()
t = open("questions.json", "r")
q_string = t.read()
questions = json.loads(q_string)
t.close()
#print(questions)

# create list called qualities taking just the keys from the birds json
#removes the name key from the list
qualities = list(birds[0].keys())
qualities.remove("name")
questions_list = list(questions.keys())
#questions_list.remove("start")

#ask = "start"

@app.route("/birdgame")
def home():
    output = ""
    question = questions["home"]
    output += f"{question}<br/>"
    output += f"<a href='/birdgame/start'>yes</a><br/>"
    output += f"<a href='/nobirdgame'>no</a><br/>"
    
    return output
    
@app.route("/nobirdgame")
def nobird():
    question = questions["nobird"]
    output = f"{question}<br/>"
    output += f"<a href='/birdgame'>ok</a><br/>"

    return output

    

@app.route("/birdgame/<gamepage>")
def game(gamepage):
        
        
                #game is called when the user clicks so it is either the start page or a link which is the answer to the previous page you displayed

### handle current url to get answers up to date ###
        answers = {}                              # gets wiped every time loaded or clicked
        
        if gamepage != "start": 
            answers = session['session_answers']  # session is a flask dictionary, 'session_answers' is a key in the dictionary, 
                                                  #the value is another dictionary we are assigning the inner dictionary to the variable answers
            answer = request.args.get('answer')   # answer is a variable that gets assigned what option was just clicked, 
                                                  # so the current  url (example):/birdgame/color?answer=white holds through the query paramater the option of the previous question that was chosen
            answers[gamepage] = answer            # takes the answer that we just pulled from the query and puts it as the value of the key 'gamepage' which is the current 
                                                  #quality that is not the displayed web quality(that technically doesnt exist because we havent sent the new page at this point in the python code or figured out what the nextquality is)
                                                  # but the one from the url because it is the link itself that will get us to the next page that is holding the information 
        
        session['session_answers'] = answers      # answers is empty on start, but if it gets a answer from the else block it will be put into session as a value to key session_answers
        session.modified = True                   #makes sure flask stores every time?

### filters bird list based on current answers ###
        # make an empty list for filtered birds
        # iterate the main birds list
        # copy birds that pass the answers to the filtered list

        filtered_birds = list(birds)
        # filter a bird if it has the quality but doesn't equal the current answer
        for bird in birds:
            for q in answers:
                if (q,answers[q]) not in bird.items():
                    filtered_birds.remove(bird)
                    break
                    
        
        filtered_qualities = list(qualities)
        for q in qualities:
            if q in answers.keys():
                filtered_qualities.remove(q)


        qualities_dict = {}                                # makes an empty dictionary called qualities_list outside the loop  
        for q in filtered_qualities:                                # loops over the qualities in the list-
            options_dict= {}                               # makes temporary dictionary that gets emptied between every quality, stores the options
            for bird in filtered_birds:                             # loops over each 'bird' in each quality,
                options_dict[bird[q]] = 1                  # within each quality, q is looping over the possible-
                                                           # options for that quality as key with 1 as the value (brown: 1) de-duplicate
            qualities_dict[q] = list(options_dict.keys())  # lists the keys of options_dict as the value of-
                                                           # the quality(why its outside the inner loop)
                                                           #print(qualities_dict)  


    #get answers up to date
        nextquality = ''                          #empty string that will hold the quality of the next page of question???
        if filtered_qualities:
            nextquality = filtered_qualities[0]

    
        
### generate webpage ###      
        output = ""
        #output += f"{answers}<br/>"
        #output += f"{filtered_birds}<br/>"
        #output += f"{filtered_qualities}<br/>"

        if nextquality:
            nextquestion = questions[nextquality]
            output += f"{nextquestion}<br/>"
            for option in qualities_dict[nextquality]:
                output += f"<a href='/birdgame/{nextquality}?answer={option}'>{option}</a><br/>"
        else:
            output += f"this is your bird: {filtered_birds} "
        
        return output

@app.route('/newbird', methods =["GET", "POST"])
def newbird():
    output = ""
    if request.method == "POST":
        name = request.form.get("name")
        color = request.form.get("color")
        
        # get all the form values
        # put them in a new dict
        # append it to birds
        # dumps birds to a string, adding indent=4 to pretty print
        # save string to birds.json

        # str = json.dumps(birds,indent=4)

        output = "Thanks:<br/>"
        output += f"{name}<br/>"
        output += f"{color}<br/>"
    else: # GET             #triple quote is multi line string
        output = """                    
<form action="/newbird" method="post">
    <label for="name">Name:</label><br/>
    <input type="text" id="name" name="name" value=""/><br/>
    <label for="color">Color:</label><br/>
    <input type="text" id="color" name="color" value=""/><br/>
    <input type="submit" value="Submit"/>
</form> 
        """
    return output
