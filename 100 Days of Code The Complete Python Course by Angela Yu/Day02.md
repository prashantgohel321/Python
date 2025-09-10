# Day 2: Understanding Data Types and How to Manipulate Strings

This is my log for Day 2 of my 100-day Python journey. Today, I dove into the fundamental concept of data types. I learned that Python treats different kinds of data, like text and numbers, in very different ways. Understanding this was the key to unlocking mathematical operations and building the final project for today: a practical Tip Calculator.

## Table of Contents
- [1. Primitive Data Types](#1-primitive-data-types)
  - [String and Subscripting](#string-and-subscripting)
  - [Integer](#integer)
  - [Float](#float)
  - [Boolean](#boolean)
- [2. Type Checking and Conversion](#2-type-checking-and-conversion)
  - [Checking Data Types with `type()`](#checking-data-types-with-type)
  - [Type Conversion (Casting)](#type-conversion-casting)
- [3. Mathematical Operations](#3-mathematical-operations)
  - [Operators and Order of Operations (PEMDAS)](#operators-and-order-of-operations-pemdas)
- [4. Number Manipulation and f-Strings](#4-number-manipulation-and-f-strings)
  - [The `round()` Function](#the-round-function)
  - [Assignment Operators](#assignment-operators)
  - [f-Strings: A Game Changer](#f-strings-a-game-changer)
- [5. Debugging: The `TypeError`](#5-debugging-the-typeerror)
- [6. Day 2 Project: Tip Calculator](#6-day-2-project-tip-calculator)

---

### 1. Primitive Data Types
I learned that "primitive" data types are the most basic building blocks for data in Python.

#### String and Subscripting
- **What is it?** A String is a sequence of characters, essentially just text. I already knew this from Day 1. What was new to me was **subscripting**. This is the process of pulling out a specific character from a string.
- **Why do I use it?** It's incredibly useful when I only need a part of a string, like the first letter.
- **How do I use it?** I use square brackets `[]` after the string and put the index (position) of the character I want. I had to remember a crucial rule: **programmers start counting from 0!**

```python
# Getting the first character 'H'
print("Hello"[0])
# Output: H

# Getting the last character 'o'
print("Hello"[4])
# Output: o
```

#### Integer
- **What is it?** An Integer (`int`) is a whole number, positive or negative, without any decimals.
- **Why do I use it?** For counting things, like the number of users or items.
- **How do I use it?** I just write the number without any quotes. I also learned a cool trick for making large numbers more readable: I can use underscores `_` as separators, and Python will just ignore them.

```python
# A simple integer
my_number = 123

# A large, readable integer
large_number = 1_000_000 # Python sees this as 1000000
```

#### Float
- **What is it?** A Float (or a floating-point number) is a number that has a decimal point.
- **Why do I use it?** For any data that requires more precision, like prices, measurements, or scientific calculations.
- **How do I use it?** I write the number with a decimal point.

```python
pi = 3.14159
```

#### Boolean
- **What is it?** A Boolean (`bool`) is a data type that can only have two values: `True` or `False`.
- **Why do I use it?** To represent logical states, like whether a user is logged in or if a game is over. They are the foundation of decision-making in code.
- **How do I use it?** I write the words `True` or `False` with a capital first letter and no quotes.

```python
is_game_over = False
is_logged_in = True
```

---

### 2. Type Checking and Conversion

#### Checking Data Types with `type()`
- **What is it?** The `type()` function is a built-in tool that tells me the data type of any piece of data or variable.
- **Why do I use it?** It's essential for debugging. If my code isn't working, I can use `type()` to check if my data is the type I expect it to be.
- **How do I use it?** I place the data or variable inside the `type()` function's parentheses.

```python
print(type(123))      # Output: <class 'int'>
print(type(3.14))     # Output: <class 'float'>
print(type("Hello"))  # Output: <class 'str'>
```

#### Type Conversion (Casting)
- **What is it?** Type conversion (or casting) is the process of changing a piece of data from one type to another.
- **Why do I use it?** This is incredibly important. For instance, the `input()` function always gives me a string. If I want to do math with that input, I *must* first convert it to an integer or a float.
- **How do I use it?** I use functions named after the data type I want to convert to, like `int()`, `float()`, and `str()`.

```python
num_char = len(input("What is your name?"))

# This will cause a TypeError! I can't concatenate a string with an integer.
# print("Your name has " + num_char + " characters.")

# I must convert the integer to a string first.
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
```

---

### 3. Mathematical Operations

#### Operators and Order of Operations (PEMDAS)
- **What are they?** These are the symbols I use to perform math: `+` (add), `-` (subtract), `*` (multiply), and `/` (divide). I also learned about `**` for exponents (e.g., `2**3` is 2 to the power of 3).
- **Why are they important?** They are the foundation of any calculation. I also learned that the order in which they are performed matters a lot. Python follows the standard mathematical order of operations, which I remember as **PEMDAS**:
    - **P**arentheses `()`
    - **E**xponents `**`
    - **M**ultiplication `*` and **D**ivision `/` (equal importance, evaluated left-to-right)
    - **A**ddition `+` and **S**ubtraction `-` (equal importance, evaluated left-to-right)
- **How do I use them?**

```python
# Python will do 3 * 3 first, then 3 / 3, then add and subtract.
print(3 * 3 + 3 / 3 - 3) # Evaluates to 9 + 1.0 - 3 = 7.0

# Using parentheses changes the order. 3 + 3 is done first.
print(3 * (3 + 3) / 3 - 3) # Evaluates to 3 * 6 / 3 - 3 = 3.0
```
I also learned that standard division (`/`) always results in a `float` (e.g., `6 / 3` is `2.0`).

---

### 4. Number Manipulation and f-Strings

#### The `round()` Function
- **What is it?** A function to round numbers to the nearest integer or to a specified number of decimal places.
- **Why do I use it?** To make output cleaner and more user-friendly, especially when dealing with money or long decimals.
- **How do I use it?**

```python
print(round(8 / 3))       # Rounds to the nearest whole number: 3
print(round(8 / 3, 2))    # Rounds to 2 decimal places: 2.67
```

#### Assignment Operators
- **What are they?** Shorthand operators to modify a variable's value based on its current value.
- **Why do I use them?** They make code more concise. It's common to update a variable, like a user's score.
- **How do I use them?**

```python
score = 0
score += 1  # This is the same as score = score + 1
print(score) # Output: 1
```

#### f-Strings: A Game Changer
- **What is it?** An f-String is a much easier way to embed variables and expressions directly inside a string.
- **Why do I use it?** It saves me from the headache of manual type conversion with `str()` and messy concatenation with `+` signs. It's a huge improvement in readability and convenience.
- **How do I use it?** I just put the letter `f` right before the opening quote of the string. Then, I can put any variable or expression inside curly braces `{}` directly in the string, and Python handles the rest.

```python
score = 0
height = 1.8
is_winning = True

# Old, messy way
# print("Your score is " + str(score) + ", your height is " + str(height))

# New, clean f-String way
print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}")
```

---

### 5. Debugging: The `TypeError`
Today, I encountered the `TypeError`. This error happens when I try to perform an operation on a data type that doesn't support it. The most common example I ran into was trying to add a string and a number together. This error is a big clue that I need to check the types of my variables and probably perform a type conversion.

---

### 6. Day 2 Project: Tip Calculator
I combined all the concepts from today to build a program that calculates how much each person in a group should pay for a bill, including a tip.

1.  **Welcome Message**: I started with a simple `print()` statement.
2.  **Get Inputs**: I used the `input()` function to ask for the total bill, the desired tip percentage, and the number of people splitting the bill.
3.  **Type Conversion**: This was the most important step. I converted the bill input to a `float` and the tip and people inputs to `int`s so I could perform calculations with them.
4.  **Math**: I calculated the total amount (bill + tip) and then divided that by the number of people.
5.  **Rounding**: The result was often a long decimal, so I used the `round()` function to format it to two decimal places, which is appropriate for money.
6.  **f-String Output**: I used an f-String to present the final, rounded amount to the user in a clear and readable sentence.

Here's my final code for the project:
```python
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

# Using an f-String to display the final result.
print(f"Each person should pay: ${final_amount}")
```