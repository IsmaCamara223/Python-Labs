# Program Name: lab7.py
# Course: IT3883/Section XXX
# Student Name: Ismael Mathieu Coppini Camara
# Assignment Number: Lab7
# Due Date: 07/25/ 2024
# Purpose: This program is a Battle ship game that allow the user to guess in which cell is located a ship  
# I used the material from the class and online ressources: Stack Overflow, Youtube and Python website

import tkinter as tk
import random

# define grid and ship sizes
size_grid = 20
ships = [
    ("Ship 1", 3),
    ("Ship 2", 2),
    ("Ship 3", 4),
    ("Ship 4", 2),
    ("Ship 5", 3),
]

#Create game window
root = tk.Tk()
root.title("Battleship Game")

#Define variables
guesses = 0
positions = {}
hits = {}

#define ships placement function
def place_ships():
    for ship, size in ships:
        while True:
            direction = random.choice(['Horizontal', 'Vertical'])
            if direction == 'Horizontal':
                row = random.randint(0, size_grid - 1)
                col = random.randint(0, size_grid - size)
                if all((row, col + i) not in positions for i in range(size)):
                    for i in range(size):
                        positions[(row, col + i)] = ship
                    break
            else:
                row = random.randint(0, size_grid - size)
                col = random.randint(0, size_grid - 1)
                if all((row + i, col) not in positions for i in range(size)):
                    for i in range(size):
                        positions[(row + i, col)] = ship
                    break

#define guesses button function
def click(row, col):
    global guesses
    guesses += 1
    if (row, col) in positions:
        button_grid[row][col].config(text="Touché", bg="red")
        hits[(row, col)] = True
    else:
        button_grid[row][col].config(text="Miss", bg="blue")
    gameover()

#define gameover function
def gameover():
    if all(position in hits for position in positions):
        for row in range(size_grid):
            for col in range(size_grid):
                button_grid[row][col].config(state=tk.DISABLED)
        tk.messagebox.showinfo(f"You lost in {guesses} guesses!")

# Create the buttons grid
button_grid = [[None for _ in range(size_grid)] for _ in range(size_grid)]
for row in range(size_grid):
    for col in range(size_grid):
        button = tk.Button(root, width=2, height=1, command=lambda r=row, c=col: click(r, c))
        button.grid(row=row, column=col)
        button_grid[row][col] = button

place_ships()
root.mainloop()
