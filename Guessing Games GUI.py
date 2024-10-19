import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Guessing Games')
root.geometry("325x200")

guessStatement = ttk.Label(root, text="Guess a number between 1 and 100 (or click 'quit' to give up)")
guessStatement.grid(row = 0, column = 0, columnspan= 5)

playerGuess = tk.IntVar()
playerGuessEntry = ttk.Entry(root, width = 10, textvariable = playerGuess)
playerGuessEntry.grid(row = 1, column = 0, columnspan = 5)

submitGuessBtn = tk.Button(root, text="Submit Guess", command = playerGuess)
submitGuessBtn.grid(row=2, column=0, columnspan=5)



root.mainloop()