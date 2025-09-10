# Day 4: Randomisation and Python Lists

This is my log for Day 4 of the 100 Days of Code Python Bootcamp. Today was about adding an element of chance to my programs and learning how to manage collections of data. I explored Python's `random` module to generate unpredictable outcomes and dove into lists, a versatile data structure for storing ordered items. These two concepts were the foundation for building a fun Rock, Paper, Scissors game where I could play against the computer.

## Table of Contents
- [1. Randomisation in Python](#1-randomisation-in-python)
  - [What are Modules?](#what-are-modules)
  - [Generating Random Integers](#generating-random-integers)
  - [Generating Random Floating Point Numbers](#generating-random-floating-point-numbers)
- [2. Python Lists: A New Data Structure](#2-python-lists-a-new-data-structure)
  - [What is a List?](#what-is-a-list)
  - [Accessing and Modifying List Items](#accessing-and-modifying-list-items)
  - [Adding Items to a List](#adding-items-to-a-list)
- [3. Debugging: The `IndexError`](#3-debugging-the-indexerror)
- [4. Nested Lists](#4-nested-lists)
- [5. Day 4 Project: Rock, Paper, Scissors](#5-day-4-project-rock-paper-scissors)

---

### 1. Randomisation in Python
I learned that while computers are deterministic (predictable), I can use clever algorithms to generate "pseudo-random" numbers that are random enough for things like games.

#### What are Modules?
- **What is a module?** A module is simply a separate file containing Python code. It's a way to organize code into logical, reusable units. Instead of writing one gigantic file, I can split my code into modules, each responsible for specific functionality.
- **Why do I use them?** To keep my code organized and to use code that other people have written. The Python `random` module is a perfect example—it contains complex code for generating random numbers that I don't have to write myself.
- **How do I use one?** I use the `import` keyword at the top of my file to bring a module's functionality into my program.

```python
import random
```

#### Generating Random Integers
- **What is it?** Using the `random` module to get a random whole number within a specific range.
- **How do I use it?** The `random.randint(a, b)` function is the primary tool. It returns a random integer between `a` and `b`, *inclusive* of both endpoints.

```python
# Generates a random integer between 1 and 10 (can be 1, 10, or anything in between)
random_integer = random.randint(1, 10)
print(random_integer)
```

#### Generating Random Floating Point Numbers
- **What is it?** Using the `random` module to get a random decimal number.
- **How do I use it?** The `random.random()` function is a common way. It generates a random float between `0.0` and `1.0` (including 0.0, but *not* including 1.0). I can then multiply this result to expand the range.

```python
# Generates a random float between 0.0 and 0.999...
random_float = random.random()

# To get a random float between 0 and 5:
random_float_expanded = random.random() * 5
print(random_float_expanded)
```

---

### 2. Python Lists: A New Data Structure

#### What is a List?
- **What is it?** A list is a **data structure** used to store a collection of items in a specific order. It's like a variable that can hold more than one value.
- **Why do I use it?** It's perfect for grouping related data, like a list of names, scores, or states. The order is preserved, which is crucial for many tasks.
- **How do I create one?** I use square brackets `[]` and separate each item with a comma.

```python
fruits = ["Cherry", "Apple", "Pear"]
states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]
```

#### Accessing and Modifying List Items
- **How do I get an item?** I use its index (position) in square brackets, just like with string subscripting. And just like strings, the index starts at **0**.

```python
# Get the first state
first_state = states_of_america[0] # This is "Delaware"

# Get the last state using a negative index
last_state = states_of_america[-1]
```
- **How do I change an item?** I can re-assign the value at a specific index.

```python
states_of_america[1] = "Pencilvania" # Changes "Pennsylvania"
```

#### Adding Items to a List
- **How do I add one item?** The `.append()` method adds a single item to the very end of the list.

```python
states_of_america.append("Angelaland")
```
- **How do I add multiple items?** The `.extend()` method adds all the items from another list to the end.

```python
states_of_america.extend(["LandOfCode", "Pythonville"])
```

---

### 3. Debugging: The `IndexError`
This is a very common error when working with lists. An `IndexError: list index out of range` means I'm trying to access an item at an index that doesn't exist. For a list with 50 items, the valid indices are `0` to `49`. If I try to access `my_list[50]`, I'll get an `IndexError`. This is often caused by an "off-by-one" error, where I forget that the count starts at 0.

---

### 4. Nested Lists
- **What are they?** A nested list is a list that contains other lists as its items.
- **Why are they useful?** They allow for more complex data organization, like creating a matrix or grouping categories of items together.

```python
dirty_dozen = [["Strawberries", "Apples"], ["Spinach", "Kale"]]
```

---

### 5. Day 4 Project: Rock, Paper, Scissors
I built a Rock, Paper, Scissors game that I could play against the computer. This project tied together everything from the day. 
1.  **Get User Input**: I asked the user to choose Rock, Paper, or Scissors by typing 0, 1, or 2. I converted this string input to an integer.
2.  **Generate Computer's Choice**: I used `random.randint(0, 2)` to have the computer make its random choice.
3.  **Use a List for ASCII Art**: I stored the ASCII art for Rock, Paper, and Scissors in a list. This was a brilliant move because the user's and computer's choices (0, 1, or 2) could be used directly as indices to retrieve the correct artwork from the list. `game_images = [rock, paper, scissors]`
4.  **Display Choices**: I printed the corresponding ASCII art for both my choice and the computer's choice using the list and the chosen indices.
5.  **Determine the Winner**: I used a series of `if`/`elif`/`else` statements to compare my choice with the computer's choice. I had to carefully map out all the winning, losing, and draw scenarios based on the game's rules (Rock beats Scissors, Scissors beats Paper, Paper beats Rock).
6.  **Handle Invalid Input**: I added a check to make sure that if the user typed an invalid number (like 3 or -1), they would automatically lose.

Here's my final code structure:
```python
import random

rock = '''...'''
paper = '''...'''
scissors = '''...'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\\n"))

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw")
```