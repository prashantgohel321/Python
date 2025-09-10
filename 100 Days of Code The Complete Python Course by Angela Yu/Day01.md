# Day 1: Working with Variables in Python to Manage Data

Welcome to my log for Day 1 of the 100 Days of Code Python Bootcamp! Today was all about getting my feet wet with the fundamental building blocks of Python. I learned how to make the computer display information, handle text, get input from a user, and store data for later use. The capstone for the day was building a cool Band Name Generator program from scratch.

## Table of Contents
- [1. The `print()` Function](#1-the-print-function)
- [2. Strings and String Manipulation](#2-strings-and-string-manipulation)
  - [What is a String?](#what-is-a-string)
  - [Creating New Lines with `\n`](#creating-new-lines-with-n)
  - [String Concatenation](#string-concatenation)
- [3. The `input()` Function](#3-the-input-function)
- [4. Python Variables](#4-python-variables)
  - [What are Variables?](#what-are-variables)
  - [Variable Naming Rules](#variable-naming-rules)
- [5. Commenting My Code](#5-commenting-my-code)
- [6. Debugging: My First Encounter with Errors](#6-debugging-my-first-encounter-with-errors)
  - [`SyntaxError`](#syntaxerror)
  - [`IndentationError`](#indentationerror)
  - [`NameError`](#nameerror)
- [7. Day 1 Project: Band Name Generator](#7-day-1-project-band-name-generator)

---

### 1. The `print()` Function
- **What is it?** The `print()` function is a command I use to tell the computer to display output to the console.
- **Why do I use it?** It's the most basic way to see the result of my code, display messages to the user, or check the value of something while my program is running.
- **How do I use it?** I type the keyword `print` in all lowercase, followed by parentheses `()`. Whatever I want to display goes inside the parentheses. To print text, I have to enclose it in double quotes.

```python
# My first line of code!
print("Hello world!")
```
When I run this, the console shows the text `Hello world!` and then a message like `Process finished with exit code 0`, which means everything worked successfully.

---

### 2. Strings and String Manipulation

#### What is a String?
- **What is it?** A "String" is the programming term for a piece of text, or a sequence of characters.
- **Why do I use it?** I use strings to work with any kind of text, like names, messages, or paragraphs.
- **How do I use it?** I create a string by putting text inside quotation marks (e.g., `"this is a string"`). The quotes tell Python that the text inside is data, not a command to be executed.

#### Creating New Lines with `\n`
- **What is it?** `\n` is a special character sequence that represents a new line.
- **Why do I use it?** It allows me to format my output, printing text across multiple lines using just one `print()` command.
- **How do I use it?** I place `\n` inside a string exactly where I want the line to break.

```python
# This will print "Hello" on the first line and "World" on the second.
print("Hello\nWorld")
```

#### String Concatenation
- **What is it?** Concatenation means joining two or more strings together to form a single, longer string.
- **Why do I use it?** It's useful for combining static text with user input or other pieces of data to form a complete message.
- **How do I use it?** I use the plus `+` symbol between two strings.

```python
# This combines three strings to form a greeting.
print("Hello" + " " + "Angela")
# Output: Hello Angela
```

---

### 3. The `input()` Function
- **What is it?** The `input()` function pauses the program and waits for the user to type something into the console.
- **Why do I use it?** To make my programs interactive. It allows me to ask the user for information, like their name or city, and then use that information in my code.
- **How do I use it?** It's similar to `print()`. The text I put inside the parentheses `()` becomes the "prompt" that is displayed to the user. The text the user types is then "returned" by the function.

```python
# The program will display "What is your name? " and wait.
# The user's typed name will replace the entire input() function.
print("Hello, " + input("What is your name? ") + "!")
```
I learned that I can "nest" functions, meaning I can put one function inside another, like putting `input()` inside `print()`.

---

### 4. Python Variables

#### What are Variables?
- **What are they?** Variables are containers for storing data values. I can give a piece of data a name (the variable name) and refer to it later using that name. This is like labeling a box so I know what's inside without having to look.
- **Why do I use them?** They make my code much more readable and manageable. Instead of repeating the same data, I can store it once in a variable and reuse it. I can also easily update or change the data the variable holds.
- **How do I use them?** I use the equals sign `=` to assign a value to a variable.

```python
# The data from the input() is stored in a variable called 'name'
name = input("What is your name? ")

# I can then use the 'name' variable anywhere I need that data
print("Your name has " + str(len(name)) + " characters.")
```

#### Variable Naming Rules
I learned some important rules for naming my variables:
1.  **Readability is Key**: Names should be descriptive (e.g., `user_name` is better than `n`).
2.  **Use Underscores**: To separate words in a variable name, I should use an underscore `_` (e.g., `band_name`). Spaces are not allowed.
3.  **Numbers**: Numbers can be in a variable name, but not at the very beginning (e.g., `pet1` is okay, `1pet` is not).
4.  **No Reserved Words**: I shouldn't name my variables after built-in functions like `print` or `input`, as it can cause confusion and errors.

---

### 5. Commenting My Code
- **What is it?** Comments are notes in the code that the computer completely ignores.
- **Why do I use them?** To explain what my code is doing. This helps me (and others) understand the code when I come back to it later.
- **How do I use them?** I start a line with a hash symbol `#`. Anything after the `#` on that line is a comment.

```python
# This is a comment. The line below asks for user input.
city = input("Which city did you grow up in?\n") # This is also a comment.
```

---

### 6. Debugging: My First Encounter with Errors
Debugging is the process of finding and fixing errors ("bugs") in my code. I learned about a few common types of errors today.

#### `SyntaxError`
This happens when I write code that doesn't follow Python's grammar rules. For example, forgetting to close a quotation mark on a string. The editor's syntax highlighting often helps me spot these by changing the color of the code unexpectedly.

#### `IndentationError`
Python is very strict about spacing. This error occurs if I add an unnecessary space or tab at the beginning of a line of code where it doesn't belong.

#### `NameError`
This happens when I try to use a variable that hasn't been created yet, or if I misspell a variable's name. Python is case-sensitive, so `name` and `Name` would be two different variables.

---

### 7. Day 1 Project: Band Name Generator
I put everything I learned today into practice by building a Band Name Generator. 🎸

1.  **Greeting**: The program started by printing a welcome message.
2.  **User Input**: It then asked for two pieces of information: the city I grew up in and the name of my pet.
3.  **Variables**: I stored each piece of input in its own variable (`city` and `pet`).
4.  **String Concatenation**: I combined the two variables with a space in between to create the band name.
5.  **Final Output**: Finally, I printed the resulting band name to the console for the user to see. I also used `\n` in my input prompts to make the cursor appear on a new line, which looked much cleaner.

Here's my final code:
```python
#1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")
#2. Ask the user for the city that they grew up in.
city = input("What's the name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet = input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city + " " + pet)
```
  