# Day 24: Working with Files, Directories, and Paths

Welcome to my log for Day 24! Today was all about making my programs interact with the local file system. This is a crucial skill for any application that needs to save data persistently. I started by upgrading my Snake Game to remember the high score between sessions. The main event was building a Mail Merge program, a practical tool for automating personalized letters, which taught me about file paths and directory navigation.

## Table of Contents
- [1. Reading and Writing to Files](#1-reading-and-writing-to-files)
- [2. Project 1: Upgrading the Snake Game with a High Score](#2-project-1-upgrading-the-snake-game-with-a-high-score)
- [3. Understanding File Paths: Absolute vs. Relative](#3-understanding-file-paths-absolute-vs-relative)
- [4. Project 2: The Mail Merge Challenge](#4-project-2-the-mail-merge-challenge)
- [5. Final Project Code (Mail Merge)](#5-final-project-code)

---

### 1. Reading and Writing to Files
I learned the fundamental techniques for file I/O (Input/Output) in Python.

-   **Opening Files:** I used the built-in `open()` function. The best practice is to use the `with` keyword, which automatically handles closing the file once the block is exited, preventing resource leaks.
    ```python
    with open("my_file.txt") as file:
        # Do something with the file
    ```
-   **Modes:** The `open()` function takes a `mode` argument:
    -   `mode="r"` (Read Only): This is the default. It allows me to read the file's contents but not change them.
    -   `mode="w"` (Write Only): This allows me to write to the file. **Important:** It deletes all existing content in the file. If the file doesn't exist, it will be created.
    -   `mode="a"` (Append Only): This allows me to add new content to the end of the file without deleting what's already there.

-   **Reading and Writing:**
    -   `.read()`: Reads the entire content of the file as a single string.
    -   `.readlines()`: Reads the file and returns a list of strings, where each item is a line from the file.
    -   `.write("New text")`: Writes a string to the file.

---

### 2. Project 1: Upgrading the Snake Game with a High Score
The first application of my new file I/O skills was to make the Snake Game's high score persistent.

1.  **Create a Data File:** I created a `data.txt` file in the project directory, which initially just contained the number `0`.
2.  **Read the High Score:** In the `Scoreboard` class's `__init__` method, I opened `data.txt` in read mode, read the number, converted it to an integer, and assigned it to the `self.high_score` attribute.
3.  **Write the New High Score:** In the `reset()` method (which is called when the player loses), I checked if the current `score` was greater than the `high_score`. If it was, I updated the `self.high_score` attribute and then opened `data.txt` in **write mode** to overwrite the old score with the new one.

Now, the high score is saved even after I close and reopen the game!

---

### 3. Understanding File Paths: Absolute vs. Relative
A file's location is defined by its path. I learned about the two main types:

-   **Absolute File Path:** The full address of a file starting from the root directory of the computer. It is independent of the current working directory.
    -   *Example (Mac/Linux):* `/Users/Angela/Desktop/my_file.txt`
    -   *Example (Windows):* `C:\Users\Angela\Desktop\my_file.txt`
-   **Relative File Path:** The path to a file starting from the current working directory (where the script is being run). This is often more portable.
    -   `./my_file.txt` or `my_file.txt`: A file in the same folder.
    -   `../another_folder/my_file.txt`: Goes up one level to the parent directory, then into `another_folder`.


---

### 4. Project 2: The Mail Merge Challenge
This was the main project for the day, designed to automate a common, repetitive task.

-   **The Goal:** Take a starting letter template (`starting_letter.txt`) and a list of names (`invited_names.txt`), and generate a personalized letter for each person, saving it as a new file.

-   **My Process:**
    1.  **Get the Names:** I opened `Input/Names/invited_names.txt` and used `.readlines()` to get a list of names.
    2.  **Clean the Names:** Each name from `.readlines()` had a newline character (`\n`) at the end. I learned to use the `.strip()` method in a loop to remove this unwanted whitespace from each name.
    3.  **Get the Letter Template:** I opened `Input/Letters/starting_letter.txt` and used `.read()` to get the entire letter content as a single string.
    4.  **Replace and Save:** I looped through my cleaned list of names. In each iteration:
        -   I used the `.replace()` method on the letter template string to swap the placeholder `[name]` with the current name.
        -   I created a new file path for the output letter (e.g., `Output/ReadyToSend/letter_for_Aang.txt`), using an f-string to insert the person's name.
        -   I opened this new file in write mode (`"w"`) and wrote the personalized letter content to it.

This project was a great demonstration of how a few lines of Python can automate a task that would have taken much longer to do manually.

---

### 5. Final Project Code (Mail Merge)

```python
# main.py

# A placeholder to be replaced in the letter template
PLACEHOLDER = "[name]"

# Open the file containing the list of names to invite
with open("./Input/Names/invited_names.txt") as names_file:
    # .readlines() creates a list where each line from the file is an item
    names = names_file.readlines()

# Open the starting letter template
with open("./Input/Letters/starting_letter.txt") as letter_file:
    # .read() gets the entire content of the file as a single string
    letter_contents = letter_file.read()
    
    # Loop through each name in the list of names
    for name in names:
        # Remove any leading/trailing whitespace (including the newline character '\n')
        stripped_name = name.strip()
        
        # Replace the placeholder in the letter with the current name
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        
        # Create a new file for the personalized letter in the output directory
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            # Write the content of the personalized letter to the new file
            completed_letter.write(new_letter)

```