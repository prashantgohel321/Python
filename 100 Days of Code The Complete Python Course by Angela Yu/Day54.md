# Day 54: Introduction to Web Development with Flask

Welcome to Day 54! Today marks a major shift in the bootcamp as we dive into the world of **web development with Python**. This was a foundational lesson packed with crucial concepts that form the bedrock of building web applications. We explored what a web server is, how to build one with the **Flask framework**, the importance of the **command line**, and the advanced Python concept of **decorators**.

## Table of Contents
- [1. Understanding Web Development: Frontend vs. Backend](#1-understanding-web-development-frontend-vs-backend)
- [2. Introduction to Flask](#2-introduction-to-flask)
- [3. Getting Started with the Command Line](#3-getting-started-with-the-command-line)
- [4. Understanding Python Decorators](#4-understanding-python-decorators)
- [5. Our First Flask Server](#5-our-first-flask-server)

---

### 1. Understanding Web Development: Frontend vs. Backend
A website isn't just the HTML and CSS that you see. Modern web applications are split into two main parts:

-   **Frontend (Client-Side):** This is what the user sees and interacts with in their browser. It's built with HTML (for structure), CSS (for style), and JavaScript (for interactivity). Think of this as the dining area of a restaurant—where the customers are.
-   **Backend (Server-Side):** This is the engine of the website. It handles the business logic, processes data, and interacts with databases. It can be built with various languages, including Python. This is the restaurant's kitchen, taking orders (requests) and preparing the food (data) before sending it out.

The **client** (your browser) sends a **request** to the **server** (a powerful, always-on computer). The server processes this request, often fetching data from a **database**, and then sends a **response** back to the client, which is rendered as a webpage.

---

### 2. Introduction to Flask
Flask is a popular and lightweight "micro" web framework for Python. But what's a framework?

-   A **library** is a collection of code that *you call* when you need it (e.g., `requests.get()`).
-   A **framework** is a structure that *calls your code*. You write functions that fit into the framework's architecture, and the framework executes them at the appropriate time (e.g., when a user visits a specific URL).

Flask provides the essential tools to build a web server without being overly complex, making it perfect for beginners and small-to-medium-sized projects.

---

### 3. Getting Started with the Command Line
The command line (or terminal/shell) is a powerful text-based interface for controlling your computer. It's faster and offers more control than a graphical user interface for many development tasks.

Key commands we learned:
-   `pwd` (Print Working Directory): Shows your current location in the file system.
-   `ls` (List): Lists all files and folders in the current directory.
-   `cd <directory>` (Change Directory): Navigates into a specified folder (e.g., `cd Desktop`). `cd ..` goes up one level.
-   `mkdir <name>` (Make Directory): Creates a new folder.
-   `touch <filename>`: Creates a new, empty file.
-   `rm <filename>` (Remove): Deletes a file. `rm -rf <foldername>` deletes a folder and everything inside it (use with caution!).

We also used the command line to set up our Flask environment and run the server.

---

### 4. Understanding Python Decorators
Decorators are an advanced Python feature used heavily in Flask. A decorator is a function that takes another function as input, adds some functionality to it (or "wraps" it), and returns the modified function.

The syntax uses the `@` symbol, which is "syntactic sugar" for this wrapping process.

To understand decorators, we reviewed key concepts:
1.  **Functions as First-Class Objects:** They can be passed as arguments to other functions.
2.  **Nested Functions:** You can define functions inside other functions.
3.  **Returning Functions:** A function can return another function without executing it.

In Flask, decorators are used to connect a URL route to the Python function that should be executed when a user visits that route.

```python
@app.route('/') # This is the decorator
def home(): # This is the function it wraps
    return "Hello, World!"
```

---

### 5. Our First Flask Server
We combined these concepts to create our first minimal Flask application.

**Code (`hello.py`):**
```python
from flask import Flask

# Create a Flask web server application
app = Flask(__name__)

# Define a route for the homepage ('/')
@app.route("/")
def hello_world():
    """This function is triggered when a user visits the homepage."""
    return "Hello, World!"

# A common pattern to run the app directly
if __name__ == "__main__":
    # The run() method starts the development server
    app.run()
```

To run this, we learned to use the terminal to set an environment variable (`export FLASK_APP=hello.py` on Mac/Linux or `set FLASK_APP=hello.py` on Windows) and then execute `flask run`. Alternatively, the `if __name__ == "__main__"` block allows us to run the server simply by executing the Python script directly.
 