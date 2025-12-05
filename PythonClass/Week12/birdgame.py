gametree = { 
    "startask": {"message": "Did you see a bird?", "choices": {"A": ["yes", "question1"],
                                                               "B": ["no", "come back when you have seen a bird"]}},
    ##"question1": {"message": "What color was the bird?", "choices": {"A": ["Brown, brownbirds"],
                                                                     ##"B": ["White, whitebirds"],
                                                                    ## "C": ["Yellow", "yellowbirds"]}}                                                                                                                          
}

stateID = "startask"
state = gametree[stateID]

print(state["message"])

if len(state["choices"]) == 0:
        print("The end")
        exit()

# for input letter 
for c in ["A", "B"]:
    if c in state["choices"]:
        choice = state["choices"][c]
        print(f"{c}: {choice[0]}")

nextstateID = None 

qualityChoice = input(":")

#if the quality matches in the current state(a or b is chosen) make the next state what was chosen
if qualityChoice in state["choices"]:
    nextstateID = state["choices"][qualityChoice][1]