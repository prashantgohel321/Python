# Day 31: Capstone Project - Flash Card App

Welcome to my log for Day 31! This was the third capstone project, and it was a really satisfying one to build: a language learning flashcard application called "Flashy." The project was a comprehensive review of many topics, requiring me to combine **Tkinter** for the user interface, **Pandas** for reading and managing the word data, and local file I/O to save my learning progress. The app helps me learn new vocabulary by showing a word, then flipping the card to reveal the translation, and intelligently removing words I've already learned.


## Table of Contents
- [1. Project Goal and Features](#1-project-goal-and-features)
- [2. Reading Word Data with Pandas](#2-reading-word-data-with-pandas)
- [3. Building the User Interface](#3-building-the-user-interface)
- [4. Flipping the Card with a Delay](#4-flipping-the-card-with-a-delay)
- [5. Saving and Loading User Progress](#5-saving-and-loading-user-progress)
- [6. Final Project Code](#6-final-project-code)

---

### 1. Project Goal and Features
The main goal was to build a desktop app that helps memorize foreign language vocabulary.
-   **Display a word:** Show a word from a foreign language (in this case, French).
-   **Flip the card:** After a 3-second delay, the card should flip to show the English translation.
-   **Track known words:** If I know the word (click the checkmark button), it should be removed from the list of words to learn. If I don't know it (click the cross button), it stays in the deck.
-   **Save progress:** The list of words I still need to learn should be saved to a file, so I can pick up where I left off next time.

---

### 2. Reading Word Data with Pandas
The vocabulary for the app is stored in a CSV file. Pandas is the perfect tool for reading this data.

-   **Reading the CSV:** I used `pandas.read_csv()` to load the word data into a DataFrame.
-   **Converting to a Dictionary List:** A plain DataFrame isn't the easiest to iterate through for this application. A more useful structure is a list of dictionaries, where each dictionary represents a word pair (e.g., `{'French': 'partie', 'English': 'part'}`). I achieved this conversion with a single line: `data.to_dict(orient="records")`. The `orient="records"` parameter is key here, as it structures the dictionary in exactly this way.

---

### 3. Building the User Interface
The UI was built entirely with Tkinter and centered around a `Canvas` widget.

-   **The Canvas:** The canvas was essential because it allowed me to layer multiple components:
    1.  A background card image (`card_front.png` or `card_back.png`).
    2.  A title text ("French" or "English").
    3.  A word text (the actual vocabulary word).
-   **Image Buttons:** The 'right' and 'wrong' buttons were created by setting the `image` property of a `Button` widget to a `PhotoImage` object.
-   **Layout:** I used the `.grid()` layout manager to arrange all the elements, using `columnspan` for the canvas to ensure it stretched over both button columns for a balanced look.

---

### 4. Flipping the Card with a Delay
The core interactive feature is the card flip, which required careful timing to avoid freezing the UI.

-   **Using `window.after()`:** I used the `window.after(3000, flip_card)` method to schedule the `flip_card` function to run after 3000 milliseconds (3 seconds). This is non-blocking and allows the UI to remain responsive.
-   **Updating the Canvas:** The `flip_card()` function uses `canvas.itemconfig()` to change the elements on the canvas. It updates the background image, the title text, the word text, and the text color.
-   **Cancelling the Timer:** A key bug-fix was to cancel the pending flip if the user clicks a button before the 3 seconds are up. I stored the ID returned by `window.after()` in a global variable (`flip_timer`) and then used `window.after_cancel(flip_timer)` at the start of the `next_card()` function to prevent the old timer from firing.

---

### 5. Saving and Loading User Progress
To make the app a useful study tool, it needed to remember which words I've already learned.

-   **Loading Words:** When the app starts, it first tries to open a `words_to_learn.csv` file.
    -   I used a `try-except` block to handle the `FileNotFoundError` that occurs on the first run.
    -   If the file is found, it's loaded with Pandas.
    -   If it's not found, the app loads the original, complete `french_words.csv`.
-   **Removing Known Words:** When the user clicks the "known" (checkmark) button, the `is_known()` function is called. This function removes the current card (dictionary) from the main list of words.
-   **Saving Progress:** After removing the word, the app immediately saves the updated list back to `words_to_learn.csv`. I created a new Pandas DataFrame from the shortened list and used `df.to_csv("data/words_to_learn.csv", index=False)`. Setting `index=False` was crucial to prevent Pandas from adding an extra index column to the CSV on each save.

---

### 6. Final Project Code

```python
# main.py
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
```