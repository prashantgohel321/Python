# Day 20: Building the Snake Game - Part 1

Welcome to my log for Day 20! Today, I embarked on a nostalgic two-day project: building the classic Snake Game. This first part focused on setting up the game environment and creating the core mechanics of the snake itself. I practiced problem decomposition by breaking the game into seven distinct steps and tackled the first three: creating the snake's body, making it move automatically, and adding keyboard controls. The most significant part of today's lesson was encapsulating all the snake's logic into its own `Snake` class, a major step in applying Object-Oriented Programming.


## Table of Contents
- [1. Breaking Down the Problem](#1-breaking-down-the-problem)
- [2. Step 1: Creating the Snake's Body](#2-step-1-creating-the-snakes-body)
- [3. Step 2: Animating the Snake's Movement](#3-step-2-animating-the-snakes-movement)
- [4. Step 3: Controlling the Snake with Keys](#4-step-3-controlling-the-snake-with-keys)
- [5. OOP in Practice: The `Snake` Class](#5-oop-in-practice-the-snake-class)
- [6. Final Project Code (Part 1)](#6-final-project-code)

---

### 1. Breaking Down the Problem
Before writing any code, I planned the entire project by breaking it down into seven manageable steps. On Day 20, I focused on the first three:
1.  **Create the Snake Body:** Display three square segments on the screen to form the initial snake.
2.  **Move the Snake:** Animate the snake so it moves forward continuously.
3.  **Control the Snake:** Allow the user to change the snake's direction using the arrow keys.

The remaining steps (food collision, scoreboard, wall collision, and tail collision) will be covered on Day 21.

---

### 2. Step 1: Creating the Snake's Body
The first task was to create the visual representation of the snake.
-   I used the `turtle` module to create three square-shaped `Turtle` objects.
-   Each segment is 20x20 pixels. I positioned them next to each other by setting their coordinates. For example, the first at `(0, 0)`, the second at `(-20, 0)`, and the third at `(-40, 0)`.
-   I used a `for` loop and a list of starting positions to create these segments efficiently instead of coding each one manually.

---

### 3. Step 2: Animating the Snake's Movement
This was the most complex part of today's lesson. Simply moving each segment forward doesn't work, as they would separate when the snake turns. The solution was to make the tail follow the head.

-   **Screen Animation Control:** To create smooth movement, I turned off the default turtle animations using `screen.tracer(0)`. This allows me to manually control when the screen updates. I then used `screen.update()` inside my main game loop to refresh the screen after all segments have moved for that frame. A small delay with `time.sleep()` controls the speed of the game.

-   **Movement Logic:** The key was to move the segments from tail to head.
    1.  The last segment moves to the position where the second-to-last segment was.
    2.  The second-to-last segment moves to the position of the segment in front of it.
    3.  This continues until I reach the head of the snake.
    4.  Finally, only the head segment moves forward into a new position.

This logic ensures that the snake's body perfectly follows the path of its head, allowing it to turn corners correctly. I implemented this using a `for` loop that iterates backward through the snake's segments.

---

### 4. Step 3: Controlling the Snake with Keys
To make the game interactive, I added keyboard controls.
-   I used the `screen.listen()` and `screen.onkey()` methods, just as I did in the Etch-A-Sketch game.
-   I created methods within my `Snake` class for `up()`, `down()`, `left()`, and `right()`. These methods change the heading of the snake's head segment.
-   I added logic to prevent the snake from immediately reversing direction. For example, if the snake is moving right, the `left()` method will be ignored. This is a classic rule of the Snake game.

---

### 5. OOP in Practice: The `Snake` Class
To keep my code organized and modular, I refactored all the logic related to the snake into a dedicated `Snake` class in a separate `snake.py` file.

-   **Attributes:**
    -   `segments`: A list to store all the `Turtle` objects that make up the snake's body.
    -   `head`: A reference to the first segment of the snake (`self.segments[0]`).
-   **Methods:**
    -   `__init__()`: Initializes the snake by calling `create_snake()`.
    -   `create_snake()`: Creates the initial three segments and adds them to the `segments` list.
    -   `move()`: Implements the tail-follows-head movement logic described above.
    -   `up()`, `down()`, `left()`, `right()`: The control methods that change the snake's heading.

This refactoring made my `main.py` file incredibly simple and readable. It's now only responsible for setting up the screen, creating the `Snake` object, and running the main game loop.

---

### 6. Final Project Code (Part 1)
Here is the complete code for the first part of the Snake Game, split into two files.

```python
# main.py
from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

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
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

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