# Day 30: Errors, Exceptions, and JSON Data Files

Welcome to my log for Day 30! This was a significant day where I moved beyond basic programming and into building more robust and resilient applications. I learned how to anticipate and handle errors gracefully using Python's **Exception Handling** mechanism. I also learned about the **JSON** data format, a universal standard for storing structured data, which allowed me to significantly upgrade the Password Manager project from yesterday.


## Table of Contents
- [1. Catching Exceptions: The `try`, `except`, `else`, `finally` Pattern](#1-catching-exceptions-the-try-except-else-finally-pattern)
- [2. Raising My Own Exceptions with `raise`](#2-raising-my-own-exceptions-with-raise)
- [3. Working with JSON Data](#3-working-with-json-data)
- [4. Project: Upgraded Password Manager](#4-project-upgraded-password-manager)
- [5. Final Project Code](#5-final-project-code)

---

### 1. Catching Exceptions: The `try`, `except`, `else`, `finally` Pattern
Errors happen, and until now, they've been crashing my programs. Today I learned how to handle them gracefully.

-   **What is it?** Exception handling is a way to manage runtime errors. Instead of the program halting, I can define a block of code to execute when a specific error occurs.
-   **Why do I use it?** To make my applications more robust. For example, if my program tries to open a file that doesn't exist (`FileNotFoundError`), it shouldn't crash. Instead, it can handle that specific error, perhaps by creating the file for the first time.
-   **How do I use it?** The pattern involves four keywords:
    -   `try`: A block of code that might cause an exception.
    -   `except`: A block of code that runs **only if** an exception occurred in the `try` block. I can specify which error to catch (e.g., `except FileNotFoundError:`).
    -   `else`: A block of code that runs **only if** no exceptions occurred in the `try` block.
    -   `finally`: A block of code that runs **no matter what**, whether an exception occurred or not. This is great for cleanup actions, like closing a file.

```python
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["non_existent_key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
```

---

### 2. Raising My Own Exceptions with `raise`
Sometimes, code might be syntactically correct but logically flawed (e.g., a user entering a height of 4 meters). In these cases, I can create my own error.

-   **What is it?** The `raise` keyword allows me to trigger my own exception at any point in the code.
-   **Why do I use it?** To stop the program from continuing with nonsensical data and to provide specific, custom error messages.
-   **How do I use it?** I simply use the `raise` keyword followed by the type of error I want to create (e.g., `ValueError`, `TypeError`).

```python
height = float(input("Height: "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
```

---

### 3. Working with JSON Data
JSON (JavaScript Object Notation) is a lightweight, human-readable format for storing and exchanging data. It looks very similar to Python dictionaries.

-   **What is it?** A standard file format that uses key-value pairs, making it perfect for storing structured data.
-   **Why do I use it?** It's a much better way to store complex data than a plain text file. It maintains the structure of dictionaries and lists, making it easy to search and update.
-   **How do I use it?** Python has a built-in `json` module.
    -   **Writing JSON (`json.dump()`):** To write a Python dictionary to a JSON file. The `indent` parameter makes the file human-readable.
    -   **Reading JSON (`json.load()`):** To read a JSON file and convert it into a Python dictionary.
    -   **Updating JSON (`json.update()`):** This is a three-step process: 1. Read the existing JSON data (`json.load`). 2. Use the dictionary's `.update()` method to add or modify data. 3. Write the entire updated dictionary back to the file (`json.dump`).

---

### 4. Project: Upgraded Password Manager
The project for the day was to take the Password Manager from Day 29 and make it significantly better.

-   **My Process:**
    1.  **Data Storage:** I changed the data storage from a simple `data.txt` file to a `data.json` file. This allows me to store the passwords in a structured way, with the website name as the primary key.
    2.  **Saving Data:** The `save()` function was updated to handle JSON. It now uses the read-update-write pattern. I wrapped this logic in a `try-except` block to handle the `FileNotFoundError` that occurs the very first time the program is run.
    3.  **Search Functionality:** I added a "Search" button and a corresponding `find_password()` function.
    4.  **Implementing Search:** The search function gets the website name from the user. It then tries to open and read `data.json`.
    5.  **Exception Handling in Search:**
        -   It catches a `FileNotFoundError` if no passwords have been saved yet.
        -   If the file is found, it loads the JSON into a dictionary and checks if the website key exists.
        -   If the key exists, it retrieves the email and password and displays them in a `messagebox`.
        -   If the key doesn't exist, it displays a different `messagebox` informing the user that no details for that website were found.

---

### 5. Final Project Code

```python
# main.py
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
```