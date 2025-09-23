# Day 71: Deploying a Flask Application to the Internet

Welcome to Day 71! This was a milestone day where I learned how to take a locally-developed Flask application and deploy it to a live web server. The process involves several steps to prepare the app for a production environment, ensuring it's secure, scalable, and stable.

## Table of Contents
- [1. Preparing for Deployment](#1-preparing-for-deployment)
- [2. Using Environment Variables for Security](#2-using-environment-variables-for-security)
- [3. Setting Up a WSGI Server with Gunicorn](#3-setting-up-a-wsgi-server-with-gunicorn)
- [4. Pushing the Project to GitHub](#4-pushing-the-project-to-github)
- [5. Deploying with a Hosting Provider](#5-deploying-with-a-hosting-provider)
- [6. Upgrading the Database to PostgreSQL](#6-upgrading-the-database-to-postgresql)

---

### 1. Preparing for Deployment
Before deploying, the project needed a few adjustments to make it production-ready.
-   **`.gitignore` File:** I added a `.gitignore` file to the project. This is crucial to prevent sensitive files (like `posts.db`), environment folders (`venv/`), and IDE configuration folders (`.idea/`) from being uploaded to a public GitHub repository.
-   **`requirements.txt`:** I ensured all necessary packages, including `gunicorn` and `psycopg2-binary` (for PostgreSQL), were listed with specific versions in the `requirements.txt` file. This guarantees that the hosting provider installs the exact same dependencies, avoiding version conflicts.

---

### 2. Using Environment Variables for Security
Hard-coding sensitive information like secret keys or database URIs directly into the code is a major security risk. To solve this, I used environment variables.

-   **Implementation:** I imported Python's `os` module and replaced hard-coded strings with `os.environ.get('VARIABLE_NAME')`. This allows the application to get sensitive data from the host server's environment instead of from the source code.

```python
import os

# Example of using an environment variable for the Flask secret key
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

# Example for the database URI, with a fallback for local development
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", "sqlite:///posts.db")
```
I also turned off debug mode (`debug=False`) for the production environment.

---

### 3. Setting Up a WSGI Server with Gunicorn
The Flask development server is not suitable for production. A robust Web Server Gateway Interface (WSGI) server is needed to handle real traffic. I used Gunicorn, a popular choice for Python applications.

-   **Procfile:** I created a file named `Procfile` (with a capital 'P' and no extension) in the root of my project. This file tells the hosting provider how to run the application.

```
web: gunicorn main:app
```
This command instructs the host to start a web process using `gunicorn`, and to find the Flask app object named `app` inside the `main.py` file.

---

### 4. Pushing the Project to GitHub
With the project prepared, I put it under version control using Git and pushed it to a remote repository on GitHub.

1.  **Initialize Git:** `git init` (or via the PyCharm GUI).
2.  **Commit Files:** I added all the project files (except those in `.gitignore`) and made an initial commit.
3.  **Push to GitHub:** I created a new repository on GitHub and pushed my local project to it. The hosting provider will pull the code directly from this repository.

---

### 5. Deploying with a Hosting Provider
I chose Render.com as my hosting provider, which offers a free tier and can deploy directly from GitHub.

-   **Create a Web Service:** I connected my GitHub account to Render and selected my blog's repository.
-   **Configure Settings:** I set the start command to `gunicorn main:app` as defined in the `Procfile`.
-   **Add Environment Variables:** In the Render dashboard, I added the environment variables I defined earlier (e.g., `FLASK_KEY`) so my application could access them securely.


---

### 6. Upgrading the Database to PostgreSQL
SQLite is a file-based database, which is not suitable for most hosting providers because their filesystems are often temporary (ephemeral). This means my SQLite database could be wiped daily.

-   **Create a PostgreSQL Database:** I used Render to create a new, managed PostgreSQL database. This is a production-grade database server.
-   **Get the Database URL:** Render provided an "Internal Database URL" for my new database.
-   **Set the `DB_URI` Environment Variable:** I added the database URL as the value for my `DB_URI` environment variable in Render. I had to modify the URL prefix from `postgres://` to `postgresql://` to make it compatible with SQLAlchemy.

With these steps completed, the application was live! The `psycopg2-binary` package allows SQLAlchemy to communicate with the PostgreSQL database seamlessly, so no code changes were needed to switch from SQLite.
   