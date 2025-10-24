# Day 79: In-Depth Analysis of Nobel Prize Winners

Welcome to Day 79! This project was a capstone challenge, bringing together many of the data science skills I've learned to analyze a rich dataset on Nobel Prize laureates from 1901 to 2020. The goal was to explore the data to answer questions about the winners' demographics, the most awarded countries, and trends over time.

This analysis involved significant data wrangling and the use of advanced visualization techniques with Plotly and Seaborn to tell a compelling story with the data.

## Table of Contents
- [1. Data Exploration and Cleaning](#1-data-exploration-and-cleaning)
- [2. Top Countries and Prize Categories](#2-top-countries-and-prize-categories)
- [3. Visualizing Global Distribution with a Choropleth Map](#3-visualizing-global-distribution-with-a-choropleth-map)
- [4. Uncovering Demographic Patterns with a Sunburst Chart](#4-uncovering-demographic-patterns-with-a-sunburst-chart)
- [5. Analyzing the Age of Nobel Laureates](#5-analyzing-the-age-of-nobel-laureates)
- [6. Key Learnings and New Techniques](#6-key-learnings-and-new-techniques)
- [7. Day 79 Project: Jupyter Notebook Code Summary](#7-day-79-project-jupyter-notebook-code-summary)

---

### 1. Data Exploration and Cleaning
The first step was to load `nobel_prize_data.csv` and get it ready for analysis.
-   **Initial Inspection:** I used `.shape`, `.info()`, and `.isna().sum()` to understand the dataset's size and identify missing values.
-   **Calculating Winner's Age:** The dataset had birth dates but not the age at which the prize was won. I converted the `birth_date` to a `datetime` object and created a new `winning_age` column by subtracting the birth year from the prize year.
-   **Handling Missing Data:** I noticed that organizations (like the World Food Programme) do not have birth dates, resulting in `NaN` values for age, which I handled in subsequent analyses.

---

### 2. Top Countries and Prize Categories
Using Pandas, I aggregated the data to find key trends.
-   **Top Countries:** I used `.value_counts()` on the `birth_country` column to identify the countries that have produced the most Nobel laureates. The United States was the clear leader.
-   **Prize Distribution:** A Plotly donut chart beautifully visualized the number of prizes awarded in each category (e.g., Physics, Chemistry, Peace).

---

### 3. Visualizing Global Distribution with a Choropleth Map
To visualize the geographic distribution of winners, I created an interactive choropleth map with Plotly Express.
-   I first calculated the number of prize winners per country and stored it in a DataFrame.
-   The `px.choropleth()` function then mapped this data onto a world map, coloring each country based on its number of laureates. This powerfully illustrated the concentration of winners in North America and Europe.


---

### 4. Uncovering Demographic Patterns with a Sunburst Chart
A sunburst chart is perfect for visualizing hierarchical data. I used Plotly's `px.sunburst()` to break down the winners by continent, country, and gender.
-   This multi-level chart clearly showed not only which countries dominated but also the stark gender imbalance within those countries and across all Nobel categories.


---

### 5. Analyzing the Age of Nobel Laureates
I investigated how the age of Nobel winners has changed over time.
-   **`sns.lmplot()`:** I used Seaborn's `lmplot` to create a scatter plot of `winning_age` vs. `year`.
-   **LOWESS Trendline:** The key feature here was setting `lowess=True`. This fits a Locally Weighted Scatterplot Smoothing (LOWESS) line to the data, which is more flexible than a straight line and better at capturing non-linear trends. The plot revealed that, on average, Nobel laureates have been getting older over the last century.
-   **Categorical Analysis:** I also used the `hue` and `row` parameters in `lmplot` to create separate trendlines for each prize category, revealing different age trends across fields.

---

### 6. Key Learnings and New Techniques
-   **Choropleth Maps:** Learned to create interactive maps to represent geographic data.
-   **Sunburst Charts:** Mastered a new technique for visualizing hierarchical data effectively.
-   **Seaborn `lmplot`:** Utilized `lmplot` with `lowess=True` to fit flexible, non-linear trendlines to scatter plot data.
-   **Data Storytelling:** Practiced combining multiple visualizations and analyses to build a comprehensive narrative from a dataset.

---

### 7. Day 79 Project: Jupyter Notebook Code Summary
Here are key code snippets that highlight the new visualization techniques used in this project.

```python
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# --- Data Preparation ---
df_data = pd.read_csv('nobel_prize_data.csv')
df_data['winning_age'] = df_data['year'] - pd.to_datetime(df_data['birth_date']).dt.year

# --- Choropleth Map of Winners per Country ---
country_counts = df_data.groupby('birth_country_current', as_index=False).agg({'full_name': pd.Series.count})
country_counts.sort_values('full_name', ascending=False, inplace=True)

world_map = px.choropleth(country_counts,
                          locations='ISO',
                          color='full_name',
                          hover_name='birth_country_current',
                          color_continuous_scale=px.colors.sequential.matter,
                          title='Number of Nobel Prize Winners by Country')
world_map.show()


# --- Sunburst Chart of Demographics ---
country_gender = df_data.groupby(['ISO', 'sex'], as_index=False).agg({'prize': pd.Series.count})
country_gender.sort_values('prize', ascending=False, inplace=True)

sunburst = px.sunburst(country_gender,
                       path=['ISO', 'sex'],
                       values='prize',
                       title='Nobel Prizes by Country and Gender')
sunburst.show()


# --- Seaborn lmplot with LOWESS ---
with sns.axes_style("whitegrid"):
    sns.lmplot(data=df_data,
               x='year',
               y='winning_age',
               hue='category',
               lowess=True, 
               aspect=2,
               scatter_kws={'alpha': 0.5},
               line_kws={'linewidth': 5})
plt.show()
```