# Day 21: Building the Snake Game - Part 2

Welcome to my log for Day 21! Today, I finished the Snake Game project by tackling the remaining four steps. This was a fantastic lesson in advanced Object-Oriented Programming and Python techniques. I learned about **class inheritance**, which allowed me to create specialized `Food` and `Scoreboard` classes based on the `Turtle` class. I also learned about **slicing**, a powerful way to work with sequences like lists, which made the tail collision logic much cleaner.

## Table of Contents
- [1. Class Inheritance](#1-class-inheritance)
- [2. Step 4: Detecting Collision with Food](#2-step-4-detecting-collision-with-food)
- [3. Step 5: Creating a Scoreboard](#3-step-5-creating-a-scoreboard)
- [4. Step 6: Detecting Collision with the Wall](#4-step-6-detecting-collision-with-the-wall)
- [5. Slicing in Python](#5-slicing-in-python)
- [6. Step 7: Detecting Collision with the Tail](#6-step-7-detecting-collision-with-the-tail)
- [7. Final Project Code (Part 2)](#7-final-project-code)

---

### 1. Class Inheritance
Class inheritance is a core concept in OOP that allows a new class (the *subclass* or *child class*) to take on the attributes and methods of an existing class (the *superclass* or *parent class*).

-   **Why use it?** It promotes code reuse. Instead of building a new class from scratch, I can inherit from a well-established one and just add or modify the specific functionality I need.
-   **Syntax:** To make a class inherit, I place the name of the superclass in parentheses after the new class's name.

    ```python
    class Fish(Animal): # Fish inherits from Animal
        def __init__(self):
            super().__init__() # Initializes all attributes/methods from Animal
    ```

For the Snake Game, both my `Food` and `Scoreboard` classes inherited from the `turtle.Turtle` class. This meant they instantly had all the capabilities of a turtle (like `goto()`, `color()`, `shape()`, `write()`) without me needing to rewrite any of that code. I could then add specialized methods, like `refresh()` for the food or `update_scoreboard()` for the score.

---

### 2. Step 4: Detecting Collision with Food
This step involved creating a `Food` class and logic to detect when the snake eats it.

-   **The `Food` Class:**
    -   Inherits from `turtle.Turtle`.
    -   In its `__init__`, it sets its own shape to a circle, color to blue, and size to be smaller than the snake segments.
    -   It has a `refresh()` method that uses `random.randint()` to move the food to a new random location on the screen.
-   **Collision Detection:**
    -   I used the `turtle.distance()` method, which calculates the distance between two turtle objects.
    -   In the main game loop, I checked `if snake.head.distance(food) < 15:`.
    -   If the distance was less than 15 pixels (a small buffer), I considered it a collision.
    -   When a collision occurred, I called `food.refresh()`, `scoreboard.increase_score()`, and `snake.extend()`.

---

### 3. Step 5: Creating a Scoreboard
I created a dedicated `Scoreboard` class to handle displaying and updating the score.

-   **The `Scoreboard` Class:**
    -   Also inherits from `turtle.Turtle`.
    -   **Attributes:** It keeps track of the `score`, starting at 0.
    -   **Methods:**
        -   `__init__()`: Sets the turtle's color to white, hides the turtle icon (`hideturtle()`), lifts the pen (`penup()`), and moves to the top of the screen to display the initial score.
        -   `update_scoreboard()`: Clears the previous score (`clear()`) and writes the new score using `self.write()`.
        -   `increase_score()`: Increments the `score` attribute and calls `update_scoreboard()`.
        -   `game_over()`: Writes "GAME OVER" in the center of the screen when the game ends.

---

### 4. Step 6: Detecting Collision with the Wall
This logic determines when the game should end because the snake has gone out of bounds.

-   **Logic:** I checked the `x` and `y` coordinates of the snake's head in the main game loop.
-   The screen was 600x600, so the coordinates range from -300 to 300. I set the boundaries slightly smaller (e.g., 280) to make the collision look more natural.
-   If `snake.head.xcor() > 280` or `snake.head.xcor() < -280` (or the equivalent for the y-axis), I set `game_is_on = False` to end the game loop and called `scoreboard.game_over()`.

---

### 5. Slicing in Python
Slicing is a concise way to get a portion of a list or tuple.

-   **Syntax:** `list[start:stop:step]`
-   **Examples:**
    -   `piano_keys[2:5]`: Gets items from index 2 up to (but not including) index 5.
    -   `piano_keys[2:]`: Gets items from index 2 all the way to the end.
    -   `piano_keys[:5]`: Gets items from the beginning up to (but not including) index 5.
    -   `piano_keys[::-1]`: A neat trick to reverse a list.

---

### 6. Step 7: Detecting Collision with the Tail
The final piece of game logic was to end the game if the snake's head collides with any part of its body.

-   **Logic:** I needed to check the distance between the snake's head and every other segment in its body.
-   **Slicing in Action:** Instead of a complex loop with an `if` statement to skip the head, I used slicing to create a new list containing just the tail segments: `snake.segments[1:]`.
-   I then looped through this `tail` slice. If `snake.head.distance(segment) < 10`, it meant a collision occurred, and I ended the game.

---

### 7. Final Project Code (Part 2)
Here is the complete and final code for the Snake Game, organized into four separate files.

```python
# main.py
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
```

```python
# snake.py
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
```

```python
# food.py
from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
```

```python
# scoreboard.py
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
```