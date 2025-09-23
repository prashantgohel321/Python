# Day 69: Integrating Users, Comments, and Relational Databases

Welcome to Day 69! Today, I combined the authentication knowledge from Day 68 with the blog project from Day 67. The goal was to build a full-featured blog where users can register, log in, and interact by commenting on posts.

This was a major step that involved restructuring the database to handle relationships between different data models, protecting administrative routes, and enhancing the user interface to reflect a user's logged-in status.

## Table of Contents
- [1. Adding User Registration and Login](#1-adding-user-registration-and-login)
- [2. Creating Database Relationships](#2-creating-database-relationships)
- [3. Restricting Access with an Admin Decorator](#3-restricting-access-with-an-admin-decorator)
- [4. Implementing the Comments Feature](#4-implementing-the-comments-feature)
- [5. Adding Gravatar Profile Images](#5-adding-gravatar-profile-images)
- [6. Day 69 Project: Final Code](#6-day-69-project-final-code)

---

### 1. Adding User Registration and Login
I started by adding the user authentication system to the blog.
-   **Forms:** I created `RegisterForm` and `LoginForm` in a separate `forms.py` file to keep my code organized.
-   **User Table:** A new `User` table was created in the `blog.db` database to store user information, including their hashed and salted passwords.
-   **Routes:** I implemented the `/register` and `/login` routes. The register route now checks if an email already exists to prevent duplicate accounts and provides a flash message. The login route verifies credentials and manages user sessions with Flask-Login.

---

### 2. Creating Database Relationships
This was the most significant part of the day. To link users to their posts and comments, I established relationships in the database using SQLAlchemy.

-   **One-to-Many Relationship:** I defined a one-to-many relationship between the `User` (parent) and `BlogPost` (child) tables. This means one user can be the author of many blog posts.
-   **Introducing Comments:** I created a new `Comment` table. This table has two "many-to-one" relationships:
    1.  Many comments can belong to one `User` (the author of the comment).
    2.  Many comments can belong to one `BlogPost`.
-   **Implementation:** This was achieved using `db.relationship()` and `db.ForeignKey` to link the tables together. Because this changed the database schema, I had to delete the old `blog.db` file and recreate it from scratch.

```python
# In User Model
posts = relationship("BlogPost", back_populates="author")
comments = relationship("Comment", back_populates="comment_author")

# In BlogPost Model
author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
author = relationship("User", back_populates="posts")
comments = relationship("Comment", back_populates="parent_post")

# In new Comment Model
author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
comment_author = relationship("User", back_populates="comments")
post_id: Mapped[str] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
parent_post = relationship("BlogPost", back_populates="comments")
```

---

### 3. Restricting Access with an Admin Decorator
To ensure only the site administrator (the first registered user, with `id=1`) can create, edit, or delete posts, I built a custom decorator.

-   **`@admin_only` Decorator:** I wrote a decorator function that checks if `current_user.id` is `1`. If not, it aborts the request with a `403 Forbidden` error.
-   **Protecting Routes:** I applied this `@admin_only` decorator to the `/new-post`, `/edit-post`, and `/delete` routes to secure them. I also updated the Jinja templates to hide the buttons for these actions from non-admin users.

---

### 4. Implementing the Comments Feature
With the database relationships in place, I added the ability for logged-in users to comment.
-   **Comment Form:** I created a simple `CommentForm` with a `CKEditorField`.
-   **Post Route Logic:** In the `/post/<int:post_id>` route, I added logic to process the `comment_form`. It first checks if the `current_user` is authenticated. If not, it flashes a message and redirects to the login page.
-   **Saving Comments:** If the user is logged in, a new `Comment` object is created, linking it to the `current_user` and the `requested_post`. The comment is then saved to the database.
-   **Displaying Comments:** I looped through `post.comments` in the `post.html` template to display all comments associated with that post.

---

### 5. Adding Gravatar Profile Images
To make the comments section more personal, I used the `flask-gravatar` library to automatically fetch profile images for commenters based on their email address. This was a simple integration that involved initializing the `Gravatar` extension and applying a filter to the user's email in the template.

```html
<!-- In post.html, inside the comments loop -->
<img src="{{ comment.comment_author.email | gravatar }}" />
```

---

### 6. Day 69 Project: Final Code
Here is the final `main.py` code, which brings together a fully-functional blog with user accounts, admin controls, and a comment system.

```python
from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# For adding profile images to the comment section
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    comments = relationship("Comment", back_populates="parent_post")


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")


class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    post_id: Mapped[str] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")


with app.app_context():
    db.create_all()


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("get_all_posts"))
    return render_template("register.html", form=form, current_user=current_user)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=form, current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, current_user=current_user)


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=comment_form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
    return render_template("post.html", post=requested_post, current_user=current_user, form=comment_form)


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, current_user=current_user)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
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
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@app.route("/contact")
def contact():
    return render_template("contact.html", current_user=current_user)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
```