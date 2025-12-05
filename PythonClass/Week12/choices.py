gametree = { 
    "startask": {"message": "Did you see a bird?", "choices": {"A": ["yes", "question1"],
                                                               "B": ["no", "come back when you have seen a bird"]}},
    "question1": {"message": "What color was the bird?", "choices": {"A": ["Brown, brownbirds"],
                                                                     "B": ["White, whitebirds"],
                                                                     "C": ["Yellow", "yellowbirds"]}}                                                                                                                          
}

stateID = "startask"
state = gametree[stateID]

#ask the question
print(state["message"])

#Give the choices
for c in ["A", "B"]:
    if c in state["choices"]:
        choice = state["choices"][c]
        print(f"{c}: {choice[0]}")

nextstateID = None 

#ask for input
qualityChoice = input(":")

#grab the birds with the quality chosen from the bird list and write them to a new bird list file... doesnt actually do that yet
if qualityChoice in state["choices"]:
    nextstateID = state["choices"][qualityChoice][1]
    ab = open("birds.py", "r")
    birdnum = 3
    for i in birdnum:
        birdguess = ab.readline(i)
        if qualityChoice in birdguess:
            bg = open("birdGuesses", "w")
            bg.write( "\n" + birdguess)
    ab.close()
    bg.close()