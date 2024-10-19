import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()
root.title('Guessing Games')
root.geometry("325x200")

guessStatement = ttk.Label(root, text="Guess a number between 1 and 100 (or click 'quit' to give up)")
guessStatement.grid(row = 0, column = 0, columnspan= 5)

playerGuess = tk.IntVar()
playerGuessEntry = ttk.Entry(root, width = 10, textvariable = playerGuess)
playerGuessEntry.grid(row = 1, column = 0, columnspan = 5)

# Random function to create random number and guess functionality
randNumGen = random.randint(1, 100)
gameAnswer = randNumGen
def random():
    if playerGuess.get() == gameAnswer:
        resultLabel.config(text="Congrat you guessed the right Number!!!") # Configure label to print text
    elif playerGuess.get() > gameAnswer:
        resultLabel.config(text="Wrong Answer! Guess a lower number Try again.") # Configure label to print text
    elif playerGuess.get() < gameAnswer:
        resultLabel.config(text="Wrong Answer! Guess a higher number Try again.") # Configure label to print text

# Label to display if player guess is right or wrong
resultLabel = ttk.Label(root, text="")
resultLabel.grid(row = 3, column = 0, columnspan = 5)

#This is for the button to submit the player's guess
submitGuessBtn = tk.Button(root, text="Submit Guess", command = random)
submitGuessBtn.grid(row=2, column=0, columnspan=5)


root.mainloop()