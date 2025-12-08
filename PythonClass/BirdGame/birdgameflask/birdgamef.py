from flask import Flask, session, request
import json 
import random

app = Flask(__name__) 
app.secret_key = "birdgamecookies" #for session cookies 


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


# create list called qualities taking just the keys from the firs bird in birds.json
qualities = list(birds[0].keys())

# make sure all birds have all qualities and no extra qualities
for bird in birds:
    for q in qualities:
        if q not in bird:
            print(bird, "missing:", q)
            exit()

    for q in bird:
        if q not in qualities:
            print(bird,"has an extra quality:", q)
            exit()

#make sure there are questions for each quality

for q in qualities:
    if q != "name":
       if q not in questions:
        print("there is no question written for:",q)
        exit()

@app.route("/birdgame")
def home():
    output = ""
    question = questions["home"]
    output += f"{question}<br/>"
    output += "<a href='/birdgame/start'>yes</a><br/>"
    output += "<a href='/nobirdgame'>no</a><br/>"
    
    return output
    
@app.route("/nobirdgame")
def nobird():
    question = questions["nobird"]
    output = f"{question}<br/>"
    output += f"<a href='/birdgame'>ok</a><br/>"

    return output

@app.route("/birdgame/<gamepage>")
def game(gamepage):

### handle current url to get answers up to date ###
        answers = {}                              
        if gamepage != "start": 
            answers = session['session_answers']  # session is a flask dictionary, 'session_answers' is a key in the dictionary, 
                                                  # the value is another dictionary we are assigning the inner dictionary to the variable answers
            answer = request.args.get('answer')   # answer is a variable that gets assigned what option was just clicked, 
                                                  # so the current  url (example):/birdgame/color?answer=white holds through the query paramater the option of the previous question that was chosen
            answers[gamepage] = answer            # takes the answer that we just pulled from the query and puts it as the value of the key 'gamepage' which is the current 
                                                  # quality that is not the displayed web quality(that technically doesnt exist because we havent sent the new page at this point in the python code or figured out what the nextquality is)
                                                  # but the one from the url because it is the link itself that will get us to the next page that is holding the information 
        
        session['session_answers'] = answers      # answers is empty on start, but if it gets a answer from the else block it will be put into session as a value to key session_answers
        session.modified = True                   #makes sure flask stores every time?

### filters bird list based on current answers ###

        filtered_birds = list(birds) #copies birds 
        # filter a bird if it has the quality but doesn't equal the current answer
        for bird in birds:
            for q in answers:   # dictionary of qualities and answers from this session
                if (q,answers[q]) not in bird.items():
                    filtered_birds.remove(bird)
                    break   #breaks from the qualities loop in answers so it doesn't try and remove the same bird again
                    
### filters qualities based on current answers ###               
        filtered_qualities = list(qualities)
        filtered_qualities.remove("name") 
        for q in qualities:
            if q in answers:
                filtered_qualities.remove(q)

### de dupes the options for each quality left to ask ##
        qualities_dict = {}                                # makes an empty dictionary called qualities_list outside the loop  
        for q in filtered_qualities:                                # loops over the qualities in the list-
            options_dict= {}                               # makes temporary dictionary that gets emptied between every quality, stores the options
            for bird in filtered_birds:                             # loops over each 'bird' in each quality,
                options_dict[bird[q]] = 1                  # within each quality, q is looping over the possible-
                                                           # options for that quality as key with 1 as the value (brown: 1) de-duplicate
            qualities_dict[q] = list(options_dict.keys())  # lists the keys of options_dict as the value of-
                                                           # the quality(why its outside the inner loop)
                                                           #print(qualities_dict)  

### sets next quality to ask if there are ones less ##
        nextquality = ''                          
        if filtered_qualities: # checks if there is anything left in filtered qualities
            nextquality = random.choice(filtered_qualities)


### generate webpage for questions and bird guess ###      
        output = ""
        if nextquality: # if next quality has any value
            nextquestion = questions[nextquality] 
            output += f"{nextquestion}<br/>"
            for option in qualities_dict[nextquality]:
                output += f"<a href='/birdgame/{nextquality}?answer={option}'>{option}</a><br/>"
            output += f"<br/><a href='/newbird'>something else</a><br/>"
            output += f"<br/>I have {len(filtered_birds)} guesses"
        else:
            output += f"your bird is called a:<br/>"
            for b in filtered_birds[0]:
                if b == "name":
                    output += f"{filtered_birds[0][b]}<br/>"
                else:
                    output += f" {b}: {filtered_birds[0][b]},  "
            output += "<br/><br/><a href='/birdgame/start'>I saw another bird</a><br/>"
        
        return output

### adding a new bird to the data ###
@app.route('/newbird', methods =["GET", "POST"])
def newbird():

    output = ""
    if request.method == "POST":   #when submit is pushed go into post
        add_bird = {}
        for q in qualities:                  ### get answer from form and make dictionary of the new bird
            value = request.form.get(q)
            add_bird[q] = value

        check_qualities = list(qualities)
        check_qualities.remove("name") 

        for bird in birds:
            matchb = True
            for q in check_qualities:            ### checking if the bird entered matches any in the data ###
                if add_bird[q] != bird[q]:
                    matchb = False
                    break
            if matchb:  
                output += f"You did not discover this bird. It is called a {bird['name']}<br/>"
                output += "<a href='/birdgame'>Back to home</a><br/>"
                return output
                    
        birds.append(add_bird)          # if the bird is not duplicated in the data, append it to the bird list 
        new_birdstr = json.dumps(birds,indent=4)
        b = open("birds.json", "w")
        b.write(new_birdstr)            #write the bird list over the old json file
        b.close()
    
        output = "I have collected the new bird!<br/>"
        output += f"{add_bird}<br/>" 
        output += "<a href='/birdgame'>Back to home</a><br/>"

    else: # GET             # displays form for new bird input 
        answers = session['session_answers'] # get current answers to see what is known about new bird already
        output = "I don't know this bird... you have discovered a new bird! <br/> Name your bird and tell me the other traits"
        output += '<form action="/newbird" method="post">'      #starts the form generating 
        for q in qualities:
            if q in answers:
                output += f"""
                    {q} is {answers[q]}                  
                    <input type="hidden" name="{q}" value="{answers[q]}"><br/>
                """
            else:
                output += f"""
                    <label for="{q}">{q}:</label><br/>
                    <input type="text" id="{q}" name="{q}" value=""/><br/>
                """
        output += '<br/><input type="submit" value="Submit"/></form>'
    return output
 