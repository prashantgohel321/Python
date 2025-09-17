# Day 55: Deeper into Flask and Advanced Decorators

Welcome to Day 55! Today we continued our journey into web development with Flask, exploring more advanced features that allow for dynamic and interactive web applications. We covered how to capture variables from a URL, render HTML with inline styles, use Flask's powerful debug mode, and build advanced decorators that can handle arguments. The day culminated in creating a web-based version of the "Higher or Lower" number guessing game.

## Table of Contents
- [1. Parsing Variables from URLs](#1-parsing-variables-from-urls)
- [2. Using Flask's Debug Mode](#2-using-flasks-debug-mode)
- [3. Rendering HTML and Inline Styling](#3-rendering-html-and-inline-styling)
- [4. Decorator Challenge: HTML Formatting](#4-decorator-challenge-html-formatting)
- [5. Advanced Decorators with Arguments (*args, **kwargs)](#5-advanced-decorators-with-arguments-args-kwargs)
- [6. Final Project: Higher or Lower Web Game](#6-final-project-higher-or-lower-web-game)

---

### 1. Parsing Variables from URLs
A key feature of web frameworks is the ability to create dynamic routes. We learned how to capture parts of a URL as variables.

By using angle brackets `<variable_name>` in the route decorator, Flask captures that segment of the URL and passes it as an argument to the view function. We can even specify a converter to type-cast the variable, like `<int:number>`.

```python
@app.route("/username/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route("/<int:number>")
def show_number(number):
    return f"The number is {number}"
```
This allows us to create flexible URLs that respond differently based on user input, which was the core mechanic for our final project.

---

### 2. Using Flask's Debug Mode
Continuously stopping and restarting the server during development is inefficient. We enabled Flask's debug mode to improve the workflow:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Enabling `debug=True` provides two major benefits:
-   **Automatic Reloader:** The server automatically restarts whenever a change is saved in the source code.
-   **Interactive Debugger:** If an error occurs, Flask displays a detailed traceback in the browser. This interactive debugger allows you to inspect variables and execute code in the context of the error, making it much easier to find and fix bugs.

---

### 3. Rendering HTML and Inline Styling
While we will learn more sophisticated ways to handle HTML soon, we started by returning HTML directly from our Python functions. A Flask view function can return a string of HTML, which the browser will render.

We learned to add multiple HTML elements and even apply inline CSS for styling, such as changing text color or alignment.

```python
@app.route('/')
def home():
    return '<h1 style="text-align: center;">Hello World</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="[https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif](https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif)" width=200>'
```

---

### 4. Decorator Challenge: HTML Formatting
To reinforce our understanding of decorators, we completed a challenge to create our own. The goal was to build decorators that could wrap a function's output in HTML tags.

For example, a `@make_bold` decorator would take the string returned by a function and wrap it in `<b>...</b>` tags. This was a great exercise in understanding how decorators can modify the behavior of functions.

```python
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

@app.route("/bye")
@make_bold
def say_bye():
    return "Bye"
# This would render "<b>Bye</b>" in the browser.
```

---

### 5. Advanced Decorators with Arguments (*args, **kwargs)
We took decorators a step further by learning how to make them work with functions that accept arguments. By using `*args` (arbitrary positional arguments) and `**kwargs` (arbitrary keyword arguments) in the inner `wrapper` function, we can create decorators that are flexible enough to wrap *any* function, regardless of its signature.

The arguments are caught by the wrapper and then passed along to the original function when it's called.

```python
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper

@logging_decorator
def a_function(a, b, c):
    return a * b * c

a_function(1, 2, 3)
```

---

### 6. Final Project: Higher or Lower Web Game
We combined all of today's concepts to build a fun "Higher or Lower" number guessing game.

-   **The Setup:** The server generates a random number between 0 and 9 when it starts.
-   **The Gameplay:**
    -   The home route (`/`) displays a welcome message and a GIF, prompting the user to guess a number.
    -   The user makes a guess by typing a number into the URL (e.g., `/5`).
    -   A dynamic route (`/<int:guess>`) captures this number.
    -   The function compares the user's `guess` to the random number and returns a different page for each outcome:
        -   Too high (e.g., a purple `<h1>` and a "too high" GIF).
        -   Too low (e.g., a red `<h1>` and a "too low" GIF).
        -   Correct! (e.g., a green `<h1>` and a "correct" GIF).

This project was a fantastic, hands-on way to apply URL parsing and conditional HTML rendering.

**Final Code (`main.py`):**
```python
from flask import Flask
import random

# Generate a random number once when the app starts
random_number = random.randint(0, 9)

app = Flask(__name__)

@app.route('/')
def home():
    """Homepage prompting the user to guess."""
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='[https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/](https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/)>"

@app.route("/<int:guess>")
def guess_number(guess):
    """Compares the user's guess to the random number and returns feedback."""
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='[https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/](https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/)>"
    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='[https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/](https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/)>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='[https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/](https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/)>"

if __name__ == "__main__":
    app.run(debug=True)
```