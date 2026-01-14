# Assignment 2 — Control Statements

This folder contains two small beginner exercises that demonstrate basic control flow in Python.

Project files

- `Task_1.py` — prompts for a number and prints whether it is even or odd.
- `Task_2.py` — computes the sum of integers from 1 to 50 and prints the result.

Task summaries

## Task 1 — Even or Odd Checker (`Task_1.py`)

Description

- Prompts the user to enter an integer and uses an `if`/`else` statement to determine parity.

Example (interactive):

```
Enter a number: 5
5 is an odd number.
```

## Task 2 — Sum of Numbers (`Task_2.py`)

Description

- Uses a `for` loop to sum integers from 1 to 50 and prints the total.

Code:

```python
total = 0
for i in range(1, 51):
	total += i
print("The sum of numbers from 1 to 50 is:", total)
```

Expected output:

```
The sum of numbers from 1 to 50 is: 1275
```

How to run

From the `Assignment 2` folder or repository root, run:

```bash
python "Python Programming/Control Statements/Assignment 2/Task_1.py"
python "Python Programming/Control Statements/Assignment 2/Task_2.py"
```

Requirements

- Python 3.x

Notes

- These scripts are intentionally simple to illustrate control statements and user input.
- If you want, I can add unit tests, example outputs saved to files, or a single runner script.

