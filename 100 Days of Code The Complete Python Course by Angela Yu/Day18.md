# Day 18: Turtle Graphics, Tuples, and GUI Art

Welcome to my log for Day 18! Today was a deep dive into graphical programming using Python's `turtle` module. I learned how to control a virtual "turtle" to draw shapes and patterns on a screen. This lesson also covered Python Tuples, a new data structure, and explored more advanced ways of importing modules and packages. The final project was a creative one: generating a spot painting in the style of artist Damien Hirst.

## Table of Contents
- [1. Getting Started with Turtle Graphics](#1-getting-started-with-turtle-graphics)
- [2. Understanding Python Tuples](#2-understanding-python-tuples)
- [3. Generating Random RGB Colors](#3-generating-random-rgb-colors)
- [4. Advanced Module Imports](#4-advanced-module-imports)
- [5. Day 18 Project: The Hirst Spot Painting](#5-day-18-project-the-hirst-spot-painting)
- [6. Final Project Code](#6-final-project-code)

---

### 1. Getting Started with Turtle Graphics
The `turtle` module is a built-in Python library that allows for the creation of simple graphics. It's a fantastic way to visualize programming concepts.

-   **Setup:** I start by creating a `Turtle` object (the artist) and a `Screen` object (the canvas).
    ```python
    from turtle import Turtle, Screen
    
    timmy = Turtle()
    screen = Screen()
    ```
-   **Reading Documentation:** The key to using any library is reading its documentation. I learned to look up methods to control the turtle's movement (`forward()`, `right()`), pen state (`penup()`, `pendown()`), and appearance (`shape()`, `color()`, `pensize()`).
-   **Challenges:** I completed several small challenges to practice, including:
    -   Drawing a square using a `for` loop.
    -   Drawing a dashed line by alternating `penup()` and `pendown()`.
    -   Drawing a series of overlapping polygons (from a triangle to a decagon), each with a random color.
    -   Creating a "random walk" where the turtle moves in random directions.
    -   Drawing a spirograph by repeatedly drawing circles at a slight tilt.

---

### 2. Understanding Python Tuples
I was introduced to a new data structure today: the **tuple**.

-   **What is a Tuple?** A tuple is an ordered collection of items, similar to a list. However, a tuple is **immutable**, meaning once it's created, its contents cannot be changed, added to, or removed.
-   **Syntax:** Tuples are created using parentheses `()`.
    ```python
    my_tuple = (1, 3, 8)
    ```
-   **Use Case:** Tuples are great for storing data that you don't want to change accidentally. A perfect example is an RGB color value, which consists of a fixed set of three numbers (Red, Green, Blue).

---

### 3. Generating Random RGB Colors
The `turtle` module can work with RGB color values, which are represented as tuples. To generate a random color, I needed to:

1.  **Set the Color Mode:** Tell the `turtle` module to accept RGB values in the 0-255 range.
    ```python
    import turtle as t
    t.colormode(255)
    ```
2.  **Generate Random Values:** Create a function to generate three random integers between 0 and 255.
3.  **Create a Tuple:** Combine these three numbers into an RGB tuple.

```python
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b) # Return the RGB tuple

timmy.color(random_color()) # Use the random color
```

---

### 4. Advanced Module Imports
I learned about the different ways to import modules and packages, which offers flexibility in how I write my code.

1.  `import turtle`: Imports the entire module. I must use `turtle.Turtle()` to access the class.
2.  `from turtle import Turtle`: Imports a specific class. I can then just use `Turtle()` directly.
3.  `import turtle as t`: Imports the module and gives it a shorter alias. I can use `t.Turtle()`. This is very common.
4.  `from turtle import *`: Imports everything from the module. This is generally discouraged because it can lead to confusion about where functions and classes come from.

I also learned about installing **external packages** from PyPI (Python Package Index) using PyCharm's package manager. For the final project, I installed and used the `colorgram.py` package.

---

### 5. Day 18 Project: The Hirst Spot Painting
The final project was to create a piece of generative art resembling a spot painting by Damien Hirst. 
The process involved two main steps:

1.  **Color Extraction:** I used the `colorgram` library to extract a palette of colors from an image of a real Hirst painting. The library returns a list of `Color` objects, which I converted into a list of RGB tuples suitable for the `turtle` module.
2.  **Drawing the Painting:**
    -   I set up the turtle and screen, setting the `colormode` to 255.
    -   I used `penup()` to prevent the turtle from drawing lines as it moved between spots.
    -   I created a 10x10 grid of dots. I used a loop to draw a row of 10 dots, then repositioned the turtle to the start of the next row, and repeated this process 10 times.
    -   Each dot was drawn using the `dot()` method, with a size of 20 and a random color chosen from the list I extracted in the first step.

---

### 6. Final Project Code
Here is the complete and final code for my Hirst Spot Painting generator.

```python
# main.py
import turtle as turtle_module
import random

# Optional: Code to extract colors using colorgram.py
# I ran this once to get the color list and then hardcoded it.
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     # Filter out very light colors (background)
#     if r > 230 and g > 230 and b > 230:
#         continue
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (52, 93, 124), (172, 154, 44), (130, 31, 23),
              (138, 122, 158), (213, 139, 123), (133, 163, 185), (198, 93, 72), (46, 121, 86),
              (72, 43, 35), (145, 178, 149), (14, 98, 70), (232, 177, 164), (160, 142, 158),
              (105, 93, 76), (229, 172, 85), (205, 128, 148)]

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()

# Set starting position
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    # If we've drawn 10 dots, move to the next line
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
```