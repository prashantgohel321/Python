# Day 23: The Turtle Crossing Game (Capstone Project)

Welcome to my log for Day 23! Today's challenge was the second major capstone project: building a "Crossy Road" style game using the turtle module. This project was a significant step up in complexity, requiring me to design and implement multiple interacting classes from scratch. I created a `Player` class for the turtle, a `CarManager` to handle the traffic, and a `Scoreboard` to track the player's level. It was a comprehensive test of my Object-Oriented Programming skills.


## Table of Contents
- [1. The Plan: Decomposing the Problem](#1-the-plan-decomposing-the-problem)
- [2. The Player Class](#2-the-player-class)
- [3. The Car Manager Class](#3-the-car-manager-class)
- [4. The Scoreboard Class](#4-the-scoreboard-class)
- [5. Putting It All Together: The Main Game Loop](#5-putting-it-all-together-the-main-game-loop)
- [6. Final Project Code](#6-final-project-code)

---

### 1. The Plan: Decomposing the Problem
The game, while simple in concept, involves several independent components that need to interact. I broke the project down into five main steps:

1.  **Move the Turtle:** Create a `Player` class that represents the turtle. It should start at the bottom of the screen and move upwards when the "Up" arrow key is pressed.
2.  **Create and Move the Cars:** Create a `CarManager` class to periodically generate new cars at random positions on the right side of the screen. These cars should move continuously from right to left.
3.  **Detect Turtle Collision:** If the player turtle collides with any of the cars, the game should end.
4.  **Detect Successful Crossing:** When the turtle reaches the top edge of the screen, it should return to its starting position, and the game should level up, making the cars move faster.
5.  **Create a Scoreboard:** Create a `Scoreboard` class to display the current level, which increases after each successful crossing. It should also display a "GAME OVER" message upon collision.

---

### 2. The Player Class
The `Player` class is responsible for everything related to the user-controlled turtle.

-   **The `Player` Class (`player.py`):**
    -   Inherits from `turtle.Turtle`.
    -   In `__init__`, I set its shape to "turtle", lifted the pen, and set its heading to North (90 degrees). It's initialized at a starting position defined by a constant.
    -   It has a `go_up()` method that moves the turtle forward by a set distance.
    -   It has a `go_to_start()` method to reset its position after a successful crossing.
    -   A boolean method `is_at_finish_line()` checks if the turtle's y-coordinate has passed the finish line.

---

### 3. The Car Manager Class
The `CarManager` class handles the creation, movement, and speed of all the cars.

-   **The `CarManager` Class (`car_manager.py`):**
    -   This class does **not** inherit from `Turtle` because it's a manager, not a single object to be drawn. Instead, it creates and manages a list of `Turtle` objects.
    -   **Attributes:** It holds a list of all car objects (`all_cars`) and tracks the current `car_speed`.
    -   **Methods:**
        -   `create_car()`: This method has a 1-in-6 chance of being triggered in each game loop. When it is, it creates a new `Turtle` object, shapes it into a rectangle, gives it a random color from a predefined list, and places it at a random y-position on the right edge of the screen. The new car is then added to the `all_cars` list.
        -   `move_cars()`: This loops through the `all_cars` list and moves each car to the left by the current `car_speed`.
        -   `level_up()`: This method is called when the player successfully crosses. It increases the `car_speed` attribute, making the game more difficult.

---

### 4. The Scoreboard Class
The `Scoreboard` class is very similar to the one from the Pong game, handling all on-screen text.

-   **The `Scoreboard` Class (`scoreboard.py`):**
    -   Inherits from `turtle.Turtle`.
    -   It tracks the current `level`.
    -   `update_scoreboard()` clears the previous text and writes the new level.
    -   `increase_level()` increments the level attribute and calls the update method.
    -   `game_over()` writes "GAME OVER" in the center of the screen.

---

### 5. Putting It All Together: The Main Game Loop
The `main.py` file orchestrates the entire game.
1.  It sets up the screen and initializes the `Player`, `CarManager`, and `Scoreboard` objects.
2.  It listens for the "Up" key to move the player.
3.  The main `while` loop runs continuously:
    -   It calls `car_manager.create_car()` and `car_manager.move_cars()` on every iteration.
    -   It checks for collision between the player and each car in the `car_manager.all_cars` list. If a collision is detected, the loop ends.
    -   It checks if the player has reached the finish line. If so, it resets the player's position, levels up the car manager, and increases the scoreboard level.

---

### 6. Final Project Code
Here is the complete and final code for my Turtle Crossing game, organized into four separate files.

```python
# main.py
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
```

```python
# player.py
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
```

```python
# car_manager.py
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
```

```python
# scoreboard.py
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
```