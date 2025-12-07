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
@app.route("/birdgame/<gamepage>")
def game(gamepage = "start"):
        #game is called when the user clicks so it is either the start page or a link which is the answer to the previous page you displayed

### generates bird list ###
        qualities_dict = {} # makes an empty dictionary called qualities_list outside the loop  
        for q in qualities: # loops over the qualities in the list-
            options_dict= {} # makes temporary dictionary that gets emptied between every quality, stores the options
            for bird in birds: # loops over each 'bird' in each quality,
                options_dict[bird[q]] = 1 # within each quality, q is looping over the possible-
                                          # options for that quality as key with 1 as the value (brown: 1) de-duplicate
            qualities_dict[q] = list(options_dict.keys()) # lists the keys of options_dict as the value of-
                                                   # the quality(why its outside the inner loop)
        #print(qualities_dict)  

### handle current url ###
        nextquality = '' #empty string that will hold the quality of the next page of question???
        answers = {} # gets wiped every time loaded or clicked
        
        if gamepage == "start": 
            nextquality = qualities[0] # hard coded to take the first quality on start (color)
        else: # if the gamepage is not start, assuming no link changing manually, 
            answers = session['session_answers'] # session is a flask dictionary, 'session_answers' is a key in the dictionary, 
            #the value is another dictionary we are assigning the inner dictionary to the variable answers
            answer = request.args.get('answer') # answer is a variable that gets assigned what option was just clicked, 
            # so the current  url (example):/birdgame/color?answer=white holds through the query paramater the option of the previous question that was chosen
            answers[gamepage] = answer # takes the answer that we just pulled from the query and puts it as the value of the key 'gamepage' which is the current 
            #quality that is not the displayed web quality(that technically doesnt exist because we havent sent the new page at this point in the python code or figured out what the nextquality is)
            # but the one from the url because it is the link itself that will get us to the next page that is holding the information 
            i = qualities.index(gamepage) # finds where the current quality is in the list of qualities
            i = i + 1 #incriment to next one in list
            if i < len(qualities): # if i has not exceeded the list length > if it has, nextqualities stays empty
                nextquality = qualities[i] # assign nextquality 
        
        session['session_answers'] = answers # answers is empty on start, but if it gets a answer from the else block it will be put into session as a value to key session_answers
        session.modified = True #makes sure flask stores every time?
        
### generate webpage ###      
        output = ""

        output += f"{answers}<br/>"
        #output += "current answers:<br/>"
        #for a in answers:
        #    output += f"<br/>"

        if nextquality:
            output += f"{nextquality}:<br/>"
            for option in qualities_dict[nextquality]:
                output += f"<a href='/birdgame/{nextquality}?answer={option}'>{option}</a><br/>"
        else:
            output += "nice bird"
        
        return output
             
                                        
### generates questions kinda ###
        if questions["start"]["answered"] == True:                                                   
            for ask in questions_list: 
                if questions[ask]["asked"] == False and questions[ask]["answered"] == False:
                    gamepage = ask
                    questions[ask]["asked"] = True
                elif questions[ask]["asked"] == True and questions[ask]["answered"] == False:
                    pass
                elif questions[ask]["asked"] == True and questions[ask]["answered"] == True:
                    pass 
            print("ask", ask) 
            print("questions list:", questions_list)
            # if all questions have been asked and answered
            #--- is this your bird 
                                
        page = questions[gamepage] # page is assigned to the value of key "start" in the questions json dict through gamepage^
        print(page)
        for i in questions[gamepage]["choices"]:  #loops over the amount of choices in the state's choices value(a list)
            questions[gamepage]["asked"] = True 
            if i in page["choices"]: #check if choice matched
                cnum= page["choices"].index(i) # choice number (cnum) is the index of where the choice stored as "i" is in the list of choices 
                choice = page["choices"][cnum] # choice is assigned by which of the choices alligned
                questions[gamepage]["answered"] = True 
                #store somehow the choice
                for c in birds:
                        if (q, choice) in c.items():
                            birdlocation = (c, "bird is at", birds.index(c))
                        else: 
                            #print(c,"bird did not match") #output
                            birds.remove(c)

        output = page["message"]
        #display_question = page["message"] 
        display_choices = options_dict  
        print(page)
        #listL = len(options[page][choices])
        #print("listleinght", listL)
        print("cnum", cnum)
        print("options", options_dict)
        output = output + f"<a href='/game/{display_choices}'>{display_choices}</a>" # choice (from list?)is added to output 
        print(output)

        #session["hi"] = "clem"
        #print(session["hi"])
        return output

            
            




