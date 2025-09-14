# Day 42: Intermediate HTML - Structure, Lists, and Links

Welcome to my log for Day 42! Today, I built upon the basics of HTML by learning the proper structure of a web page, known as the **HTML Boilerplate**. I also explored how to organize content with ordered and unordered lists, and how to make my pages interactive with hyperlinks and images. The day's project was to combine all these new skills to create a fun birthday invitation website.


## Table of Contents
- [1. The HTML Boilerplate](#1-the-html-boilerplate)
- [2. Nesting and Indentation](#2-nesting-and-indentation)
- [3. List Elements](#3-list-elements)
  - [Unordered Lists (`<ul>`)](#unordered-lists-ul)
  - [Ordered Lists (`<ol>`)](#ordered-lists-ol)
- [4. The Anchor Element (`<a>`): Creating Links](#4-the-anchor-element-a-creating-links)
- [5. The Image Element (`<img>`): Displaying Images](#5-the-image-element-img-displaying-images)
- [6. Day 42 Project: Birthday Invite Website](#6-day-42-project-birthday-invite-website)

---

### 1. The HTML Boilerplate
Every proper HTML document follows a standard structure. This "boilerplate" code tells the browser how to interpret and render the page correctly.

-   `<!DOCTYPE html>`: The very first line, which declares the document type and tells the browser it's an HTML5 document.
-   `<html>`: The root element that wraps all other content. The `lang="en"` attribute specifies the page language, which is important for accessibility.
-   `<head>`: This section contains meta-information about the page that isn't displayed to the user.
    -   `<meta charset="UTF-8">`: Specifies the character encoding to ensure all text (including symbols and emojis) displays correctly.
    -   `<title>`: Sets the text that appears in the browser tab.
-   `<body>`: This is where all the visible content of the webpage goes—headings, paragraphs, images, links, etc.

Here’s the complete boilerplate structure:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Website</title>
</head>
<body>
    <h1>My Content Goes Here</h1>
</body>
</html>
```
In VS Code, I learned I can generate this instantly by typing `!` and pressing Enter.

---

### 2. Nesting and Indentation
HTML elements are often placed inside one another, a concept called **nesting**. For example, the `<head>` and `<body>` elements are nested inside the `<html>` element. To keep the code readable and understand these relationships, proper **indentation** is essential. It visually shows the hierarchical structure of the page.

---

### 3. List Elements
Lists are fundamental for organizing content.

#### Unordered Lists (`<ul>`)
I use an unordered list when the sequence of items doesn't matter, like a shopping list. Each item is defined with a `<li>` (list item) tag, and browsers render them with bullet points.

```html
<ul>
    <li>Milk</li>
    <li>Cheese</li>
    <li>Bread</li>
</ul>
```

#### Ordered Lists (`<ol>`)
When the sequence is important, like in a recipe's instructions, I use an ordered list. Browsers automatically number the `<li>` items.

```html
<ol>
    <li>Mix flour and eggs.</li>
    <li>Pour into a baking pan.</li>
    <li>Bake for 30 minutes.</li>
</ol>
```
I also learned that lists can be nested inside other list items to create complex, multi-level outlines.

---

### 4. The Anchor Element (`<a>`): Creating Links
The anchor element is what makes the web "hypertext." It creates a clickable link to another page or resource.

-   **The `href` Attribute:** This is the most critical part. `href` stands for "hypertext reference" and its value is the URL that the link will navigate to. Without an `href`, the text will appear but won't be a functional link.

```html
<a href="[https://www.google.com](https://www.google.com)">Go to Google</a>
```

---

### 5. The Image Element (`<img>`): Displaying Images
To display images, I use the `<img>` tag. It's a **void element**, meaning it's self-closing and doesn't have a closing tag because it doesn't contain text content.

-   **The `src` Attribute:** The "source" attribute points to the image file's URL or local path.
-   **The `alt` Attribute:** The "alternative text" is crucial for accessibility. It provides a description of the image for screen readers used by visually impaired users and is also displayed if the image fails to load.

```html
<img src="puppy.jpg" alt="A cute puppy playing in the sand." />
```

---

### 6. Day 42 Project: Birthday Invite Website
The final project of the day was to create a birthday invitation webpage. This was a great exercise to combine all the elements I learned:
-   I used `<h1>` and `<h2>` tags for the main invitation text.
-   An `<img>` tag displayed a birthday cake image.
-   A `<ul>` with `<li>` elements listed what guests should bring.
-   An `<a>` tag provided a Google Maps link to the party location.

Here is the final code for my birthday invite project:

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Birthday Invite!</title>
</head>
<body>
    <h1>It's My Birthday!</h1>
    <h2>On the 12th May</h2>

    <img src="[https://raw.githubusercontent.com/appbrewery/webdev/main/birthday-cake3.4.jpeg](https://raw.githubusercontent.com/appbrewery/webdev/main/birthday-cake3.4.jpeg)" alt="A purple birthday cake with candles" />

    <h3>What to bring:</h3>
    <ul>
        <li>Balloons (I love balloons)</li>
        <li>Cake (I'm really good at eating)</li>
        <li>An appetite (There will be lots of food)</li>
    </ul>

    <h3>This is where you need to go:</h3>
    <a href="[https://www.google.com/maps/place/The+Pigeon+People/@35.672851,139.712613,17z/data=!4m14!1m7!3m6!1s0x60188c9a00539b2d:0x893521990c34515!2sThe+Pigeon+People!8m2!3d35.672851!4d139.7151879!16s%2Fg%2F11sb3m6x_2!3m5!1s0x60188c9a00539b2d:0x893521990c34515!8m2!3d35.672851!4d139.7151879!16s%2Fg%2F11sb3m6x_2?entry=ttu](https://www.google.com/maps/place/The+Pigeon+People/@35.672851,139.712613,17z/data=!4m14!1m7!3m6!1s0x60188c9a00539b2d:0x893521990c34515!2sThe+Pigeon+People!8m2!3d35.672851!4d139.7151879!16s%2Fg%2F11sb3m6x_2!3m5!1s0x60188c9a00539b2d:0x893521990c34515!8m2!3d35.672851!4d139.7151879!16s%2Fg%2F11sb3m6x_2?entry=ttu)">
        Google Map Link
    </a>
</body>
</html>
```