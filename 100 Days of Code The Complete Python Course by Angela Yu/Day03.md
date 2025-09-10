# Day 3: Control Flow and Logical Operators

Welcome to my log for Day 3! This was a really exciting day because I learned how to give my programs a "brain." I can now write code that makes decisions based on certain conditions. This is called control flow, and it's what makes programs smart and interactive. I learned about `if`, `else`, and `elif` statements, which let me create branching paths in my code. The final project was to build a classic "Choose Your Own Adventure" game, which was a perfect way to apply these new skills.

## Table of Contents
- [1. Conditional Statements: `if` / `else`](#1-conditional-statements-if--else)
  - [Comparison Operators](#comparison-operators)
- [2. The Modulo Operator `%`](#2-the-modulo-operator-)
- [3. Nested `if` / `else` Statements](#3-nested-if--else-statements)
- [4. The `elif` Statement](#4-the-elif-statement)
- [5. Multiple `if` Statements](#5-multiple-if-statements)
- [6. Logical Operators](#6-logical-operators)
  - [`and`](#and)
  - [`or`](#or)
  - [`not`](#not)
- [7. Day 3 Project: Treasure Island - Choose Your Own Adventure](#7-day-3-project-treasure-island---choose-your-own-adventure)

---

### 1. Conditional Statements: `if` / `else`
- **What are they?** `if` and `else` are keywords that let me execute different blocks of code depending on whether a condition is `True` or `False`. It's like a fork in the road for my program.
- **Why do I use them?** To make my program respond differently to different situations. For example, checking if a user is tall enough to ride a roller coaster.
- **How do I use them?** The structure is key. I start with `if`, followed by a condition and a colon `:`. The code to run if the condition is true is indented on the next line(s). The `else` block is at the same indentation level as the `if`, also followed by a colon, and its code is also indented.

```python
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the roller coaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")
```
**Indentation is not optional in Python; it's how Python knows which code belongs to which block!**

#### Comparison Operators
I use these operators inside the `if` statement to form the condition:
- `>`: Greater than
- `<`: Less than
- `>=`: Greater than or equal to
- `<=`: Less than or equal to
- `==`: **Equal to**. I have to use a double equals sign to check for equality. A single equals sign (`=`) is for assigning a value to a variable.
- `!=`: Not equal to

---

### 2. The Modulo Operator `%`
- **What is it?** The modulo operator (`%`) gives me the **remainder** of a division.
- **Why do I use it?** It's a clever way to check for divisibility. A common use case is determining if a number is even or odd.
- **How do I use it?** If `number % 2` equals `0`, the number is even because it divides perfectly by 2 with no remainder. If the remainder is `1`, the number is odd.

```python
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
```

---

### 3. Nested `if` / `else` Statements
- **What are they?** A nested `if`/`else` is an `if` statement that is placed *inside* another `if` or `else` block.
- **Why do I use them?** To check for a second (or third, or fourth...) condition *after* a previous condition has already been met. It creates a more complex, multi-layered decision process.
- **How do I use them?** The key is indentation. The nested `if` statement is indented inside the outer `if` block.

```python
if height >= 120:
  print("You can ride.")
  age = int(input("What is your age? "))
  if age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you can't ride.")
```

---

### 4. The `elif` Statement
- **What is it?** `elif` is short for "else if". It lets me check for multiple different conditions in a sequence.
- **Why do I use it?** When I have more than two possible outcomes. Instead of nesting `if` statements over and over, `elif` keeps the code cleaner and flatter.
- **How do I use it?** It goes between an `if` and an `else`. The program checks the `if` condition first. If it's false, it checks the first `elif`. If that's false, it checks the next `elif`, and so on. If none of the `if` or `elif` conditions are true, the `else` block is executed.

```python
if age < 12:
  print("Please pay $5.")
elif age <= 18:
  print("Please pay $7.")
else:
  print("Please pay $12.")
```

---

### 5. Multiple `if` Statements
- **What is the difference?** Unlike an `if`/`elif`/`else` structure where only *one* block of code will run, using multiple separate `if` statements means that **every `if` condition will be checked independently**.
- **Why do I use this?** When I need to check for several different conditions that aren't mutually exclusive. For example, adding extra toppings to a pizza. The customer could want pepperoni *and* extra cheese.
- **How do I use it?** I just write one `if` statement after another, at the same indentation level.

```python
bill = 0
# ... code to determine initial bill based on pizza size ...

wants_pepperoni = input("Do you want pepperoni? Y or N ")
if wants_pepperoni == "Y":
  bill += 2

wants_extra_cheese = input("Do you want extra cheese? Y or N ")
if wants_extra_cheese == "Y":
  bill += 1

print(f"Your final bill is ${bill}")
```

---

### 6. Logical Operators
- **What are they?** These operators allow me to combine multiple conditions in a single `if` statement.
- **Why do I use them?** To create more complex and specific conditions without deeply nested `if` statements.

#### `and`
Both conditions must be `True` for the overall statement to be `True`.
```python
if age >= 45 and age <= 55:
  print("Have a free ride on us!")
```

#### `or`
Only one of the conditions needs to be `True` for the overall statement to be `True`.
```python
if day == "Saturday" or day == "Sunday":
  print("It's the weekend!")
```

#### `not`
Reverses a condition. It makes a `True` condition `False`, and a `False` condition `True`.
```python
if not is_raining:
  print("Go for a walk!")
```
---

### 7. Day 3 Project: Treasure Island - Choose Your Own Adventure
I used all of today's concepts to build a text-based adventure game. The game's story progressed based on the user's choices.

1.  **Story and ASCII Art**: I started with a welcome message and some cool ASCII art to set the scene.
2.  **First Choice (`if`/`else`)**: The user was presented with a choice (e.g., "left" or "right"). I used an `if`/`else` statement to handle the two outcomes. One path led to a "Game Over," and the other continued the story.
3.  **Handling User Input**: I learned to use the `.lower()` string method on the user's input. This converted their answer to all lowercase, so my program would work whether they typed "Left", "left", or "LEFT".
4.  **Nested Logic**: The continuing path led to another choice, which required a nested `if`/`else` statement inside the first `if` block.
5.  **Final Choice (`if`/`elif`/`else`)**: The final stage presented three choices (e.g., three colored doors). This was a perfect use case for an `if`/`elif`/`else` structure to handle the multiple possible outcomes, with only one correct answer leading to victory.

This project was a fantastic way to see how simple `if`/`else` blocks can be combined to create complex and branching logic.
```python
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\\n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\\n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\\n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")
```