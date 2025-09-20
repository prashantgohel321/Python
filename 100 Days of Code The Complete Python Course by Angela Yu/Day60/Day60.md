# Day 60: Making the Contact Form Work

Welcome to Day 60! The focus of today was to bring our upgraded blog to life by making the contact form fully functional. This required us to dive into one of the most fundamental concepts of web development: handling data submitted from HTML forms. We learned how to configure a form to send a `POST` request, how to receive and parse that data in Flask, and finally, how to use that data to send an email.


## Table of Contents
- [1. Understanding HTML Forms & HTTP Methods](#1-understanding-html-forms--http-methods)
- [2. Receiving POST Requests in Flask](#2-receiving-post-requests-in-flask)
- [3. Accessing Form Data with the `request` Object](#3-accessing-form-data-with-the-request-object)
- [4. Combining GET and POST Routes](#4-combining-get-and-post-routes)
- [5. Sending an Email with `smtplib`](#5-sending-an-email-with-smtplib)
- [6. Day 60 Project: Functional Blog Contact Form Code](#6-day-60-project-functional-blog-contact-form-code)

---

### 1. Understanding HTML Forms & HTTP Methods
An HTML `<form>` is used to collect user input. To send this data to a server, two key attributes are needed:
-   **`method`**: Specifies the HTTP method to use. `GET` requests append data to the URL (visible to the user), while `POST` requests send the data in the body of the HTTP request (more secure for sensitive information). For a contact form, `POST` is the correct choice.
-   **`action`**: Specifies the URL (the route on our server) where the form data should be sent for processing.

We updated our `contact.html` form to send a `POST` request to our `/contact` route, which we dynamically generated using `url_for('contact')`.

```html
<form action="{{ url_for('contact') }}" method="post">
    <!-- form inputs go here -->
</form>
```

---

### 2. Receiving POST Requests in Flask
By default, Flask routes only respond to `GET` requests. To make a route handle a `POST` request, you must explicitly add it to the `methods` list in the `@app.route()` decorator.

```python
@app.route("/contact", methods=["GET", "POST"])
def contact():
    # Logic to handle both GET and POST will go here
    pass
```

---

### 3. Accessing Form Data with the `request` Object
To get the data that was submitted, Flask provides a global `request` object that must be imported. The form data is stored in the `request.form` dictionary-like object. You can access each piece of data using the `name` attribute of its corresponding `<input>` or `<textarea>` element.

```python
from flask import request

def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    print(f"Received message from {name} ({email}): {message}")
```

---

### 4. Combining GET and POST Routes
It's a common pattern to have a single route handle both displaying a form (`GET`) and processing its submission (`POST`). This is achieved by checking `request.method` inside the view function.

-   If `request.method == "POST"`, we process the form data. After processing, we can re-render the same template but pass a variable to confirm the submission was successful.
-   If the method is `GET`, we simply render the blank form as usual.

We also passed a boolean `msg_sent` to our template. In `contact.html`, we used a Jinja `if` statement to change the `<h1>` text based on this variable, providing instant feedback to the user on the same page.

**`main.py`:**
```python
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        # ... process the data (e.g., send email) ...
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)
```

**`contact.html`:**
```html
<div class="page-heading">
  {% if msg_sent: %}
    <h1>Successfully sent your message</h1>
  {% else: %}
    <h1>Contact Me</h1>
  {% endif %}
  <span class="subheading">Have questions? I have answers.</span>
</div>
```

---

### 5. Sending an Email with `smtplib`
The final step was to put our knowledge from Day 32 into practice. We created a `send_email()` function that uses Python's `smtplib` library. This function takes the name, email, phone number, and message from the form, formats them into a string, and sends an email to the website owner's address. This function is called within the `if request.method == "POST":` block.

---

### 6. Day 60 Project: Functional Blog Contact Form Code
Here is the final `main.py` with the complete logic for handling the contact form.

**`main.py`:**
```python
from flask import Flask, render_template, request
import requests
import smtplib

# --- Constants for Email ---
# NOTE: You should use environment variables for real projects
OWN_EMAIL = "YOUR_EMAIL@gmail.com"
OWN_PASSWORD = "YOUR_APP_PASSWORD"

# --- Fetch Blog Posts ---
posts = requests.get("[https://api.npoint.io/c790b4d5cab58020d391](https://api.npoint.io/c790b4d5cab58020d391)").json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    """Sends an email with the form data."""
    email_message = f"Subject:New Message from Blog\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(from_addr=OWN_EMAIL, to_addrs=OWN_EMAIL, msg=email_message.encode("utf-8"))

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
```