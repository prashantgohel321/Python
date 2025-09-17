# Day 56: Rendering HTML Templates and Serving Static Files

Welcome to Day 56! Today, we took a major step forward in building professional-looking websites with Flask. We moved away from returning simple HTML strings and learned how to render complete, separate HTML files. We also covered the crucial topic of serving **static files**—like CSS stylesheets, images, and JavaScript—which are essential for any modern website. The final project was to take a free, professionally designed HTML5 template and customize it into a personal digital name card.

## Table of Contents
- [1. Rendering HTML Files with `render_template`](#1-rendering-html-files-with-render_template)
- [2. Serving Static Files (CSS, Images, JS)](#2-serving-static-files-css-images-js)
- [3. Browser Caching and Hard Reloads](#3-browser-caching-and-hard-reloads)
- [4. Final Project: Customizing an HTML5 Template](#4-final-project-customizing-an-html5-template)
- [5. Day 56 Project: Digital Name Card Code](#5-day-56-project-digital-name-card-code)

---

### 1. Rendering HTML Files with `render_template`
Writing an entire website as a single Python string is impractical. Flask provides a much better way to manage HTML using the `render_template()` function.

-   **The `templates` Folder:** Flask has a strict rule: it looks for HTML files in a folder named `templates` in the root of your project directory. All your `.html` files must go here.
-   **Using `render_template`:** To use it, you first import it from the `flask` module. Then, in your view function, you return `render_template("filename.html")` instead of a string.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This will find and render index.html from the 'templates' folder.
    return render_template("index.html")
```
This separation of concerns (Python logic in `.py` files, HTML structure in `.html` files) is a fundamental concept in web development.

---

### 2. Serving Static Files (CSS, Images, JS)
Websites are more than just HTML. They need CSS for styling, images for visuals, and often JavaScript for interactivity. These are called **static files** because they don't change.

-   **The `static` Folder:** Just like with templates, Flask has a convention for static files. They must be placed in a folder named `static` in the root of your project.
-   **Linking to Static Files:** In your HTML file, you reference these files with a path that starts from the `static` folder.

For example, if you have `style.css` in a `css` subfolder inside `static`, you would link to it in your HTML like this:

```html
<link rel="stylesheet" href="static/css/style.css">
```

And for an image:

```html
<img src="static/images/my_photo.png">
```
Flask automatically knows to serve any file requested from the `/static/...` URL path.

---

### 3. Browser Caching and Hard Reloads
A common "gotcha" during development is that browsers **cache** static files. This means that after you visit a site, your browser saves a copy of the CSS and images to speed up future visits.

If you change a static file (e.g., update your CSS), simply refreshing the page might not show your changes because the browser is still using the old, cached version. To fix this, you need to perform a **hard reload** (usually `Cmd+Shift+R` on Mac or `Ctrl+Shift+R` on Windows), which forces the browser to ignore the cache and download fresh copies of all files.

---

### 4. Final Project: Customizing an HTML5 Template
The day's main project was to apply these concepts to a real-world scenario.
1.  **Download a Template:** We downloaded a free, responsive HTML5 template ("Identity" from html5up.net).
2.  **Organize Files:** We created the `templates` and `static` folders in our Flask project and moved the downloaded files into the correct locations (`index.html` into `templates`, and all CSS, JS, and image folders into `static`).
3.  **Update Paths:** We went through the `index.html` file and updated all the links and image sources to include the `static/` prefix (e.g., changing `assets/css/main.css` to `static/assets/css/main.css`).
4.  **Serve with Flask:** We created a simple `server.py` to render the `index.html` file.
5.  **Customize:** We then personalized the website by changing the text, replacing the avatar and background images, and updating the social media links.

This process demonstrates how quickly you can build a beautiful, functional website by integrating a pre-made frontend template with a Python backend.

---

### 5. Day 56 Project: Digital Name Card Code
Here is the final structure and code for the digital name card project.

**Project Structure:**
```
/name-card-project
|-- /static
|   |-- /assets
|   |   |-- /css
|   |   |-- /js
|   |-- /images
|       |-- my_avatar.png
|       |-- bg.jpg
|-- /templates
|   |-- index.html
|-- server.py
```

**`server.py`:**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the main page of the digital name card."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
```

**`templates/index.html` (Snippet showing path updates):**
```html
<!DOCTYPE HTML>
<html>
	<head>
		<title>Angela Yu</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!-- Note the updated path to include 'static' -->
		<link rel="stylesheet" href="static/assets/css/main.css" />
	</head>
	<body class="is-loading">
		<!-- Wrapper -->
			<div id="wrapper">
				<!-- Main -->
					<section id="main">
						<header>
							<!-- And here for the image -->
							<span class="avatar"><img src="static/images/my_avatar.png" alt="" /></span>
							<h1>Angela Yu</h1>
							<p>Programmer & Teacher</p>
						</header>
						<footer>
							<ul class="icons">
								<li><a href="#" class="fa-twitter">Twitter</a></li>
								<li><a href="#" class="fa-instagram">Instagram</a></li>
								<li><a href="#" class="fa-facebook">Facebook</a></li>
							</ul>
						</footer>
					</section>
				<!-- ... rest of the file ... -->
			</div>
	</body>
</html>
```