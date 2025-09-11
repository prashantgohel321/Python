# Day 12: Scope & The Number Guessing Game

Welcome to my log for Day 12! Today's lesson was focused on a fundamental and sometimes tricky programming concept: **Scope**. I learned about the difference between variables created inside functions (local scope) versus those created outside (global scope). This knowledge is crucial for avoiding common bugs. The project for the day was a significant milestone: I built a "Guess the Number" game entirely from scratch, without any starter code, forcing me to think through the logic and structure from the very beginning.

## Table of Contents
- [1. Understanding Scope in Python](#1-understanding-scope-in-python)
  - [Local Scope](#local-scope)
  - [Global Scope](#global-scope)
  - [There is No Block Scope in Python](#there-is-no-block-scope-in-python)
- [2. Modifying a Global Variable](#2-modifying-a-global-variable)
  - [The `global` Keyword](#the-global-keyword)
  - [The Better Approach: Using `return`](#the-better-approach-using-return)
- [3. Global Constants](#3-global-constants)
- [4. Day 12 Project: Number Guessing Game](#4-day-12-project-number-guessing-game)
- [5. Final Project Code: Guess the Number](#5-final-project-code-guess-the-number)

---

### 1. Understanding Scope in Python
Scope refers to the region of a program where a particular variable is accessible. Think of it like a variable's "lifespan" or "visibility."

#### Local Scope
-   **What is it?** A variable created **inside a function** has a local scope.
-   **Why is it important?** It means the variable is only accessible from within that function. Once the function finishes executing, the variable is destroyed and can't be accessed from outside. This prevents variables in different functions from accidentally interfering with each other.
-   **Example:**

    ```python
    def drink_potion():
      potion_strength = 2 # local variable
      print(potion_strength)

    drink_potion()
    # print(potion_strength) # This would cause a NameError
    ```

#### Global Scope
-   **What is it?** A variable created in the main body of a Python file (i.e., not inside any function) has a global scope.
-   **Why is it important?** It means the variable can be accessed from anywhere in the file, both inside and outside of functions.
-   **Example:**

    ```python
    player_health = 10 # global variable

    def drink_potion():
      print(player_health) # Can access the global variable

    drink_potion()
    ```

#### There is No Block Scope in Python
This was a key takeaway. Unlike some other languages, creating a variable inside an `if`, `while`, or `for` loop **does not** create a new local scope. The variable is still accessible within the scope where the loop itself resides (e.g., within the function, or globally if the loop is not in a function).

```python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy) # This works! new_enemy is accessible globally.
```

---

### 2. Modifying a Global Variable
Simply trying to change a global variable from within a local scope can be tricky. If I assign a new value to a variable inside a function that has the same name as a global variable, Python creates a *new local variable* instead of modifying the global one.

#### The `global` Keyword
-   **What is it?** The `global` keyword explicitly tells Python that inside a function, I want to modify a global variable, not create a new local one.
-   **Why is it used?** It's the direct way to modify a global variable from a local scope. However, it's generally considered bad practice because it can make code confusing and hard to debug. It's often difficult to track where and when a global variable is being changed.

    ```python
    enemies = 1

    def increase_enemies():
      global enemies
      enemies += 1
      print(f"enemies inside function: {enemies}")

    increase_enemies()
    print(f"enemies outside function: {enemies}")
    # Both will now print 2
    ```

#### The Better Approach: Using `return`
A much cleaner and safer way to "modify" a global variable is to avoid modifying it directly. Instead, I can have the function `return` the new value. Then, outside the function, I can update the global variable with this returned value. This makes the flow of data explicit and much easier to follow.

```python
enemies = 1

def increase_enemies():
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}") # Prints 2
```

---

### 3. Global Constants
-   **What are they?** Global constants are variables that I define globally and never intend to change. They hold values that are constant throughout the program, like the value of PI or a URL.
-   **Why are they useful?** They make my code more readable by giving a descriptive name to a static value.
-   **How do I define them?** The convention in Python is to write the variable name in all **UPPERCASE** letters, with words separated by underscores. This signals to other developers (and my future self) that this value should not be modified.

```python
PI = 3.14159
EASY_LEVEL_TURNS = 10
```

---

### 4. Day 12 Project: Number Guessing Game
The project for the day was to build a number guessing game. This was the first time I had to create a program from a completely blank file. 
The logic I implemented:
1.  The computer picks a random number between 1 and 100.
2.  The program asks the user to choose a difficulty level: 'easy' (10 guesses) or 'hard' (5 guesses).
3.  I stored the number of turns for each difficulty as global constants.
4.  A `while` loop continues as long as the player has guesses remaining and hasn't guessed the correct number.
5.  Inside the loop, the player is told how many attempts they have left and prompted to make a guess.
6.  A function `check_answer()` compares the guess to the actual number and provides feedback ("Too high." or "Too low.").
7.  Each incorrect guess reduces the number of turns by 1.
8.  If the player guesses correctly, they win, and the loop ends.
9.  If the player runs out of turns, they lose, and the game reveals the answer.

---

### 5. Final Project Code: Guess the Number
Here is the complete and final code for my Number Guessing Game.

```python
# main.py
import random
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(art.logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)
  # print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()
```

```python
# art.py
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
```