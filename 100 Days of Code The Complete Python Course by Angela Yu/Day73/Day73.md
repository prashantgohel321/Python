# Day 73: Visualizing Data with Matplotlib & Pandas

Welcome to Day 73! Today's project was an exciting dive into data visualization. Using a dataset from Stack Overflow, I analyzed the popularity of various programming languages over time. This involved advanced data manipulation with Pandas and creating insightful charts with Matplotlib, one of Python's most popular plotting libraries.

The main goal was to transform raw, tabular data into a compelling visual story about the trends in programming.

## Table of Contents
- [1. Data Exploration and Cleaning](#1-data-exploration-and-cleaning)
- [2. Working with Time-Series Data](#2-working-with-time-series-data)
- [3. Reshaping the DataFrame with `.pivot()`](#3-reshaping-the-dataframe-with-pivot)
- [4. Creating Visualizations with Matplotlib](#4-creating-visualizations-with-matplotlib)
- [5. Smoothing Time-Series Data with `.rolling()`](#5-smoothing-time-series-data-with-rolling)
- [6. Day 73 Project: Jupyter Notebook Code Summary](#6-day-73-project-jupyter-notebook-code-summary)

---

### 1. Data Exploration and Cleaning
The first step was to load the `QueryResults.csv` file into a Pandas DataFrame. I performed an initial analysis to understand its structure.

-   **Initial Checks:** I used `.shape`, `.head()`, and `.count()` to inspect the data's dimensions and check for missing values.
-   **Renaming Columns:** The column names were `m` and `TagName`. I renamed them to `DATE` and `TAG` for clarity using `df.rename()`.
-   **Handling Missing Values:** I identified rows with missing values and filled them using `.fillna(0)`.

---

### 2. Working with Time-Series Data
The 'DATE' column was initially stored as a string. To perform time-based analysis, it needed to be converted to a proper `datetime` object.

-   **`pd.to_datetime()`:** This powerful Pandas function converted the 'DATE' string column into a `datetime` column, which is essential for plotting time-series data correctly.

```python
df.DATE = pd.to_datetime(df.DATE)
```

---

### 3. Reshaping the DataFrame with `.pivot()`
The data was in a "long" format, with each row representing a single observation (a language tag for a given month). To plot multiple lines on the same chart (one for each language), I needed to reshape the data into a "wide" format.

-   **`.pivot(index, columns, values)`:** This function was perfect for the task. I set `DATE` as the new index, `TAG` as the new columns, and the post count as the values. This created a DataFrame where each row is a date and each column is a programming language.

```python
pivoted_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
```

---

### 4. Creating Visualizations with Matplotlib
With the data correctly shaped, I used Matplotlib to create line charts.



-   **Basic Plotting:** I could plot a single language easily: `plt.plot(pivoted_df.index, pivoted_df.python)`.
-   **Styling the Chart:** Matplotlib offers extensive customization. I learned to add a title, labels for the x and y-axes, and adjust the font sizes.
    ```python
    plt.figure(figsize=(16,10)) 
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Number of Posts', fontsize=14)
    plt.ylim(0, 35000)
    ```
-   **Plotting Multiple Lines:** I used a `for` loop to iterate through the columns of my pivoted DataFrame and plot each programming language on the same chart, adding a legend to distinguish them.

---

### 5. Smoothing Time-Series Data with `.rolling()`
The raw monthly data was very noisy, making it difficult to spot long-term trends. To address this, I applied a rolling mean to smooth out the lines.

-   **`.rolling(window).mean()`:** This method calculates the average over a defined "window" of time. For example, a window of 6 would calculate the 6-month moving average. This technique reveals underlying trends more clearly.

```python
# Create a rolling average over 6 months
roll_df = pivoted_df.rolling(window=6).mean()

# Plot the smoothed data
plt.plot(roll_df.index, roll_df['java'], label='java')
plt.plot(roll_df.index, roll_df['python'], label='python')
```

---

### 6. Day 73 Project: Jupyter Notebook Code Summary
Here is a summary of the key Python code used in the Google Colab notebook for this analysis.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
df.rename(columns={'m': 'DATE', 'TagName': 'TAG'}, inplace=True)
df.DATE = pd.to_datetime(df.DATE)
df.fillna(0, inplace=True)

# Pivot the DataFrame
pivoted_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
pivoted_df.fillna(0, inplace=True)

# Plotting with Matplotlib
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in pivoted_df.columns:
    plt.plot(pivoted_df.index, pivoted_df[column], linewidth=2, label=pivoted_df[column].name)

plt.legend(fontsize=16)
plt.show()

# Smoothing the data with a rolling mean
roll_df = pivoted_df.rolling(window=12).mean()

# Plotting the smoothed data
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=3, label=roll_df[column].name)
    
plt.legend(fontsize=16)
plt.show()
```