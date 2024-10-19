import random
print("Guess a number between 1 and 100")
playerGuess = input()
#>>>>>>> 7dc299db3ac005da4fa8b22c8f7e4053c72eaa20
#<<<<<<< HEAD
randNumGen = random.randint(1,1000)

gameAnswer = randNumGen

if playerGuess > gameAnswer:
    print("Wrong Answer!Guess a lower number Try again.")
elif playerGuess < gameAnswer:
    print("Wrong Answer!Guess a higher number Try again.")
else:
     print("Congrats you guessed the right Number!!!")

