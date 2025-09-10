# Day 10: Functions with Outputs and the Calculator Project

Welcome to my log for Day 10! Today's focus was on the final piece of the function puzzle: functions that have outputs. I learned how the `return` keyword works, which allows a function to pass data back to the part of the code that called it. This is a fundamental concept that enables more complex and modular programming. I also learned about writing `Docstrings` to document my functions. I applied all of this by building a calculator that can perform addition, subtraction, multiplication, and division, and even chain calculations together.

## Table of Contents
- [1. Functions with Outputs](#1-functions-with-outputs)
  - [The `return` Keyword](#the-return-keyword)
  - [`print` vs. `return`](#print-vs-return)
  - [Multiple `return` Statements](#multiple-return-statements)
- [2. Docstrings](#2-docstrings)
- [3. Day 10 Project: Calculator](#3-day-10-project-calculator)
  - [Storing Functions in a Dictionary](#storing-functions-in-a-dictionary)
  - [Implementing Recursion for New Calculations](#implementing-recursion-for-new-calculations)
- [4. Final Project Code: Calculator](#4-final-project-code-calculator)

---

### 1. Functions with Outputs

#### The `return` Keyword
So far, my functions have performed actions, but they haven't given anything back. Functions with outputs can do both.

-   **What is it?** The `return` keyword is used inside a function to specify the value that the function should output. When a `return` statement is executed, the function immediately ends, and the specified value is sent back to where the function was called.
-   **Why do I use it?** It allows a function to compute a value (like a calculation or a formatted string) and let me use that value elsewhere in my code. I can store the returned value in a variable or pass it directly into another function.
-   **How do I use it?** I use the `return` keyword followed by the value or variable I want to output.

```python
def format_name(f_name, l_name):
  # Convert names to Title Case
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  
  # Return the formatted full name
  return f"{formatted_f_name} {formatted_l_name}"

# Call the function and store its output in a variable
my_formatted_name = format_name("AnGeLA", "yU") 
print(my_formatted_name) # Output: Angela Yu
```

#### `print` vs. `return`
This was a key concept for me to grasp.
-   `print()` simply **displays** a value to the console. It's for human eyes. The program can't work with that printed value.
-   `return` **provides** a value as the output of the function. This output can be stored in a variable and used by other parts of the program. It's for the computer to use. A function can return a value without ever printing it.

#### Multiple `return` Statements
A function stops executing as soon as it hits a `return` statement. I can use this to my advantage by having conditional returns. For instance, I can perform checks at the beginning of a function and `return` early if the inputs are invalid, preventing the rest of the function's code from running unnecessarily.

```python
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs." # Early return
  
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"
```

---

### 2. Docstrings
Docstrings are a formal way to document what my functions do. They are strings placed as the very first line inside a function definition, enclosed in triple quotes (`"""Docstring goes here"""`).

When I later call that function, my code editor can show me this docstring as a hint, which is incredibly helpful for remembering what a function does, what inputs it needs, and what it returns.

```python
def add(n1, n2):
  """Adds two numbers and returns the result."""
  return n1 + n2
```

---

### 3. Day 10 Project: Calculator
The project for the day was to build a command-line calculator. 
The logic involved:
1.  Ask the user for the first number.
2.  Display the available mathematical operations (+, -, \*, /).
3.  Ask the user to pick an operation.
4.  Ask for the second number.
5.  Perform the calculation and display the result.
6.  Ask the user if they want to continue calculating with the result, or start a new calculation.

#### Storing Functions in a Dictionary
A really neat trick I learned was how to store functions inside a dictionary. This allowed me to easily select the correct mathematical operation based on the user's input. The keys were the operation symbols (`"+"`, `"-"`), and the values were the names of my functions (`add`, `subtract`).

```python
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

symbol = "+"
calculation_function = operations[symbol] # This gets the add() function
result = calculation_function(2, 3) # This is like calling add(2, 3)
```

#### Implementing Recursion for New Calculations
To handle the "start new calculation" feature, I used **recursion**. Recursion is the concept of a function calling itself. My main `calculator()` function contained all the logic. If the user chose to start a new calculation, I simply called `calculator()` again from within itself, which effectively restarted the entire process from the beginning.

---

### 4. Final Project Code: Calculator
Here is the complete and final code for my Calculator program.

```python
# main.py
import art
import os

def clear():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def add(n1, n2):
  """Adds two numbers and returns the result."""
  return n1 + n2

def subtract(n1, n2):
  """Subtracts the second number from the first and returns the result."""
  return n1 - n2

def multiply(n1, n2):
  """Multiplies two numbers and returns the result."""
  return n1 * n2

def divide(n1, n2):
  """Divides the first number by the second and returns the result."""
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(art.logo)
  
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What's the next number?: "))
    
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
```

```python
# art.py
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
```