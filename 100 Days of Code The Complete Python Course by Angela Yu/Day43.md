# Day 43: Introduction to CSS

Welcome to my log for Day 43! Today, I dove into **CSS (Cascading Style Sheets)**, the language that brings visual design to the web. The key takeaway was understanding the principle of **separation of concerns**: HTML is for the content and structure, while CSS is purely for the styling. I learned the three different ways to apply CSS and practiced using various selectors to target specific elements on a page. The project for the day was to style a color vocabulary website.


## Table of Contents
- [1. What is CSS?](#1-what-is-css)
- [2. Three Ways to Add CSS](#2-three-ways-to-add-css)
  - [Inline CSS](#inline-css)
  - [Internal CSS](#internal-css)
  - [External CSS](#external-css)
- [3. CSS Selectors](#3-css-selectors)
- [4. Day 43 Project: Color Vocabulary Website](#4-day-43-project-color-vocabulary-website)

---

### 1. What is CSS?
CSS stands for **Cascading Style Sheets**. It's a language that allows me to define the visual appearance of HTML elements. Before CSS, styling was done directly in HTML with tags like `<font>` and attributes like `color`, which made the code messy and hard to maintain. CSS was created to separate the styling from the structure, making websites much easier to manage and design.

The "cascading" part refers to the order of priority rules that determine which style applies if multiple styles target the same element.

---

### 2. Three Ways to Add CSS
I learned and practiced the three distinct methods for applying CSS styles to an HTML document.

#### Inline CSS
This method applies styles directly to a single HTML element using the `style` attribute. It's useful for very specific, one-off styling but is generally avoided for larger projects as it mixes style with structure.

```html
<h1 style="color: blue;">This heading is blue</h1>
```

#### Internal CSS
Internal CSS is placed within a `<style>` tag inside the `<head>` section of the HTML file. The styles defined here apply only to that specific HTML page. This is good for single-page websites or unique styles on one page.

```html
<head>
    <style>
        h1 {
            color: red;
        }
    </style>
</head>
```

#### External CSS
This is the most common and recommended method. Styles are written in a separate `.css` file and linked to the HTML document from the `<head>` section. This approach keeps the content and styling completely separate, allowing me to style multiple pages with a single stylesheet.

```html
<!-- index.html -->
<head>
    <link rel="stylesheet" href="styles.css">
</head>

<!-- styles.css -->
h1 {
    color: green;
}
```

---

### 3. CSS Selectors
Selectors are the patterns used to "select" the HTML elements I want to style. I practiced using the five basic types:

-   **Element Selector:** Targets all elements of a specific type (e.g., `p`, `h1`, `img`).
    ```css
    p {
        font-size: 16px;
    }
    ```
-   **Class Selector:** Targets all elements with a specific `class` attribute. It's denoted by a period (`.`) followed by the class name. This is great for applying the same style to multiple, different elements.
    ```css
    .highlight {
        background-color: yellow;
    }
    ```
-   **ID Selector:** Targets a single, unique element with a specific `id` attribute. It's denoted by a hash (`#`) symbol. An ID must be unique per page.
    ```css
    #main-title {
        font-size: 32px;
    }
    ```
-   **Attribute Selector:** Targets elements based on the presence or value of an attribute. For example, selecting all `li` elements with a `value` attribute equal to "4".
    ```css
    li[value="4"] {
        color: blue;
    }
    ```
-   **Universal Selector:** The asterisk (`*`) selects every single element on the page. It's often used for resetting default browser styles.
    ```css
    * {
        text-align: center;
    }
    ```

---

### 4. Day 43 Project: Color Vocabulary Website
The day's project was to apply these CSS concepts to a real webpage. I was given an unstyled HTML file containing a list of colors in Spanish, each with a corresponding image. My task was to:
1.  Create an external `style.css` file and link it correctly.
2.  Use **ID selectors** to change the text color of each color name (e.g., "Rojo") to match its meaning (red).
3.  Use a **class selector** to change the font-weight of all the color titles.
4.  Use an **element selector** to resize all images to a uniform square size (200x200 pixels).

This project was a fantastic hands-on exercise for solidifying my understanding of how CSS selectors work in practice.

Here is the final CSS code for the project:

```css
/* style.css */
#red {
    color: red;
}

#blue {
    color: blue;
}

#orange {
    color: orange;
}

#green {
    color: green;
}

#yellow {
    color: yellow;
}

.color-title {
    font-weight: normal;
}

img {
    height: 200px;
    width: 200px;
}
```