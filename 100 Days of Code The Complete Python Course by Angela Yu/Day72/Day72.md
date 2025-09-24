# Day 72: Data Exploration & Analysis with Pandas

Welcome to Day 72! Today's focus was on data exploration using Pandas, a cornerstone library for data science in Python. I moved from a traditional IDE to a Google Colab notebook to analyze a dataset from PayScale, which contains salary information for various college majors.

The goal was to clean the data, analyze it, and answer questions like which majors have the highest earning potential and which are the lowest-risk from a financial standpoint.

## Table of Contents
- [1. Setting Up in Google Colab](#1-setting-up-in-google-colab)
- [2. Preliminary Data Exploration](#2-preliminary-data-exploration)
- [3. Data Cleaning: Handling Missing Values](#3-data-cleaning-handling-missing-values)
- [4. Answering Key Questions with Pandas](#4-answering-key-questions-with-pandas)
- [5. Sorting Values and Finding the Majors with the Highest Potential](#5-sorting-values-and-finding-the-majors-with-the-highest-potential)
- [6. Grouping and Aggregating Data](#6-grouping-and-aggregating-data)
- [7. Day 72 Project: Jupyter Notebook Code Summary](#7-day-72-project-jupyter-notebook-code-summary)

---

### 1. Setting Up in Google Colab
For data science, notebook environments like Google Colab or Jupyter are preferred over IDEs like PyCharm. They allow for executing code in cells and immediately seeing the output (like tables and charts), which is ideal for exploratory analysis.

The first step was to import the Pandas library and load the `salaries_by_college_major.csv` dataset into a DataFrame.

```python
import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')
```

---

### 2. Preliminary Data Exploration
Once the data was loaded, I used several Pandas methods to get a feel for the dataset:
-   **`.head()`:** To view the first 5 rows of the DataFrame.
-   **`.tail()`:** To view the last 5 rows.
-   **`.shape`:** To find the number of rows and columns.
-   **`.columns`:** To see the names of all columns.
-   **`.isna()`:** To check for missing or non-existent data (`NaN` values).

---

### 3. Data Cleaning: Handling Missing Values
The initial exploration revealed a row with `NaN` values. Missing data can corrupt analysis, so it needs to be handled. For this dataset, I chose to remove the row with the missing data entirely.

```python
# Create a new, clean DataFrame by dropping rows with NaN values.
clean_df = df.dropna()
```

---

### 4. Answering Key Questions with Pandas
With a clean DataFrame, I could start answering questions. I learned how to access specific columns and use methods to find key information.

-   **Highest Starting Salary:** I accessed the 'Starting Median Salary' column, found the maximum value with `.max()`, and then found its row index with `.idxmax()` to identify the corresponding major.

```python
# To find the major with the highest starting salary:
max_salary = clean_df['Starting Median Salary'].max()
major_index = clean_df['Starting Median Salary'].idxmax()
major_name = clean_df['Undergraduate Major'].loc[major_index]
# Result: Physician Assistant
```
I used similar logic to find the majors with the highest mid-career salary and the lowest starting and mid-career salaries.

---

### 5. Sorting Values and Finding the Majors with the Highest Potential
To determine which majors had the highest growth potential, I created a new column called 'Spread'. This column represents the difference between the 90th percentile and 10th percentile mid-career salaries.

-   **Adding a New Column:**
    ```python
    spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
    clean_df.insert(1, 'Spread', spread_col)
    ```
-   **Sorting by a Column:** I then used `.sort_values()` to see which majors had the highest and lowest spreads. A high spread indicates high earning potential but also higher risk.
    ```python
    # To find the majors with the highest potential (largest spread)
    highest_potential = clean_df.sort_values('Spread', ascending=False)
    ```

---

### 6. Grouping and Aggregating Data
A powerful feature of Pandas is the ability to group data. I wanted to compare the average salaries across different degree categories (STEM, HASS, Business).

-   **`.groupby()`:** I used this method to group the DataFrame by the 'Group' column.
-   **`.mean()`:** After grouping, I applied the `.mean()` method to calculate the average of the numeric columns for each group.

```python
# Set display format for floats
pd.options.display.float_format = '{:,.2f}'.format 

# Group by category and calculate the mean
clean_df.groupby('Group').mean()
```
This provided a clean summary table comparing the earning potential across the different fields of study.

---

### 7. Day 72 Project: Jupyter Notebook Code Summary
The entire analysis was performed in a Jupyter Notebook. Here is a summary of the key code used to explore and analyze the salary data.

```python
import pandas as pd

# Load and explore the data
df = pd.read_csv('salaries_by_college_major.csv')
df.head()
df.shape
df.columns
df.isna()

# Clean the data
clean_df = df.dropna()
clean_df.tail()

# Find major with the highest starting salary
highest_start_salary_major = clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmax()]
print(highest_start_salary_major)

# Find major with the highest mid-career salary
highest_mid_career_major = clean_df['Undergraduate Major'].loc[clean_df['Mid-Career Median Salary'].idxmax()]
print(highest_mid_career_major)

# Find major with the lowest starting salary
lowest_start_salary_major = clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]
print(lowest_start_salary_major)

# Calculate and add a 'Spread' column
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)

# Sort by the highest potential and risk
highest_potential = clean_df.sort_values('Spread', ascending=False)
print(highest_potential[['Undergraduate Major', 'Spread']].head())

# Group by degree category and find the average salaries
pd.options.display.float_format = '{:,.2f}'.format
print(clean_df.groupby('Group').mean())
```