# Day 8: Functions with Inputs & Caesar Cipher Project

Welcome to my log for Day 8! Today, I went beyond simple functions and learned how to make them truly powerful by passing in data. This opened up a whole new world of possibilities, moving from functions that do the same thing every time to functions that can adapt based on the inputs they receive. I learned the key difference between parameters and arguments and explored positional vs. keyword arguments. The day's project was to build a classic cryptography tool: the Caesar Cipher.

## Table of Contents
- [1. Functions with Inputs](#1-functions-with-inputs)
  - [Parameter vs. Argument](#parameter-vs-argument)
- [2. Positional vs. Keyword Arguments](#2-positional-vs-keyword-arguments)
- [3. Day 8 Project: Caesar Cipher](#3-day-8-project-caesar-cipher)
  - [Part 1: The Encryption Function](#part-1-the-encryption-function)
  - [Part 2: The Decryption Function](#part-2-the-decryption-function)
  - [Part 3: Refactoring and Final Touches](#part-3-refactoring-and-final-touches)
- [4. Final Project Code: Caesar Cipher](#4-final-project-code-caesar-cipher)

---

### 1. Functions with Inputs
While the functions I wrote on Day 6 were useful, they were static—they did the exact same thing every time. Today, I learned to make them dynamic.

-   **What is it?** A function with an input is a function that can accept a piece of data when it's called, and then use that data inside its code block.
-   **Why do I use it?** It allows a single function to be much more versatile. For example, instead of a function that just prints "Hello", I can create a `greet()` function that takes a name as an input and prints "Hello, Angela" or "Hello, Jack".
-   **How do I create one?** I add a variable name inside the parentheses when I define the function. This variable acts as a placeholder for the data that will be passed in.

#### Parameter vs. Argument
I learned two important terms related to function inputs:
-   **Parameter**: The name of the input variable inside the function's definition. It's the placeholder.
-   **Argument**: The actual piece of data that I pass to the function when I call it. It's the value that fills the placeholder.

```python
# 'name' is the PARAMETER
def greet(name):
  print(f"Hello, {name}")
  print(f"How do you do, {name}?")

# "Angela" is the ARGUMENT
greet("Angela") 
```

---

### 2. Positional vs. Keyword Arguments
When a function has multiple inputs, the way I provide the arguments matters.

-   **Positional Arguments**: This is the default way. The arguments I pass in are assigned to parameters based on their position. The first argument goes to the first parameter, the second to the second, and so on. This is simple but can lead to errors if I mix up the order.

    ```python
    def greet_with(name, location):
      print(f"Hello {name}")
      print(f"What is it like in {location}?")
    
    # name becomes "Angela", location becomes "London"
    greet_with("Angela", "London") 
    ```

-   **Keyword Arguments**: To avoid positional errors and make my code more readable, I can explicitly name the parameters when I call the function. With keyword arguments, the order no longer matters.

    ```python
    # The order is swapped, but the result is the same
    # because the keywords link the arguments to the correct parameters.
    greet_with(location="London", name="Angela")
    ```
---

### 3. Day 8 Project: Caesar Cipher
The project for the day was to create a program that can encrypt and decrypt messages using the Caesar Cipher technique, where each letter in a message is shifted by a certain number of places down the alphabet. 
#### Part 1: The Encryption Function
The first step was to create an `encrypt` function that would shift letters *forwards*.
-   The function took two inputs: the `text` to encrypt and the `shift` amount.
-   I created a list of all the letters in the alphabet.
-   Inside the function, I looped through each `letter` in the input `text`.
-   For each letter, I found its `position` (index) in the alphabet list using `alphabet.index(letter)`.
-   I calculated the `new_position` by adding the `shift` amount to the original `position`.
-   I retrieved the `new_letter` from the alphabet list at the `new_position`.
-   **Wrapping the Alphabet**: A key challenge was handling letters near the end of the alphabet. For example, if I shift 'z' by 5, I should wrap around to 'e'. I solved this by realizing that I could simply duplicate the alphabet list (`alphabet += alphabet`), making it long enough that I wouldn't go out of range for any reasonable shift.

#### Part 2: The Decryption Function
Next, I created a `decrypt` function to shift letters *backwards*. The logic was nearly identical to the `encrypt` function, but instead of adding the shift amount, I **subtracted** it from the letter's position.

#### Part 3: Refactoring and Final Touches
Having two functions (`encrypt` and `decrypt`) that were 95% the same was inefficient. The final part of the project was to refactor them into a single, more elegant solution.
-   **Single `caesar()` Function**: I combined the logic into one function called `caesar()` that took a third parameter: `direction` ('encode' or 'decode').
-   **Conditional Shift**: Inside the function, I used an `if` statement. If the direction was 'decode', I multiplied the `shift` amount by -1. This clever trick allowed me to use the same line of code (`new_position = position + shift_amount`) for both encrypting (adding a positive number) and decrypting (adding a negative number).
-   **User Experience**:
    -   I added a `while` loop to let the user run the program again after a run was complete.
    -   I improved the logic to handle numbers, symbols, and spaces by checking if a character was in the alphabet list. If it wasn't, I just appended the character to the result without trying to shift it.
    -   I imported a cool ASCII art logo from a separate `art.py` file to make the program look better.

---

### 4. Final Project Code: Caesar Cipher
Here is the complete and final code for my Caesar Cipher program.

```python
# main.py
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

print(art.logo)

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # In case the user enters a shift greater than 26
  shift = shift % 26
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_continue = False
    print("Goodbye")
```

```python
# art.py
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             
"""
```