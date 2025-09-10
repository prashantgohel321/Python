# Day 5: Automating with Python Loops

Welcome to my log for Day 5 of the 100 Days of Code Python Bootcamp. Today's focus was on a concept that truly unlocks the power of programming: **loops**. I learned how to make the computer perform repetitive tasks automatically, which is a massive time-saver. I specifically worked with `for` loops, learning to iterate through items in a list and to repeat actions a specific number of times using the `range()` function. The day culminated in a very practical and useful project: a PyPassword Generator to create strong, secure passwords.

## Table of Contents
- [1. `for` Loops](#1-for-loops)
  - [Looping Through a List](#looping-through-a-list)
  - [The Importance of Indentation](#the-importance-of-indentation)
- [2. Using `for` Loops with the `range()` Function](#2-using-for-loops-with-the-range-function)
- [3. Day 5 Project: PyPassword Generator](#3-day-5-project-pypassword-generator)
  - [Easy Level: Sequential Password](#easy-level-sequential-password)
  - [Hard Level: Shuffled Password](#hard-level-shuffled-password)

---

### 1. `for` Loops
- **What is it?** A `for` loop is a way to execute a block of code over and over again for each item in a sequence (like a list). It's a fundamental tool for automation.
- **Why do I use it?** To avoid writing the same code multiple times. If I have a list of 100 names and want to print each one, a `for` loop lets me do it in three lines of code instead of 100.

#### Looping Through a List
- **How do I use it?** The syntax is very readable: `for item in list_of_items:`. The `item` is a temporary variable that holds the value of the current item in the list for each iteration of the loop.

```python
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")

# This will print:
# Apple
# Apple Pie
# Peach
# Peach Pie
# Pear
# Pear Pie
```

#### The Importance of Indentation
I learned again today just how critical indentation is in Python. Any code that I want to be executed *inside* the loop **must** be indented. Code that is not indented will only run *after* the entire loop has finished.

```python
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
print(fruits) # This is OUTSIDE the loop

# This will print:
# Apple
# Peach
# Pear
# ["Apple", "Peach", "Pear"]
```
---

### 2. Using `for` Loops with the `range()` Function
- **What is it?** The `range()` function generates a sequence of numbers, which I can then loop through. This is perfect for when I want to run a loop a specific number of times, without needing an existing list.
- **Why do I use it?** To perform an action a set number of times. For example, to add up all the numbers from 1 to 100.
- **How do I use it?** `range(start, end, step)`.
  - The `start` is inclusive.
  - The `end` is **exclusive** (the range goes *up to* but does not include this number).
  - The `step` is optional and determines the increment (defaults to 1).

```python
# To loop 10 times (numbers 0 through 9)
for number in range(0, 10):
  print(number)

# To sum numbers from 1 to 100
total = 0
for number in range(1, 101): # range(1, 101) gives numbers 1, 2, ..., 100
  total += number
print(total) # Output: 5050
```

---

### 3. Day 5 Project: PyPassword Generator
I built a program to generate strong passwords based on user preferences for the number of letters, symbols, and numbers. I tackled this in two stages.

#### Easy Level: Sequential Password
In the first version, I generated the password characters in a fixed order: all the requested letters first, then all the symbols, then all the numbers.

1.  **Get User Input**: I asked the user how many letters, symbols, and numbers they wanted in their password.
2.  **Use `for` loops with `range()`**: I used three separate `for` loops.
    - The first loop ran for the number of letters requested. In each iteration, it picked a random letter from a list of letters and added it to my password string.
    - The second loop did the same for symbols.
    - The third loop did the same for numbers.
3.  **Use `random.choice()`**: Inside each loop, `random.choice(list)` was the perfect tool to select a random character from the corresponding list (`letters`, `symbols`, or `numbers`).
4.  **Build the Password String**: I initialized an empty string variable `password = ""` and concatenated each randomly chosen character to it.

#### Hard Level: Shuffled Password
A predictable order makes a password weaker. The hard level involved shuffling the characters to create a truly random password.

1.  **Generate Characters and Store in a List**: Instead of building a string directly, I first used the same `for` loops to generate the required random letters, symbols, and numbers, but this time I `.append()`-ed each character to a **list**.

    ```python
    password_list = []
    for char in range(1, nr_letters + 1):
      password_list.append(random.choice(letters))
    # ... same for symbols and numbers ...
    ```

2.  **Shuffle the List**: Once I had my list of characters (e.g., `['a', 'b', 'c', '!', '@', '1', '2']`), I used the `random.shuffle()` function. This function shuffles the items of a list in-place, completely randomizing their order.

    ```python
    random.shuffle(password_list)
    # The list is now something like ['@', 'c', '1', 'b', '!', 'a', '2']
    ```

3.  **Convert List to String**: Finally, I needed to turn the shuffled list back into a single password string. I used another `for` loop to iterate through my shuffled `password_list` and add each character to a final password string.

    ```python
    password = ""
    for char in password_list:
      password += char
    
    print(f"Your password is: {password}")
    ```
This project was a fantastic exercise in using loops for generation and combining them with lists and the `random` module to create something complex and useful.
 