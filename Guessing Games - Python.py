import random

randNumGen = random.randint(1,100)

while True:
    print("Guess a number between 1 and 100 (or type 'quit' to give up)")
    playerGuess = int(input())

    gameAnswer = randNumGen

    if playerGuess == "quit":
        print("You gave up! the number was ", gameAnswer)

    if playerGuess > gameAnswer:
        print("Wrong Answer!Guess a lower number Try again.")
    elif playerGuess < gameAnswer:
        print("Wrong Answer!Guess a higher number Try again.")
    elif playerGuess == gameAnswer:
        print("Congrats you guessed the right Number!!!")
    else:
        print("Please enter a valid number")

