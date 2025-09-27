# Day 74: LEGO Dataset Analysis with Pandas & Matplotlib

Welcome to Day 74! Today's project was a deep dive into a real-world dataset from Rebrickable, all about LEGO. This wasn't just a single file, but a relational database split into multiple CSVs. The challenge was to combine these files to answer interesting questions about LEGO's history, from its most popular themes to the complexity of its sets over the years.

## Table of Contents
- [1. Understanding the Relational Data](#1-understanding-the-relational-data)
- [2. Exploring Individual Datasets](#2-exploring-individual-datasets)
- [3. Merging DataFrames with `.merge()`](#3-merging-dataframes-with-merge)
- [4. Analysis: LEGO Sets & Themes Over Time](#4-analysis-lego-sets--themes-over-time)
- [5. Advanced Visualizations in Matplotlib](#5-advanced-visualizations-in-matplotlib)
- [6. Day 74 Project: Jupyter Notebook Code Summary](#6-day-74-project-jupyter-notebook-code-summary)

---

### 1. Understanding the Relational Data
The dataset was split into three main files: `colors.csv`, `sets.csv`, and `themes.csv`. These files are linked together like tables in a database.
-   **`sets.csv`:** Contains information about individual LEGO sets, including a `theme_id`.
-   **`themes.csv`:** Contains the names of the themes, linked by an `id` column.
-   **Foreign Keys:** The `theme_id` in `sets.csv` is a "foreign key" that corresponds to the `id` (the "primary key") in `themes.csv`. Understanding this relationship is key to combining the data.

---

### 2. Exploring Individual Datasets
I started by loading each CSV into its own Pandas DataFrame and performing initial exploration.

-   **`colors.csv`:** I used `.nunique()` to find out how many unique colors are in the LEGO palette.
-   **`sets.csv`:** I used `.sort_values()` to find the year the first LEGO sets were released and which set had the most parts. I also used `.groupby()` to count the number of sets released per year.

---

### 3. Merging DataFrames with `.merge()`
To find out which theme names corresponded to the `theme_id` in the `sets` data, I needed to merge the DataFrames. The `.merge()` function in Pandas is perfect for this, acting like a JOIN in SQL.

-   First, I aggregated the `sets` data to count how many sets belong to each `theme_id`.
-   Then, I merged this aggregated data with the `themes` DataFrame on the `id`/`theme_id` columns.

```python
# Count number of sets per theme
set_theme_count = sets_df["theme_id"].value_counts()
set_theme_count_df = pd.DataFrame({'id': set_theme_count.index, 
                                 'set_count': set_theme_count.values})

# Merge with the themes DataFrame to get theme names
merged_df = pd.merge(set_theme_count_df, themes_df, on='id')
```

---

### 4. Analysis: LEGO Sets & Themes Over Time
With the merged data, I could perform more complex analysis.
-   **Most Popular Themes:** By looking at the `merged_df`, I could easily identify the theme with the highest `set_count`.
-   **Annual Trends:** I grouped the `sets` data by year and used `.agg()` to calculate both the number of new themes and new sets released each year.

---

### 5. Advanced Visualizations in Matplotlib
This project required more than just simple plots.

-   **Bar Chart:** I created a bar chart to visualize the top 10 LEGO themes by the number of sets.


-   **Scatter Plot:** A scatter plot helped me investigate the relationship between the year a set was released and the number of parts it contained, showing how set complexity has evolved.


-   **Line Chart with Two Y-Axes:** To compare the number of sets and themes released each year on the same chart (which have very different scales), I used Matplotlib's `twinx()` method to create a second y-axis.

---

### 6. Day 74 Project: Jupyter Notebook Code Summary
The following is a summary of the key code used in the notebook to perform the LEGO analysis.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
colors_df = pd.read_csv('colors.csv')
sets_df = pd.read_csv('sets.csv')
themes_df = pd.read_csv('themes.csv')

# --- Analysis ---

# Number of unique colors
num_colors = colors_df['name'].nunique()

# Number of sets per theme
set_theme_count = sets_df["theme_id"].value_counts()
set_theme_count_df = pd.DataFrame({'id': set_theme_count.index, 
                                 'set_count': set_theme_count.values})

# Merge sets and themes
merged_df = pd.merge(set_theme_count_df, themes_df, on='id')

# --- Visualizations ---

# Bar chart of top themes
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.show()

# Line chart with two y-axes
themes_by_year = sets_df.groupby('year').agg({'theme_id': pd.Series.nunique})
sets_by_year = sets_df.groupby('year').agg({'set_num': pd.Series.nunique})

ax1 = plt.gca() # get current axes
ax2 = ax1.twinx() 
ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
ax2.plot(themes_by_year.index[:-2], themes_by_year.theme_id[:-2], color='b')

ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='green')
ax2.set_ylabel('Number of Themes', color='blue')
plt.show()

```