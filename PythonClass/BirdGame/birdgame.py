
import json


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
newbirds = []
qualities = list(birds[0].keys())
qualities.remove("name")
#print(qualities)


# loops over the qualities in the list and makes two empty dictionaries called qualities_list and choices
# loops over each 'bird' in each quality,
# adds q in current bird like 'color' or 'pattern' to the dictionary as a key with the value 1
#for each quality, adds to choices the key quality with the value as a list of the possible descriptors
for q in qualities:
    qualities_dict = {}
    choices = {}
    for bird in birds:
        qualities_dict[bird[q]] = 1
        #print(bird[q])
    choices[q] = list(qualities_dict.keys())
    print("qualities_dict", qualities_dict)
    print("choices", choices)
    
    
    ask = q
    #print(questions[ask], choices[q])
    #print("quals", qualities)

    answer = input()
    if answer in choices[q]:
        for c in birds:
            if (q, answer) in c.items():
                newbirds.append(c)
                #print(newbirds)
        birdsstring = newbirds
          

    else:
        print("I dont know this description")
    #isnt 
    #print(newbirds)
    #birdsstring = newbirds
    #print(len(birds)) 
  

    
    




