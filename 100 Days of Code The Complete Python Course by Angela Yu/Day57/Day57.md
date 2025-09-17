# Day 57: Templating with Jinja

Welcome to Day 57! Today, we explored **Jinja**, the templating engine that comes bundled with Flask. This is a crucial skill that allows us to move from static websites to dynamic web applications by embedding Python logic directly into our HTML files. We learned how to pass data from our server to our templates, use control structures like loops and conditionals, and dynamically generate URLs. The day's project was to build a clean, multi-page blog.


## Table of Contents
- [1. What is Templating?](#1-what-is-templating)
- [2. Passing Variables to Templates](#2-passing-variables-to-templates)
- [3. Using Control Structures in Jinja](#3-using-control-structures-in-jinja)
- [4. URL Building with `url_for()`](#4-url-building-with-url_for)
- [5. Day 57 Project: A Templated Blog](#5-day-57-project-a-templated-blog)

---

### 1. What is Templating?
A templating engine like Jinja lets you create a base HTML structure (a "template") and then insert dynamic data into it. Instead of creating a separate HTML file for every single blog post, you create one `post.html` template and dynamically fill in the title, subtitle, and body content for each post.

Jinja uses special delimiters to distinguish its code from regular HTML:
-   `{{ ... }}`: For **expressions**. Anything inside these double curly braces gets evaluated and printed to the template. Use this for displaying variables or simple statements (e.g., `{{ 5 * 6 }}` would render as `30`).
-   `{% ... %}`: For **statements**. This is used for control structures like `for` loops, `if` statements, and more.

---

### 2. Passing Variables to Templates
To use data from your Python server in your HTML, you pass it as keyword arguments to the `render_template()` function.

In your Python file, you can calculate a value or fetch data, then give it a variable name that Jinja can use.

**`server.py`:**
```python
from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    # The variable 'year' is now available in index.html
    return render_template("index.html", year=current_year)
```

**`templates/index.html`:**
```html
<footer>
    <p>Copyright {{ year }}</p>
</footer>
```
This code dynamically inserts the current year into the footer, so you never have to update it manually again!

---

### 3. Using Control Structures in Jinja
For more complex logic, like displaying a list of items, you can use statement blocks (`{% ... %}`). This is essential for rendering collections of data, like blog posts.

You can loop through a list of posts passed from your server and render HTML for each one.

**`server.py`:**
```python
@app.route('/blog')
def get_blog():
    # all_posts is a list of post objects fetched from an API
    return render_template("blog.html", posts=all_posts)
```

**`templates/blog.html`:**
```html
{% for blog_post in posts %}
    <h1>{{ blog_post.title }}</h1>
    <h2>{{ blog_post.subtitle }}</h2>
{% endfor %}
```
Note that you must explicitly close the statement with `{% endfor %}`. Similarly, an `if` statement must be closed with `{% endif %}`.

---

### 4. URL Building with `url_for()`
Hard-coding URLs in your templates (e.g., `<a href="/post/1">`) is brittle. If you ever change the route in your Python code, you have to manually update it everywhere in your HTML.

Flask provides the `url_for()` function to solve this. It generates a URL for a specific function.

```html
<!-- This link will point to the route handled by the 'show_post' function -->
<a href="{{ url_for('show_post', index=post.id) }}">Read</a>
```
This is much more robust. `url_for()` takes the name of the view function as its first argument and any variable parts of the URL as keyword arguments.

---

### 5. Day 57 Project: A Templated Blog
We combined all these concepts to build a simple but functional blog.

1.  **Data Source:** We used an API from n:point to get a list of blog posts in JSON format. In `main.py`, we fetched this data and created a list of `Post` objects.
2.  **Homepage (`index.html`):**
    * The `/` route fetches all posts from the API.
    * It passes the list of post objects to `index.html`.
    * The template uses a `{% for post in all_posts %}` loop to display the title and subtitle for each post in a card format.
    * Each card has a "Read" link generated with `url_for('show_post', index=post.id)`, which creates a unique URL for each post (e.g., `/post/1`, `/post/2`).
3.  **Post Page (`post.html`):**
    * A dynamic route (`@app.route("/post/<int:index>")`) listens for requests to individual post URLs.
    * It finds the correct post from the list based on the `index` passed from the URL.
    * It passes that single `post` object to the `post.html` template.
    * `post.html` then renders the full `title`, `subtitle`, and `body` of that specific post.

This project effectively demonstrates how to build a dynamic, data-driven website where the content and structure are managed separately.
  