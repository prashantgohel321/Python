# Day 44: Intermediate CSS - The Box Model & Typography

Welcome to my log for Day 44! Today's focus was on the core principles of CSS that control the layout and appearance of every element on a webpage. I dove deep into the **CSS Box Model** to understand spacing and sizing, and explored various **font and text properties** to control typography. The final project was a creative exercise in building a motivational poster website, which required me to apply all of these new styling techniques.

## Table of Contents
- [1. CSS Color Properties](#1-css-color-properties)
- [2. Font & Text Styling](#2-font--text-styling)
- [3. The CSS Box Model](#3-the-css-box-model)
- [4. The `<div>` Element](#4-the-div-element)
- [5. Day 44 Project: Motivational Poster Website](#5-day-44-project-motivational-poster-website)

---

### 1. CSS Color Properties
I revisited CSS colors, learning the difference between `color` (for text) and `background-color`. I practiced using both **named colors** (e.g., `red`, `antiquewhite`) and **hexadecimal (hex) codes** (e.g., `#FFFFFF`), which I sourced from design tools like Color Hunt to create professional-looking color palettes.

```css
body {
    background-color: #FDF6F0; /* A light beige hex color */
}

h1 {
    color: darkslateblue; /* A named color */
}
```

---

### 2. Font & Text Styling
I explored several properties to control the appearance of text:

-   **`font-size`**: I learned about different units for sizing text:
    -   **Absolute units:** `px` (pixels) and `pt` (points).
    -   **Relative units:** `em` (relative to the parent element's font size) and `rem` (relative to the root `<html>` element's font size). Using `rem` is best practice for creating scalable and consistent designs.
-   **`font-weight`**: This property controls the thickness of the text. I can use keywords like `normal` and `bold`, or numeric values from 100 to 900.
-   **`font-family`**: This sets the typeface. I learned how to use web fonts from services like **Google Fonts** by linking them in my HTML `<head>`. It's crucial to provide fallback generic font families (like `sans-serif` or `serif`) in case the primary font fails to load.
-   **`text-align`**: Used to align text horizontally within its container (`left`, `right`, `center`).

---

### 3. The CSS Box Model
This was the most crucial concept of the day. Every HTML element can be thought of as a rectangular box with several layers that control its size and spacing relative to other elements.


-   **Content:** The actual text, image, or other content of the element, defined by `width` and `height`.
-   **Padding:** The transparent space between the content and the border. It increases the overall size of the box from the inside.
-   **Border:** A line that goes around the padding and content. Its style, width, and color can be customized.
-   **Margin:** The transparent space *outside* the border. It's used to create space between an element and its neighbors.

I practiced using the Chrome Developer Tools to inspect and modify the box model of live elements, which is an essential skill for debugging layouts.

---

### 4. The `<div>` Element
The `<div>` (content division element) is an invisible container used to group other HTML elements. It has no visual appearance on its own but is incredibly powerful when combined with CSS. By grouping elements into `divs`, I can:
-   Apply a common style (like a background color or border) to an entire section.
-   Use the box model properties (`margin`, `padding`) on the `div` to position a whole group of elements on the page.

---

### 5. Day 44 Project: Motivational Poster Website
The final project was to build a motivational poster website, styled to look like the classic inspirational memes. This required me to apply all the day's concepts:

1.  **Grouping with `<div>`**: I wrapped the image, `<h1>`, and `<p>` elements in a single `div` with a class of `poster`.
2.  **Centering with the Box Model**: I centered the `poster` div horizontally by setting its `width` to `50%` and its `margin-left` to `25%`. This was a clever trick to achieve centering without more advanced layout techniques.
3.  **Custom Fonts**: I imported the "Libre Baskerville" font from Google Fonts to style the heading.
4.  **Styling Elements**:
    -   I set a `background-color` on the `<body>`.
    -   I styled the `<h1>` and `<p>` with specific colors and `text-align: center`.
    -   I used the `text-transform: uppercase` property on the `<h1>` to make it all caps via CSS.
    -   The `<img>` was given a white `border` and its `width` was set to `100%` to ensure it filled the entire width of its parent `div`.

Here is the final code for the project:

**HTML (`index.html`):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Motivational Poster</title>
  <link rel="stylesheet" href="./style.css" />
  <link rel="preconnect" href="[https://fonts.googleapis.com](https://fonts.googleapis.com)">
  <link rel="preconnect" href="[https://fonts.gstatic.com](https://fonts.gstatic.com)" crossorigin>
  <link href="[https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap](https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap)" rel="stylesheet">
</head>
<body>
  <div class="poster">
    <img class="motivation-img" src="./assets/images/daenerys.jpeg" alt="Daenerys Targaryen holding a dragon egg">
    <h1>That Special Moment</h1>
    <p>When you find the perfect avocado at the supermarket</p>
  </div>
</body>
</html>
```

**CSS (`style.css`):**
```css
body {
  background-color: black;
}

.poster {
  width: 50%;
  margin-left: 25%;
  margin-top: 100px;
  color: white;
  font-family: "Libre Baskerville", serif;
  text-align: center;
}

.motivation-img {
  border: 5px solid white;
  width: 100%;
}

h1 {
  text-transform: uppercase;
  font-size: 3rem;
}
```