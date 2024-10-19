import random

randNumGen = random.randint(1,100)

while True:
    print("Guess a number between 1 and 100 (or type 'quit' to give up)")
    playerGuess = input()

    gameAnswer = randNumGen

    if playerGuess == "quit":
        print("You gave up! the number was ", gameAnswer)
        break
    
    try:
        playerGuess = int(playerGuess)
    except ValueError:
        print("Please enter valid number")

    if playerGuess == gameAnswer:
        print("Congrats you guessed the right Number!!!")
        break
    elif playerGuess > gameAnswer:
        print("Wrong Answer!Guess a lower number Try again.")
    elif playerGuess < gameAnswer:
        print("Wrong Answer!Guess a higher number Try again.")
    

