# Program to create a Dice Roller Game

# EXPLANATION : -
# This program is designed to simulate the experience of rolling a physical dice. When the program runs, it prompts the user to
# enter how many dice they would like to roll. For each die, the program uses the random.randint() function to generate a random
# number between 1 and 6, just like the possible outcomes of a real six-sided die. These random values are stored in a list called
# dice, which helps keep track of all the rolls. Each of these numbers is then mapped to an ASCII art representation of a die face,
# stored in a dictionary named dice_art. This dictionary holds 6 unique designs, one for each die number. The program displays all
# the dice horizontally using nested loops, giving the appearance that the dice are placed side by side. After displaying the dice
# the program calculates the sum of all rolled values and prints the total, giving a clear result of the turn.

import random

"""

ASSETS FOR THE GAME:- 
 
We use these unicode-characters to in order to print an ASCII dice:
print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
 o/p: ● ┌ ─ ┐ │ └ ┘

Basic box-shape we use for our dice:
"┌───────────┐"
"│           │"
"│           │"
"│           │"
"└───────────┘"

"""

dice_art = {
    1: ("┌───────────┐",
        "│           │",
        "│     ●     │",
        "│           │",
        "└───────────┘"),

    2: ("┌───────────┐",
        "│  ●        │",
        "│           │",
        "│        ●  │",
        "└───────────┘"),

    3: ("┌───────────┐",
        "│  ●        │",
        "│     ●     │",
        "│        ●  │",
        "└───────────┘"),

    4: ("┌───────────┐",
        "│  ●     ●  │",
        "│           │",
        "│  ●     ●  │",
        "└───────────┘"),

    5: ("┌───────────┐",
        "│  ●     ●  │",
        "│     ●     │",
        "│  ●     ●  │",
        "└───────────┘"),

    6: ("┌───────────┐",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "└───────────┘")
}

dice = []  # Stores the random results (1–6) of each die rolled
total = 0
print("------------DICE-ROLLER-GAME------------")
num_of_dice = int(input("How many dice would you like to roll? "))  # No. of dice, we want to roll

for die in range(num_of_dice):  # die is our counter
    dice.append(random.randint(1, 6))

# Method - 1: prints the dice in a vertical format
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)
# Explanation :
# dice[die]: This gets the random number (between 1–6) stored at position die in the dice list. For example, if the list is
# [3, 6, 2], then the dice[0] = 3. dice_art.get(dice[die]): This fetches the ASCII art for that number from the dictionary
# dice_art. Each value in this dictionary is a tuple containing 5 strings (each representing a line of the die). for line in...
# :This means we’re now looping over all 5 lines of that ASCII die face. So this loop prints one die vertically, line by line.


# Method - 2: prints the dice in a horizontal format
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end=" ")
    print()
# Explanation :
# The outer loop goes through each line index from 0 to 4 (because each die has 5 lines in its ASCII art). dice_art.get(die)[line]:
# This grabs only one line (based on the current index) of the ASCII art for each die. For example, dice_art[3][0] would return :
# "┌───────────┐" if die = 3 and line = 0. end=" ": This prevents print() from moving to a new line after each die's part is printed.
# Instead, all dice are printed side by side on the same line. After all dice have printed one line, a plain print() moves to the next
# row (next line of the dice), creating the illusion of dice lying next to each other.

for die in dice:
    total += die
print(f"Total: {total}")
