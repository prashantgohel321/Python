# Day 28: Building a GUI Pomodoro Timer with Tkinter

Welcome to my log for Day 28! Today's project was to build a fully functional desktop application from scratch: a Pomodoro Timer. This was a fantastic exercise in creating a more dynamic GUI using **Tkinter**. I learned how to use the `Canvas` widget to layer images and text, a crucial skill for more complex interfaces. I also tackled the important concept of handling time-based events in a GUI without freezing the program, and implemented the complete logic for the Pomodoro Technique.


## Table of Contents
- [1. The Tkinter Canvas Widget](#1-the-tkinter-canvas-widget)
- [2. Handling Time and Countdowns in a GUI](#2-handling-time-and-countdowns-in-a-gui)
- [3. Python's Dynamic Typing](#3-pythons-dynamic-typing)
- [4. Project: The Pomodoro Timer](#4-project-the-pomodoro-timer)
- [5. Final Project Code](#5-final-project-code)

---

### 1. The Tkinter Canvas Widget
The `Canvas` is one of Tkinter's most powerful widgets. Unlike simpler widgets that just hold one thing (like a label or a button), the canvas is like a real artist's canvas, allowing me to place and layer multiple elements on top of each other.

-   **Creating a Canvas:** I initialized it just like any other widget, specifying a width and height.
-   **Placing an Image:** To put the tomato image on the canvas, I first had to load it using `tkinter.PhotoImage`. Then, I used `canvas.create_image()` to place it at a specific (x, y) coordinate on the canvas.
-   **Layering Text:** To place the timer text *on top* of the image, I used `canvas.create_text()`. This method also takes x and y coordinates, along with arguments for the text content, font, and color.
-   **Updating Canvas Items:** A key learning point was that to change an item on the canvas (like the timer text), I need to use the `canvas.itemconfig()` method, passing it the ID of the item I want to change and the new configuration (e.g., `text="new text"`).

---

### 2. Handling Time and Countdowns in a GUI
A major challenge in any GUI programming is dealing with time. A simple `while` loop with a `time.sleep()` call will freeze the entire application, because it blocks the `mainloop()` from listening to user events.

-   **Event-Driven Programming:** GUIs are "event-driven." They sit in a `mainloop`, constantly listening for events (like button clicks). Blocking this loop makes the app unresponsive.
-   **The `.after()` Method:** Tkinter provides a brilliant solution with the `window.after()` method. It works by scheduling a function to be called after a specified delay (in milliseconds) *without* blocking the mainloop.
-   **Creating a Recursive Loop:** I created the countdown effect by having my `count_down()` function call `window.after()` on itself.

    ```python
    def count_down(count):
        # ... update the UI with the count ...
        if count > 0:
            window.after(1000, count_down, count - 1) # Wait 1 sec, then call itself with a decremented count
    ```
-   **Cancelling the Timer:** I also learned to use `window.after_cancel()` to stop the scheduled function call, which was essential for the "Reset" button functionality. This required storing the ID returned by `window.after()` in a variable.

---

### 3. Python's Dynamic Typing
During this project, I encountered a practical example of Python's **dynamic typing**. To format the timer display correctly (e.g., showing "05" instead of "5"), I needed to conditionally change the data type of my seconds variable.

-   If the `count_sec` was an integer less than 10, I could reassign it to a formatted **string** like `f"0{count_sec}"`.
-   Python allows a variable's type to change during runtime, which is not possible in statically-typed languages like C++ or Java. While powerful, it's something to be mindful of.

---

### 4. Project: The Pomodoro Timer
The goal was to create a desktop app to help with the Pomodoro productivity technique (25 min work, 5 min break, with a longer break after 4 work sessions).

-   **My Process:**
    1.  **UI Setup:** I created the main window, used a `Canvas` to display the tomato image and the timer text. I added the "Timer" label, "Start" and "Reset" buttons, and a label for checkmarks, arranging everything with the `.grid()` layout manager.
    2.  **Timer Logic:** I implemented the `count_down()` function using `window.after()` to handle the second-by-second countdown and update the text on the canvas.
    3.  **Pomodoro Cycle:** The `start_timer()` function was the brain of the app. It tracked the number of repetitions (`reps`) to determine whether the next session should be a work period, a short break, or a long break, and then started the `count_down()` with the correct duration.
    4.  **Reset Mechanism:** The `reset_timer()` function was connected to the reset button. It used `window.after_cancel()` to stop the timer, reset the timer text and title, and cleared the checkmarks.
    5.  **User Feedback:** The UI provides clear feedback by changing the title label to "Work" or "Break" (with different colors) and adding a checkmark for each completed work session.

---

### 5. Final Project Code

```python
# main.py
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
```