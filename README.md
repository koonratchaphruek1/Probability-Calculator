# Probability-Calculator
A Python program that can calculate the odds of several events occurring together in a set amount of tries.

## Running chanceCalc.py

### Prerequisites
- Python 3.x installed on your system

### How to Run

1. Open a terminal/command prompt

2. Run the program:
   ```
   python chanceCalc.py
   ```

### Usage Instructions

When you run the program, it will prompt you for:

1. **Number of items** - How many different events you want to calculate
2. **Number of rolls** - How many times you want to attempt these events
3. **For each item:**
   - **Item name** - What you want to call this event (e.g., "heads")
   - **Chance** - The odds in format "1 in X" (e.g., 2 for a coin flip which is 1 in 2)

### Example

```
🔢Input num of items: 2
🌹Input amount of rolls: 10
🛞 Input item name & chance: heads 2
🛞 Input item name & chance: tails 2
```

This calculates the probability of getting both heads AND tails within 10 rolls.

### Output

The program will display the calculated odds in the format:
```
=====================================
The chance of getting [items] in [rolls] rolls is
 = 1 in [chance]
=====================================
```
