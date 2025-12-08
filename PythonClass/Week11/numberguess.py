import random
guess = ''
guesses = 3
num = random.randint(0,10)
print("num",num)
print("guess a number between 0 and 10:")
guess = int(input())

if num != guess:
    if guesses > 0 :
        print(f"you have {guesses} guesses left")
        print("try again:")
        guess = int(input())
        guesses = guesses - 1
        print(guess)
    else:
        print("you ran out of guesses, play again? type y")
        again = input()
        if again == "y":
            num = random.randint(0,10)
            guesses = 3
            guess = ''
else:
    print("congratulations")

    



