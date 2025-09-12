# Day 22: Building the Famous Pong Game

Welcome to my log for Day 22! Today's project was to build one of the most iconic video games of all time: Pong. This was a fantastic challenge that pushed me to think carefully about game mechanics and how to structure a more complex application using Object-Oriented Programming. I broke the problem down into eight distinct steps and created separate classes for the paddles, the ball, and the scoreboard, each with its own specific behaviors and attributes.


## Table of Contents
- [1. The Plan: Decomposing the Problem](#1-the-plan-decomposing-the-problem)
- [2. Creating the Paddles](#2-creating-the-paddles)
- [3. Creating the Ball and Making It Move](#3-creating-the-ball-and-making-it-move)
- [4. Detecting Collisions and Bouncing](#4-detecting-collisions-and-bouncing)
- [5. Detecting a Miss and Keeping Score](#5-detecting-a-miss-and-keeping-score)
- [6. Final Project Code](#6-final-project-code)

---

### 1. The Plan: Decomposing the Problem
Before writing any code, I broke the game down into a series of smaller, manageable problems. This is a crucial skill for tackling any large project.
1.  **Create the Screen:** Set up the game window with the correct size and color.
2.  **Create and Move a Paddle:** Create the right-side paddle and make it respond to key presses.
3.  **Create the Second Paddle:** Create the left-side paddle and control it with different keys.
4.  **Create the Ball:** Create the ball and make it move across the screen.
5.  **Detect Wall Collision:** Make the ball bounce off the top and bottom walls.
6.  **Detect Paddle Collision:** Make the ball bounce off the paddles.
7.  **Detect a Miss:** Determine when a paddle misses the ball.
8.  **Keep Score:** Create a scoreboard that updates when a player scores.

---

### 2. Creating the Paddles
I created a `Paddle` class to serve as a blueprint for both the right and left paddles. This is a perfect example of code reuse through OOP.

-   **The `Paddle` Class (`paddle.py`):**
    -   It inherits from the `turtle.Turtle` class, giving it all the properties of a turtle.
    -   In its `__init__`, I set its shape to "square" and used `shapesize()` to stretch it into the classic rectangular paddle shape (100 pixels tall, 20 pixels wide).
    -   The `__init__` also takes a `position` tuple `(x, y)` as an argument, so I can create paddles at different starting locations (one on the right, one on the left).
    -   It contains `go_up()` and `go_down()` methods, which change the paddle's y-coordinate.
-   **In `main.py`:**
    -   I created two instances of the `Paddle` class: `r_paddle` and `l_paddle`, passing in their respective starting coordinates.
    -   I used `screen.listen()` and `screen.onkey()` to bind the arrow keys (`Up`, `Down`) to the `r_paddle`'s movement methods and the `W` and `S` keys to the `l_paddle`'s methods.

---

### 3. Creating the Ball and Making It Move
Next, I created a `Ball` class to manage its appearance and movement.

-   **The `Ball` Class (`ball.py`):**
    -   Also inherits from `turtle.Turtle`.
    -   Its shape is a "circle" and its color is "white".
    -   It has a `move()` method that continuously updates its position.
    -   I created two attributes, `x_move` and `y_move`, which determine how many pixels the ball moves on each screen refresh. By default, both were set to `10`, making the ball move diagonally. The `move()` method adds these values to the ball's current `xcor()` and `ycor()`.

---

### 4. Detecting Collisions and Bouncing
This was the core physics of the game.

-   **Wall Collision:**
    -   In the main game loop, I checked if the ball's y-coordinate (`ball.ycor()`) exceeded the top or bottom boundary of the screen (e.g., `> 280` or `< -280`).
    -   If it did, I needed to reverse its vertical direction. I created a `bounce_y()` method in the `Ball` class that simply reverses the sign of `self.y_move` (e.g., `self.y_move *= -1`).
-   **Paddle Collision:**
    -   This was trickier. I had to check two conditions: the `distance()` from the ball to the paddle, and that the ball was close to the edge of the screen (e.g., `ball.xcor() > 320`).
    -   If a collision occurred, I reversed the ball's horizontal direction. I created a `bounce_x()` method that reverses the sign of `self.x_move`.

---

### 5. Detecting a Miss and Keeping Score
The final steps were to handle scoring and resetting the ball.

-   **Detecting a Miss:** In the game loop, if the ball's x-coordinate went past the paddle's position (e.g., `ball.xcor() > 380`), it meant that player missed.
-   **Resetting:** When a miss occurred, I called a `reset_position()` method in the `Ball` class. This method sent the ball back to the center `(0, 0)` and also called `bounce_x()` to make it start moving toward the other player.
-   **The `Scoreboard` Class (`scoreboard.py`):**
    -   This class also inherits from `Turtle` and is responsible for displaying the scores.
    -   It tracks the `l_score` and `r_score`.
    -   Its `update_scoreboard()` method clears the old score and writes the new one.
    -   When a miss was detected in `main.py`, I called a method like `scoreboard.l_point()` to increment the appropriate score and trigger an update.

---

### 6. Final Project Code
Here is the complete and final code for my Pong game, organized into four separate files.

```python
# main.py
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
```

```python
# paddle.py
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
```

```python
# ball.py
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
```

```python
# scoreboard.py
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
```