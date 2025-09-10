# Day 6: Python Functions and While Loops

Welcome to my log for Day 6. Today was about leveling up my coding skills by learning how to create my own functions and understanding a new kind of loop, the `while` loop. Functions allow me to package up code to make it reusable and more readable, which is incredibly powerful. `while` loops give me another way to control the flow of my program by repeating actions until a specific condition is met. I spent the day applying these concepts in a fun, visual environment called Reeborg's World, where I programmed a robot to navigate through a series of increasingly difficult hurdles and mazes.

## Table of Contents
- [1. Defining and Calling Functions](#1-defining-and-calling-functions)
- [2. Indentation in Python](#2-indentation-in-python)
- [3. `while` Loops](#3-while-loops)
  - [`for` Loop vs. `while` Loop](#for-loop-vs-while-loop)
  - [The Danger of Infinite Loops](#the-danger-of-infinite-loops)
- [4. Day 6 Project: Escaping the Maze](#4-day-6-project-escaping-the-maze)

---

### 1. Defining and Calling Functions
Up until now, I've been *using* built-in functions like `print()` and `len()`. Today, I learned how to create my own.

- **What is it?** A function is a named block of code that performs a specific task. I can define it once and then "call" it (run it) whenever I need it.
- **Why do I use them?** To avoid repeating myself (the DRY principle - Don't Repeat Yourself) and to make my code more organized and readable. Instead of writing the same ten lines of code in five different places, I can put them in a function and just call that function's name.
- **How do I create one?**
    1.  **Define** the function using the `def` keyword, followed by the function's name, parentheses `()`, and a colon `:`.
    2.  **Indent** all the code that belongs to the function on the following lines.
    3.  **Call** the function by writing its name followed by parentheses.

```python
# 1. Defining the function
def turn_right():
  turn_left()
  turn_left()
  turn_left()

# 2. Calling the function
turn_right() 
```
In the Reeborg's World exercises, the robot only knew how to `turn_left()`. By creating a `turn_right()` function, I made my code much easier to understand and write.

---

### 2. Indentation in Python
Today really hammered home how important indentation (the spaces at the beginning of a line) is in Python.

- **What is it?** Indentation is how Python determines the grouping of statements. It's used to define a **code block**.
- **Why is it important?** Unlike many other languages that use curly braces `{}` to define code blocks, Python uses whitespace. Everything indented under a `def`, `if`, `for`, or `while` statement is considered part of that block. Incorrect indentation will lead to an `IndentationError`.
- **How do I do it?** The standard convention is to use **four spaces** for each level of indentation. Most code editors, including the one I'm using, will automatically insert four spaces when I press the `Tab` key.

---

### 3. `while` Loops
I learned a new type of loop today that works differently from the `for` loops I learned yesterday.

- **What is it?** A `while` loop executes a block of code **as long as a certain condition is true**.
- **Why do I use it?** It's perfect for situations where I don't know in advance how many times the loop needs to run. I just want it to keep going until some goal is reached or some state changes.
- **How do I use it?** I use the `while` keyword, followed by a condition and a colon. The loop continues as long as the condition evaluates to `True`.

```python
# This robot will keep jumping until it reaches the goal.
while not at_goal():
  jump()
```

#### `for` Loop vs. `while` Loop
I now understand the key difference between the two loops:
-   **Use a `for` loop** when I want to iterate over a finite sequence of items (like each item in a list) or when I want to run a loop a specific number of times (`for i in range(6)`).
-   **Use a `while` loop** when I want the loop to continue until a condition is no longer met, and I don't necessarily know how many iterations that will take.

#### The Danger of Infinite Loops
A `while` loop can be dangerous if the condition *never* becomes false. This creates an **infinite loop**, where the program gets stuck and runs forever (or until it crashes). This can happen if I forget to include code inside the loop that changes the condition. For example, if I'm counting down a number, I have to remember to subtract from it in each iteration.

---

### 4. Day 6 Project: Escaping the Maze
The final project was to write a single program that could guide a robot through any randomly generated maze.  The robot's starting position and direction were also random.

The key to solving this was an algorithm called the "right-hand rule." By making the robot always try to keep a wall to its right, it would eventually find the exit.

1.  **Main Logic (`while` loop)**: The core of the program was a `while` loop that kept the robot moving as long as it was not at the goal: `while not at_goal():`.
2.  **Define `turn_right()`**: Just like in the exercises, I first defined a `turn_right()` function to make the logic cleaner.
3.  **Conditional Algorithm (`if`/`elif`/`else`)**: Inside the `while` loop, I implemented the "right-hand rule" with a series of checks:
    -   `if right_is_clear():` If there's no wall on the right, the robot should turn right and move forward one step. This is its first priority.
    -   `elif front_is_clear():` If it can't turn right (because there's a wall), its next priority is to just move forward.
    -   `else:` If it can't go right and it can't go forward, the only option left is to `turn_left()`.

This simple set of hierarchical rules, repeated over and over by the `while` loop, was powerful enough to solve any maze presented. It was a fantastic demonstration of how simple programming concepts can be combined to solve very complex problems.
 