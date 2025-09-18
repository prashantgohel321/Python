# Day 59: Upgrading a Blog with a Bootstrap Template

Welcome to my log for Day 59! Today, we leveraged the power of the web development community by taking our simple blog and giving it a major facelift with a free, professional Bootstrap template called "Clean Blog" from Start Bootstrap. This is a common and efficient workflow: instead of building a complex front-end from scratch, we adapt a pre-existing template to work with our Flask backend.

This project was a fantastic exercise in integrating front-end assets, making a static template dynamic, and organizing code for a multi-page website.


## Table of Contents
- [1. Project Setup: Integrating the Template](#1-project-setup-integrating-the-template)
- [2. Fixing Static File Paths](#2-fixing-static-file-paths)
- [3. Creating Reusable Partials with `{% include %}`](#3-creating-reusable-partials-with-include)
- [4. Rendering Dynamic Blog Content](#4-rendering-dynamic-blog-content)
- [5. Creating Individual Post Pages](#5-creating-individual-post-pages)
- [6. Day 59 Project: Upgraded Blog Code](#6-day-59-project-upgraded-blog-code)

---

### 1. Project Setup: Integrating the Template
The first step was to set up the project and incorporate the downloaded template files.

1.  **Download Template:** I downloaded the "Clean Blog" template from the Start Bootstrap website.
2.  **Create Flask Structure:** In a new PyCharm project, I created the essential Flask folders: `templates` for HTML files and `static` for CSS, JavaScript, and images.
3.  **Organize Files:** I moved the `index.html`, `about.html`, `contact.html`, and `post.html` files into the `templates` folder. The `assets`, `css`, and `js` folders from the template were all moved into my `static` folder.
4.  **Basic Server:** I wrote a minimal `main.py` with a route for the homepage (`/`) that rendered the `index.html` template.

---

### 2. Fixing Static File Paths
When I first ran the server, the website was unstyled because the HTML file couldn't find the CSS and JavaScript files. The original template used relative paths like `css/styles.css`, but Flask serves these from the `static` folder.

The solution was to use Flask's `url_for()` function to generate the correct paths. I went through all the HTML files and updated every link to a static asset.

**Before:**
```html
<link href="css/styles.css" rel="stylesheet" />
```

**After:**
```html
<link href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet" />
```
I did the same for JavaScript files, the favicon, and the background images in the `<header>` style attributes.

---

### 3. Creating Reusable Partials with `{% include %}`
The `index.html`, `about.html`, `contact.html`, and `post.html` files all shared the exact same header (including the navigation bar) and footer code. Repeating this code in every file is inefficient and hard to maintain (a principle known as DRY: Don't Repeat Yourself).

Jinja's `{% include %}` statement solves this perfectly.
1.  **Create Partials:** I created `header.html` and `footer.html` in the `templates` folder.
2.  **Move Code:** I cut the header/navigation code from the top of `index.html` and pasted it into `header.html`. I did the same for the footer code, moving it to `footer.html`.
3.  **Include Partials:** In `index.html`, `about.html`, `contact.html`, and `post.html`, I replaced the removed code with simple include statements.

```html
{% include "header.html" %}

<!-- Main page content goes here -->

{% include "footer.html" %}
```
Now, if I need to change a navigation link, I only have to edit `header.html` once, and the change will appear on every page.

---

### 4. Rendering Dynamic Blog Content
With the template structure in place, the next step was to populate the homepage with actual blog data from our n:point API.

-   **Fetch Data:** In `main.py`, I used the `requests` library to get the JSON data from the API endpoint and stored it in a list called `posts`.
-   **Pass to Template:** This `posts` list was passed to the `index.html` template during rendering: `render_template("index.html", all_posts=posts)`.
-   **Jinja For Loop:** In `index.html`, I used a Jinja `for` loop to iterate through the `all_posts` list and generate the HTML for each post preview dynamically.

```html
{% for post in all_posts %}
<div class="post-preview">
  <a href="{{ url_for('show_post', index=post.id) }}">
    <h2 class="post-title">{{ post.title }}</h2>
    <h3 class="post-subtitle">{{ post.subtitle }}</h3>
  </a>
  <p class="post-meta">
    Posted by {{ post.author }} on {{ post.date }}
  </p>
</div>
<hr class="my-4" />
{% endfor %}
```

---

### 5. Creating Individual Post Pages
The final piece of functionality was to make each post preview clickable, leading to a full page for that post.

-   **Dynamic Route:** I created a dynamic route in `main.py`: `@app.route("/post/<int:index>")`. This route accepts an integer (the post's ID) from the URL.
-   **View Function:** The `show_post(index)` function loops through the `posts` list to find the dictionary with the matching `id`.
-   **Render Post:** It then passes that single `post` object to the `post.html` template.
-   **Template Update:** The `post.html` template was updated to use the variables from the passed-in `post` object (e.g., `{{ post.title }}`, `{{ post.body }}`). The header's background image was also made dynamic using `{{ post.image_url }}`.

---

### 6. Day 59 Project: Upgraded Blog Code
Here is the final Python code that powers the blog.

**`main.py`:**
```python
from flask import Flask, render_template
import requests

# The API endpoint for the blog posts
posts = requests.get("[https://api.npoint.io/c790b4d5cab58020d391](https://api.npoint.io/c790b4d5cab58020d391)").json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    """Renders the homepage with all post previews."""
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    """Renders the about page."""
    return render_template("about.html")

@app.route("/contact")
def contact():
    """Renders the contact page."""
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    """Renders a single post page based on the post's ID."""
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
```