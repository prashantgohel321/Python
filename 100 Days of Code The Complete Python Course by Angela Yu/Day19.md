# Day 19: Instances, State, and Higher-Order Functions

Welcome to my log for Day 19! Today was all about making my applications interactive. I learned how to listen for user events like key presses and how to manage multiple objects created from the same class, each maintaining its own independent state. This opened the door to building two classic games: an Etch-A-Sketch program and a turtle race.

## Table of Contents
- [1. Event Listeners & Higher-Order Functions](#1-event-listeners--higher-order-functions)
- [2. Project 1: Etch-A-Sketch](#2-project-1-etch-a-sketch)
- [3. Object State and Multiple Instances](#3-object-state-and-multiple-instances)
- [4. Day 19 Project: Turtle Racing Game](#4-day-19-project-turtle-racing-game)
- [5. Final Project Code](#5-final-project-code)

---

### 1. Event Listeners & Higher-Order Functions
To create interactive programs that respond to user input, I need to use **event listeners**.

-   **What is an Event Listener?** An event listener is a procedure or function that waits for an event to occur, such as a key press or a mouse click. In the `turtle` module, I use the `screen.listen()` method to make the `Screen` object start paying attention to events.

-   **Higher-Order Functions:** Python functions are "first-class citizens," which means they can be passed around just like any other variable. A **higher-order function** is a function that takes another function as an argument. The `screen.onkey()` method is a perfect example.

-   **Binding Keys to Functions:** The `screen.onkey()` method binds a function to a specific key press.
    -   `key`: The string name of the key to listen for (e.g., "space", "w", "Up").
    -   `fun`: The function to be called when the key is pressed. **Crucially, I pass the function name *without* parentheses `()`**. This passes a reference to the function itself, rather than calling it immediately.

    ```python
    from turtle import Turtle, Screen

    tim = Turtle()
    screen = Screen()

    def move_forwards():
        tim.forward(10)

    screen.listen()
    screen.onkey(key="space", fun=move_forwards) # Pass the function, don't call it
    screen.exitonclick()
    ```

---

### 2. Project 1: Etch-A-Sketch
My first challenge was to build a simple Etch-A-Sketch game. 
-   **Goal:** Control a turtle using keyboard keys to draw on the screen.
-   **Controls:**
    -   `W`: Move forwards
    -   `S`: Move backwards
    -   `A`: Turn counter-clockwise (left)
    -   `D`: Turn clockwise (right)
    -   `C`: Clear the drawing and reset the turtle to the center.
-   **Logic:** I created a separate function for each action (e.g., `move_forwards`, `turn_left`, `clear_screen`). Then, I created a series of `screen.onkey()` listeners, each binding one of my functions to its corresponding key.

---

### 3. Object State and Multiple Instances
This was a key OOP concept for building the racing game.

-   **Instance:** An instance is a specific object created from a class. If `Turtle` is the blueprint, then `timmy` and `tommy` would be two separate instances created from that blueprint.
    ```python
    timmy = Turtle()
    tommy = Turtle()
    ```
-   **State:** The state refers to the current values of an object's attributes at any given moment. `timmy` and `tommy` are independent of each other. `timmy` can have a `color` attribute set to "green" while `tommy`'s is "purple". They can be at different positions and have different headings. This independence is what allows them to act as individual racers in the game.

---

### 4. Day 19 Project: Turtle Racing Game
The main project for the day was a turtle racing game, which brought together all the concepts I learned.

-   **Setup:** I configured the screen to a specific `width` and `height`.
-   **User Bet:** I used `screen.textinput()` to create a pop-up window asking the user to bet on which color turtle would win.
-   **Creating the Racers:**
    -   I created a list of colors (e.g., `["red", "orange", "yellow", "green", "blue", "purple"]`).
    -   I used a `for` loop to create multiple `Turtle` objects (instances), one for each color.
    -   Each turtle instance was given its unique color and starting position. I used `goto(x, y)` to line them all up on the left side of the screen at different Y-coordinates.
-   **The Race Logic:**
    -   The race was run inside a `while` loop that continues as long as a `is_race_on` flag is `True`.
    -   Inside the loop, I iterated through my list of turtle objects.
    -   For each turtle, I generated a random distance and moved it forward using `turtle.forward()`.
    -   After each move, I checked the turtle's x-coordinate (`turtle.xcor()`). If it crossed the finish line (the right edge of the screen), the loop would stop.
-   **Determining the Winner:**
    -   When a turtle crossed the finish line, I got its color using `turtle.pencolor()`.
    -   I compared this winning color to the `user_bet` to determine if the user won or lost and printed the result.

---

### 5. Final Project Code
Here is the complete and final code for my Turtle Racing Game.

```python
# main.py
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
```