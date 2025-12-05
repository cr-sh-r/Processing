from flask import Flask
import json

app = Flask(__name__) # capital F Flask is the library


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
                questions[gamepage]["answerd"] = True 
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

        
        return output

            
            




