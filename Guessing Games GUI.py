import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()
root.title('Guessing Games')
root.geometry("400x400")

root.grid_columnconfigure(0, weight=1)

guessStatement = ttk.Label(root, text="Guess a number between 1 and 100")
guessStatement.grid(row = 0, column = 0, columnspan = 1)

playerGuess = tk.IntVar()
playerGuessEntry = ttk.Entry(root, width = 10, textvariable = playerGuess)
playerGuessEntry.grid(row = 1, column = 0, columnspan = 1)

def restartGame():
    global gameAnswer
    gameAnswer = random.randint(1, 100)
    playerGuess.set(0)
    resultLabel.config(text="")
    restartBtn.grid_forget()

# Random function to create random number and guess functionality
randNumGen = random.randint(1, 100)
gameAnswer = randNumGen
def checkGuess():
    if playerGuess.get() < 1 or playerGuess.get() > 100:
        resultLabel.config(text="Wrong Answer! Guess between 1-100. Try again.") # Configure label to print text
    elif playerGuess.get() == gameAnswer:
        resultLabel.config(text="Congrat you guessed the right Number!!!") # Configure label to print text
        restartBtn.grid(row= 5, column= 0)
    elif playerGuess.get() > gameAnswer:
        resultLabel.config(text="Wrong Answer! Guess a lower number Try again.") # Configure label to print text
    elif playerGuess.get() < gameAnswer:
        resultLabel.config(text="Wrong Answer! Guess a higher number Try again.") # Configure label to print text
        playerGuess.set('')
    

# Label to display if player guess is right or wrong
resultLabel = ttk.Label(root, text="")
resultLabel.grid(row = 2, column = 0, columnspan = 1)

#This is for the button to submit the player's guess
submitGuessBtn = tk.Button(root, text="Submit Guess", command = checkGuess)
submitGuessBtn.grid(row=3, column=0, columnspan=1)

quitBtn = tk.Button(root, text = "Quit", command = root.quit)
quitBtn.grid(row=4, column=0)

restartBtn = tk.Button(root, text = "Restart", command = restartGame)
restartBtn.grid(row= 5, column= 0)
restartBtn.grid_remove()

root.mainloop()