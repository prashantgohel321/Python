# Day 41: Introduction to Web Development with HTML

Welcome to my log for Day 41! Today marked a major turning point in my coding journey as I stepped into the world of web development. I learned the fundamental theory behind how the internet works and then dove into writing my very first **HTML** code to build the structure of a webpage. The day's project was to create a simple but well-structured movie ranking page.

## Table of Contents
- [1. How the Internet Works](#1-how-the-internet-works)
- [2. How Websites Work: HTML, CSS & JavaScript](#2-how-websites-work-html-css--javascript)
- [3. Setting Up My Development Environment](#3-setting-up-my-development-environment)
- [4. Introduction to HTML](#4-introduction-to-html)
  - [Heading Elements (`<h1>` to `<h6>`)](#heading-elements-h1-to-h6)
  - [Paragraph Elements (`<p>`)](#paragraph-elements-p)
  - [Void Elements (`<hr />`, `<br />`)](#void-elements-hr---br-)
- [5. Day 41 Project: My Favorite Movies Website](#5-day-41-project-my-favorite-movies-website)

---

### 1. How the Internet Works
I started by demystifying the "cloud." The internet isn't a magical floating entity; it's a physical network of computers connected by massive undersea and underground cables.

-   **Clients and Servers:** My computer is a **client**. When I visit a website, I'm requesting files from a **server**, which is a powerful computer that's online 24/7 to store and "serve" website files.
-   **IP Addresses & DNS:** Every device on the internet has a unique **IP Address** (like a postal code). When I type a domain like `google.com`, my request goes to a **DNS (Domain Name System)** server, which acts like a phonebook, looking up the IP address for that domain so my browser can connect to the right server.


---

### 2. How Websites Work: HTML, CSS & JavaScript
A website is typically made of three types of files, each with a specific job:

-   **HTML (HyperText Markup Language):** The **structure** and content. It's the skeleton of the webpage, defining elements like headings, paragraphs, images, and buttons.
-   **CSS (Cascading Style Sheets):** The **styling**. It controls the visual presentation, including colors, fonts, layout, and spacing. It's the "clothing" and "decoration" for the HTML skeleton.
-   **JavaScript (JS):** The **behavior** and interactivity. It makes the website functional, allowing things like button clicks to trigger actions, animations to run, or data to be fetched.

A website can exist with only HTML, but it can't exist with only CSS or JS.

---

### 3. Setting Up My Development Environment
To start building websites, I set up my local environment:
-   **VS Code:** I installed Visual Studio Code, a professional and highly popular code editor.
-   **Extensions:** I installed essential extensions like **Live Preview** (to see my webpage update in real-time) and **Prettier** (to automatically format my code).
-   **Google Chrome:** I'll be using Chrome for its excellent Developer Tools, which I used to inspect and even temporarily edit the HTML of live websites like TechCrunch.

---

### 4. Introduction to HTML
HTML uses **tags** to define **elements**. An element is usually composed of an opening tag (e.g., `<p>`) and a closing tag (e.g., `</p>`), with the content placed in between.

#### Heading Elements (`<h1>` to `<h6>`)
Headings are used to create a hierarchical structure for the content.
-   `<h1>` is the most important, top-level heading (like a book title). A page should only have one `<h1>`.
-   `<h2>` through `<h6>` represent subheadings of decreasing importance. It's best practice not to skip heading levels (e.g., jumping from an `<h1>` to an `<h3>`).

#### Paragraph Elements (`<p>`)
The `<p>` tag is used to group text into paragraphs. Browsers automatically add space before and after paragraph elements, separating them visually. This is crucial for readability and accessibility.

#### Void Elements (`<hr />`, `<br />`)
Void elements are unique because they are self-closing and do not contain any content.
-   `<hr />` (Horizontal Rule): Creates a thematic break or a horizontal line across the page, useful for separating sections.
-   `<br />` (Line Break): Inserts a single line break. This is useful for formatting content like poems or addresses where line breaks are meaningful but the content should remain within a single paragraph.

---

### 5. Day 41 Project: My Favorite Movies Website
I put all this new knowledge into practice by building a simple, one-page website to list and describe my favorite movies. The project required me to structure the content logically using the HTML elements I learned about today.

-   I used an `<h1>` for the main title of the page.
-   An `<h2>` served as the subtitle.
-   An `<hr />` visually separated the header from the movie list.
-   Each movie title was an `<h3>`.
-   A `<p>` tag followed each movie title to provide a brief description.

This project was a great hands-on introduction to structuring a document with HTML.

Here is the final code for my movie ranking page:

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>My Favorite Movies</title>
</head>
<body>
    <h1>Top Movies of All Time According to Me</h1>
    <h2>My Best 3 Movies</h2>
    <hr />
    <h3>Spirited Away</h3>
    <p>My favorite anime film. The art and story are beautiful.</p>
    
    <h3>Ex Machina</h3>
    <p>A really cool and thought-provoking sci-fi movie.</p>

    <h3>Drive</h3>
    <p>Beautifully shot with an amazing soundtrack.</p>
</body>
</html>
```