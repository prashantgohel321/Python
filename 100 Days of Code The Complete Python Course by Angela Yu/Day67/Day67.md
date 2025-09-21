# Day 67: Full CRUD Functionality with a RESTful Blog

Welcome to Day 67! Today, I elevated my blog project from a read-only site to a dynamic, fully-featured Content Management System (CMS). I implemented the complete set of CRUD (Create, Read, Update, Delete) operations, allowing posts to be managed directly through the web interface.

This project integrates Flask-SQLAlchemy for database interactions, Flask-WTF for form handling, and Flask-CKEditor for a rich text editing experience.

## Table of Contents
- [1. Project Setup: From JSON to SQLite](#1-project-setup-from-json-to-sqlite)
- [2. Reading Posts (GET Requests)](#2-reading-posts-get-requests)
- [3. Creating New Posts (POST Requests)](#3-creating-new-posts-post-requests)
- [4. Editing Existing Posts (POST/PATCH)](#4-editing-existing-posts-postpatch)
- [5. Deleting Posts (DELETE)](#5-deleting-posts-delete)
- [6. Day 67 Project: Final Code](#6-day-67-project-final-code)

---

### 1. Project Setup: From JSON to SQLite
I moved my data persistence from a simple JSON file to a more robust SQLite database. This was managed using Flask-SQLAlchemy, which allows me to define my database schema using Python classes.

The `BlogPost` model was configured as my table, defining all the necessary columns for a blog post, such as `title`, `subtitle`, `body`, and `author`.

```python
# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
```

---

### 2. Reading Posts (GET Requests)
The "Read" part of CRUD was implemented with two routes:
-   `@app.route('/')`: This route queries the database for all `BlogPost` entries, which are then passed to the `index.html` template to be displayed on the homepage.
-   `@app.route('/post/<int:post_id>')`: This dynamic route retrieves a single blog post from the database using its unique `id`. Flask-SQLAlchemy's `db.get_or_404()` is a convenient way to fetch the record or return a 404 error if it doesn't exist.

---

### 3. Creating New Posts (POST Requests)
I added a `/new-post` route that handles both `GET` (to display the form) and `POST` (to submit the new post) requests.

-   **WTForm with CKEditor:** I created a `CreatePostForm` using Flask-WTF. A key feature is the use of `CKEditorField`, which replaces a standard `<textarea>` with a powerful rich text editor, allowing for formatted blog content.
-   **Data Submission:** When the form is submitted (`form.validate_on_submit()`), a new `BlogPost` object is created using the data from the form. The current date is automatically generated and formatted. The new post is then added to the database session and committed. Finally, the user is redirected to the homepage to see their new post.

---

### 4. Editing Existing Posts (POST/PATCH)
To allow users to update posts, I implemented an `/edit-post/<int:post_id>` route.

-   **Pre-populating the Form:** When a user navigates to the edit page, the route first fetches the corresponding `BlogPost` from the database. The `CreatePostForm` is then instantiated with the existing data from the post object, pre-filling all the fields for the user.
-   **Updating the Record:** When the user submits the edited form, the application finds the existing post in the database and updates its attributes (`title`, `body`, etc.) with the new data from the form. The changes are then committed with `db.session.commit()`. The user is redirected to the updated post page.
-   **Note on HTTP Methods:** While updating a resource should ideally use a `PUT` or `PATCH` request, standard HTML forms only support `GET` and `POST`. Therefore, I handled the update logic within a `POST` request.

---

### 5. Deleting Posts (DELETE)
The final piece of CRUD functionality is deleting posts.

-   A new route, `/delete/<int:post_id>`, was created.
-   On the homepage (`index.html`), a delete link (using an '✘' symbol) was added next to each post.
-   When clicked, this link makes a `GET` request to the delete route. The route finds the post by its ID, removes it from the database session using `db.session.delete(post_to_delete)`, and commits the change. The user is then redirected back to the homepage.

---

### 6. Day 67 Project: Final Code
Here is the complete `main.py` code for the fully functional blog application.

```python
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=form.author.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, is_edit=False)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)

```