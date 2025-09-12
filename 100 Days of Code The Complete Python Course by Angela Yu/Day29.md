# Day 29: Building a Password Manager GUI

Welcome to my log for Day 29! Today’s project was to build a very useful desktop application: a password manager called "MyPass." This project was a great opportunity to build a more complex GUI with **Tkinter**, practice saving data to files, and integrate logic from a previous project (the password generator). I also learned how to use pop-up message boxes for user interaction and a new library, `pyperclip`, to copy text to the clipboard.


## Table of Contents
- [1. Advanced Grid Layout with `columnspan`](#1-advanced-grid-layout-with-columnspan)
- [2. UI/UX Enhancements: Focus, Insert, and Delete](#2-uiux-enhancements-focus-insert-and-delete)
- [3. Saving Data to a File](#3-saving-data-to-a-file)
- [4. Pop-up Dialogs with `messagebox`](#4-pop-up-dialogs-with-messagebox)
- [5. Password Generation and Clipboard Integration](#5-password-generation-and-clipboard-integration)
- [6. Final Project Code](#6-final-project-code)

---

### 1. Advanced Grid Layout with `columnspan`
To create the layout for the password manager, I needed some widgets to span across multiple grid columns. The `columnspan` argument in the `.grid()` method was perfect for this.

-   **How it works:** `widget.grid(column=1, row=4, columnspan=2)` tells the widget to start in column 1 on row 4, but to take up the space of two columns instead of just one.
-   **Application:** I used `columnspan` for the "Website" and "Email" entry fields, as well as the final "Add" button, to make them stretch across the UI for a clean and organized look.

---

### 2. UI/UX Enhancements: Focus, Insert, and Delete
I learned a few new methods to make the application more user-friendly:

-   **`.focus()`:** Calling `website_entry.focus()` immediately after creating the UI places the cursor directly into the website entry field, so the user can start typing right away.
-   **`.insert()`:** I used `email_entry.insert(0, "myemail@example.com")` to pre-populate the email field with a default value. The `0` index means the text is inserted at the beginning. The constant `END` can be used to append text.
-   **`.delete()`:** To clear the input fields after the user saves the password, I used `website_entry.delete(0, END)`. This deletes all characters from the beginning (index 0) to the end.

---

### 3. Saving Data to a File
When the user clicks the "Add" button, the app needs to save the website, email, and password to a local file.

-   **Process:**
    1.  I retrieved the text from each `Entry` widget using the `.get()` method.
    2.  I used `with open("data.txt", "a") as data_file:` to open a file in **append mode** (`"a"`). This adds new entries to the end of the file without overwriting existing ones. If the file doesn't exist, it gets created automatically.
    3.  I wrote the formatted string (e.g., `Website | Email | Password\n`) to the file. The `\n` is crucial for putting each new entry on its own line.

---

### 4. Pop-up Dialogs with `messagebox`
To provide feedback, I used Tkinter's `messagebox` module, which needs to be explicitly imported: `from tkinter import messagebox`.

-   **Error/Info Pop-ups:** For simple validation, like checking if fields were empty, I used `messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")`. This displays a simple pop-up with an "OK" button.
-   **Confirmation Pop-ups:** Before saving the data, I used `messagebox.askokcancel()` to ask for user confirmation. This function returns a boolean value (`True` if OK is clicked, `False` if Cancel is clicked), which I used in an `if` statement to decide whether to proceed with saving the file.

---

### 5. Password Generation and Clipboard Integration
I integrated the password generator logic from Day 5 to make the app more powerful.

-   **Refactoring:** I refactored the Day 5 code, wrapping it in a `generate_password()` function. This function now populates the password `Entry` field directly using `.insert()`.
-   **`pyperclip` Library:** To make the generated password immediately useful, I used the external `pyperclip` library.
    -   After installing it, I could simply call `pyperclip.copy(password)` to copy the newly generated password string to the system clipboard. This allows the user to immediately paste it into a website's sign-up form.

---

### 6. Final Project Code

```python
# main.py
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

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
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
```