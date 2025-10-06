
# Day 77: NumPy - The Foundation of Numerical Computing in Python

Welcome to Day 77! Today marked a fundamental step in my data science journey as I dove into NumPy (Numerical Python), the library that underpins much of the scientific computing ecosystem in Python, including Pandas. This project focused on understanding and utilizing NumPy's core data structure, the `ndarray`, to perform efficient calculations and manipulations.

The main event was a fascinating challenge: manipulating image data directly by treating images as NumPy arrays.

## Table of Contents
- [1. The Power of NumPy's ndarray](#1-the-power-of-numpys-ndarray)
- [2. Array Creation and Manipulation](#2-array-creation-and-manipulation)
- [3. Broadcasting and Linear Algebra](#3-broadcasting-and-linear-algebra)
- [4. Image Manipulation with NumPy](#4-image-manipulation-with-numpy)
- [5. Key Learnings](#5-key-learnings)
- [6. Day 77 Project: Jupyter Notebook Code Summary](#6-day-77-project-jupyter-notebook-code-summary)

---

### 1. The Power of NumPy's ndarray
The central feature of NumPy is the `ndarray` (n-dimensional array). Unlike Python lists, `ndarrays` are:
-   **Fast:** They are implemented in C, making mathematical operations significantly faster.
-   **Memory Efficient:** They store data more compactly.
-   **Convenient:** They allow for vectorized operations, meaning I can perform an operation on the entire array at once without writing a loop.

---

### 2. Array Creation and Manipulation
I learned several ways to create and work with `ndarrays`:
-   **Creation:** From Python lists, using functions like `np.zeros()`, `np.ones()`, `np.random.random()`, and `np.linspace()` to create arrays for various purposes.
-   **Slicing:** I practiced accessing subsets of multi-dimensional arrays using slicing, similar to Python lists but extended to multiple dimensions (e.g., `my_array[0, 1:3]`).
-   **Shape and Reshaping:** I used `.shape` to check the dimensions of an array and `.reshape()` to change its structure without changing its data.

---

### 3. Broadcasting and Linear Algebra
Two powerful concepts I explored were broadcasting and linear algebra.
-   **Broadcasting:** This describes how NumPy handles operations on arrays of different shapes. For example, I can add a single number (a scalar) to every element in a large array in a single operation.
-   **Linear Algebra:** NumPy is the go-to library for linear algebra in Python. I performed matrix multiplication using both `np.matmul()` and the `@` operator, which is crucial for tasks like image processing.

---

### 4. Image Manipulation with NumPy
The most exciting part of the day was working with images. An image is essentially an `ndarray`:
-   A color image is a 3D array: `(height, width, color_channels)`.
-   A grayscale image is a 2D array: `(height, width)`.

I performed several transformations on an image of a cupcake:
-   **Grayscale Conversion:** I converted the color image to grayscale by performing a dot product between the image's RGB channels and a `grey_vals` array containing standard luminance values.
-   **Flipping:** Used `np.flip()` to turn the image upside down.

-   **Rotating:** Used `np.rot90()` to rotate the color image.

-   **Inverting (Solarizing):** I inverted the image colors by subtracting each pixel's value from 255 (`255 - color_img_array`).


---

### 5. Key Learnings
-   NumPy `ndarrays` are the backbone of numerical processing in Python.
-   Broadcasting allows for efficient, vectorized operations.
-   Images are just arrays of numbers and can be manipulated using standard NumPy array operations.
-   Understanding linear algebra concepts like the dot product is practical for tasks like image processing.

---

### 6. Day 76 Project: Jupyter Notebook Code Summary
Here are some key code snippets from the notebook, showcasing image manipulation with NumPy.

```python
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# --- Load Image as NumPy Array ---
img = Image.open('overlook.jpg')
img_array = np.array(img)

# --- Grayscale Conversion ---
# The weights for converting RGB to grayscale
grey_vals = np.array([0.2126, 0.7152, 0.0722])

# Convert image to floats between 0 and 1
sRGB_array = img_array / 255

# Perform dot product to get grayscale values
img_gray = sRGB_array @ grey_vals 
# Alternative: np.matmul(sRGB_array, grey_vals)

plt.imshow(img_gray, cmap='gray')
plt.show()

# --- Image Transformations ---

# Flip image upside down
flipped_img = np.flip(img_gray)
plt.imshow(flipped_img, cmap='gray')
plt.show()

# Rotate the color image
rotated_img = np.rot90(img_array)
plt.imshow(rotated_img)
plt.show()

# Invert/Solarize the color image
inverted_img = 255 - img_array
plt.imshow(inverted_img)
plt.show()
```