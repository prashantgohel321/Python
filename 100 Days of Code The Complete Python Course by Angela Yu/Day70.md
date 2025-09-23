# Day 70: Git, GitHub, and Version Control Fundamentals

Welcome to Day 70! Today was all about learning Git, the industry-standard version control system. I learned how to track changes in my projects, create save points, revert to previous versions, and collaborate with others using GitHub. This is a foundational skill that moves beyond just writing code to managing it professionally.

## Table of Contents
- [1. What is Version Control?](#1-what-is-version-control)
- [2. Local Repositories: The Basic Workflow](#2-local-repositories-the-basic-workflow)
- [3. Remote Repositories with GitHub](#3-remote-repositories-with-github)
- [4. Ignoring Files with `.gitignore`](#4-ignoring-files-with-gitignore)
- [5. Branching and Merging](#5-branching-and-merging)
- [6. Collaboration: Forks and Pull Requests](#6-collaboration-forks-and-pull-requests)

---

### 1. What is Version Control?
Version control is like having an infinite series of "undo" buttons for an entire project. It allows me to save snapshots (called "commits") of my code at different points in time. If I make a mistake or want to go back to an older version, I can do so easily without manually saving multiple copies of my project folder. Git is the most popular software for managing this process.

---

### 2. Local Repositories: The Basic Workflow
I started by learning how to manage a project locally on my machine. The core workflow consists of three areas: the Working Directory, the Staging Area, and the Local Repository.

-   **Initialize a Repository:** The first step in any new project is to initialize Git.
    ```bash
    git init
    ```
-   **Check Status:** This command is my best friend. It shows which files have been modified, which are being tracked, and what's in the staging area.
    ```bash
    git status
    ```
-   **Staging Files (Add):** Before committing, I need to add files to the "staging area." This lets me choose which changes I want to include in the next commit.
    ```bash
    git add <file_name>   # Add a specific file
    git add .             # Add all modified files in the current directory
    ```
-   **Committing Changes:** A commit is a snapshot of the staged files. Each commit has a unique ID and requires a message describing the changes.
    ```bash
    git commit -m "Your descriptive commit message"
    ```
-   **Viewing History:** I can see the log of all previous commits with `git log`.
-   **Viewing and Reverting Changes:**
    -   `git diff <file_name>`: Shows the differences between the current file and the last committed version.
    -   `git checkout <file_name>`: Discards all changes in the working directory and reverts the file to the last committed version.

---

### 3. Remote Repositories with GitHub
While a local repository is great, GitHub allows me to store my code remotely. This serves as a backup and is essential for collaboration.

-   **Linking to a Remote:** After creating a new repository on GitHub, I link my local repository to it. The remote is conventionally named `origin`.
    ```bash
    git remote add origin <repository_url>
    ```
-   **Pushing Changes:** To upload my local commits to GitHub, I use `git push`.
    ```bash
    git push -u origin main
    ```
    The `-u` flag sets the upstream branch, so in the future, I can simply run `git push`.

---

### 4. Ignoring Files with `.gitignore`
Some files, like secret keys, API credentials, virtual environment folders (`venv/`), and OS-specific files (`.DS_Store`), should never be committed to a public repository. The `.gitignore` file tells Git which files and folders to ignore.

I simply create a file named `.gitignore` in the project's root directory and list the files/folders to ignore, one per line. GitHub provides useful templates for different languages.

---

### 5. Branching and Merging
Branching is one of Git's most powerful features. It allows me to work on new features or bug fixes in isolation without affecting the main codebase.


-   **Creating a Branch:**
    ```bash
    git branch <new_branch_name>
    ```
-   **Switching to a Branch:**
    ```bash
    git checkout <branch_name>
    ```
-   **Merging a Branch:** Once I'm happy with the changes in my feature branch, I switch back to the main branch and merge the feature branch into it.
    ```bash
    git checkout main
    git merge <feature_branch_name>
    ```

---

### 6. Collaboration: Forks and Pull Requests
When I want to contribute to a project that I don't have write access to, I use the fork and pull request model.


1.  **Fork:** I create a personal copy of the repository on my own GitHub account by clicking the "Fork" button.
2.  **Clone:** I `git clone` my forked repository to my local machine.
3.  **Branch & Commit:** I create a new branch, make my changes, and commit them locally.
4.  **Push to Fork:** I `git push` my changes to my forked repository on GitHub.
5.  **Create a Pull Request (PR):** From my forked repository on GitHub, I open a "Pull Request." This is a formal request to the original project owner to review my changes and merge them into their main repository. The project owner can then review the code, suggest changes, and ultimately approve and merge the PR.
  