# `dice roller`

This is a simple command-line dice roller game written in Python that simulates rolling one or more six-sided dice. Each die's result is displayed as ASCII art, mimicking the appearance of physical dice placed side by side, followed by the total sum of all rolls.

![dice_roller](demo.gif)

## Prerequisites

- Python 3.x installed on your system
- No external dependencies — `random` is part of the Python standard library

## How to Use

1. **Run the script:**

```bash
python dice_roller.py
```

2. **Enter the number of dice to roll when prompted:**

The script generates a random value (1–6) for each die, displays them side by side as ASCII art, and prints the total of all rolls.

## How It Works

**Key Components in `dice_roller.py`:**

- `random.randint(1, 6)`: Generates a random value between 1 and 6 for each die, simulating a real dice roll.
- `dice_art`: A dictionary mapping each possible roll (1–6) to its corresponding 5-line ASCII art representation.
- Nested loop (`for line in range(5): for die in dice:`): Prints each die's art line by line, side by side, so multiple dice appear aligned horizontally.
- `total`: Accumulates and displays the sum of all rolled values after the dice are shown.

## Notes

- Dice are displayed horizontally by default; a vertical display method is included in the code as a commented-out alternative.
- Designed for simplicity and demonstration purposes, using only Python's standard library.
