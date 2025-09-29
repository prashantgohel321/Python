# Day 76: Google Play Store App Analytics with Plotly

Welcome to Day 76! Today’s project was a comprehensive analysis of the Google Play Store, using a real-world dataset to understand the dynamics of the app market. This was an excellent exercise in data cleaning and introduced a fantastic new tool for data visualization: Plotly.

The goal was to take a messy, raw dataset and transform it into a series of insightful, interactive visualizations that reveal trends in app categories, pricing, and ratings.

## Table of Contents
- [1. Data Cleaning and Preparation](#1-data-cleaning-and-preparation)
- [2. Exploring the App Data](#2-exploring-the-app-data)
- [3. Visualizing Data with Plotly](#3-visualizing-data-with-plotly)
- [4. Uncovering Pricing and Revenue Insights](#4-uncovering-pricing-and-revenue-insights)
- [5. Key Findings and Learnings](#5-key-findings-and-learnings)
- [6. Day 76 Project: Jupyter Notebook Code Summary](#6-day-76-project-jupyter-notebook-code-summary)

---

### 1. Data Cleaning and Preparation
The raw `apps.csv` dataset was messy and required significant cleaning before any analysis could be done.

-   **Dropping Duplicates:** I used `.duplicated()` and `.drop_duplicates()` to identify and remove thousands of duplicate entries.
-   **Handling Missing Values:** I inspected the data for `NaN` values and dropped rows that were missing critical information like `Rating` and `Android_Ver`.
-   **Data Type Conversion:** Many columns that should have been numeric (like `Installs` and `Price`) were stored as strings with characters like `,`, `+`, and `$`. I wrote code to strip these characters and convert the columns to numeric types, which is essential for calculations and plotting.

```python
# Remove symbols from the 'Installs' column
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)

# Remove '$' from the 'Price' column
df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
```

---

### 2. Exploring the App Data
Once the data was clean, I started exploring it to find initial insights.

-   **Highest Rated Apps:** I used `.sort_values()` to find the apps with the highest ratings and the largest number of reviews.
-   **Category Analysis:** Using `.groupby('Category')`, I aggregated the data to find the number of apps in each category, the average rating, and the total number of installs. This helped identify the most crowded and potentially most popular categories.

---

### 3. Visualizing Data with Plotly
Instead of Matplotlib, I used **Plotly Express** for this project. Plotly creates beautiful, interactive, and web-ready visualizations with concise code.

-   **Donut Chart:** I created a donut chart to show the distribution of apps by Content Rating (e.g., Everyone, Teen, Mature 17+). Plotly makes it easy to add hover-over data and customize the chart's appearance.


-   **Bar Chart:** A bar chart visualized the number of apps in the top 10 categories, clearly showing that Family and Game categories dominate the Play Store.
-   **Scatter Plot:** I created a scatter plot to show the relationship between the number of installs and the number of reviews, using a color scale to represent the app's rating.

---

### 4. Uncovering Pricing and Revenue Insights
I segmented the data into free and paid apps to analyze pricing strategies.

-   **Revenue Estimation:** For paid apps, I created a new `Revenue_Estimate` column by multiplying the `Installs` by the `Price`.
-   **Box Plots:** I used a Plotly box plot to visualize the distribution of prices across different app categories. This was a great way to see the price range, median price, and identify outliers in each category. Medical and Family apps showed the highest price points.


---

### 5. Key Findings and Learnings
-   The Family and Game categories have the most apps.
-   Tools and Entertainment apps have the highest number of installs.
-   There's a huge disparity between free and paid apps in terms of download volume.
-   Most paid apps are priced under $10, with Medical and Dating categories showing a willingness for higher prices.

---

### 6. Day 76 Project: Jupyter Notebook Code Summary
Here are some key code snippets from the notebook, showcasing data cleaning and Plotly visualization.

```python
import pandas as pd
import plotly.express as px

# --- Data Cleaning ---
df_apps_clean = pd.read_csv('apps.csv')
df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'], inplace=True)
df_apps_clean.dropna(inplace=True)

# Clean and convert 'Installs' and 'Price'
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',', "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)

df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace('$', "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)

# --- Visualization with Plotly Express ---

# Donut Chart for Content Rating
ratings = df_apps_clean.Content_Rating.value_counts()
fig = px.pie(labels=ratings.index, 
             values=ratings.values, 
             title="Content Rating",
             names=ratings.index,
             hole=0.6)
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.show()

# Bar Chart for App Categories
top10_category = df_apps_clean.Category.value_counts()[:10]
bar = px.bar(x=top10_category.index, y=top10_category.values)
bar.show()

# Box Plot for Paid App Prices by Category
df_paid_apps = df_apps_clean[df_apps_clean['Price'] > 0]
box = px.box(df_paid_apps,
             x='Category',
             y="Price",
             title='Price per Category',
             log_y=True) # Use a log scale for better visualization
box.show()
```