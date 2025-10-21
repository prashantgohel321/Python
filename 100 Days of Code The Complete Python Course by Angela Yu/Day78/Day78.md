# Day 78: Linear Regression with Seaborn and Scikit-Learn

Welcome to Day 78! Today's project was a deep dive into the relationship between movie production budgets and worldwide revenue. I used a new dataset (`cost_revenue_dirty.csv`) that required careful cleaning and then applied two new, powerful libraries: **Seaborn** for statistical data visualization and **Scikit-Learn** for building a linear regression model.

The central question was: can a movie's budget predict its financial success?

## Table of Contents
- [1. Data Cleaning and Preparation](#1-data-cleaning-and-preparation)
- [2. Visualizing Relationships with Seaborn](#2-visualizing-relationships-with-seaborn)
- [3. Building a Linear Regression Model](#3-building-a-linear-regression-model)
- [4. Evaluating the Model and Making Predictions](#4-evaluating-the-model-and-making-predictions)
- [5. Key Learnings](#5-key-learnings)
- [6. Day 78 Project: Jupyter Notebook Code Summary](#6-day-78-project-jupyter-notebook-code-summary)

---

### 1. Data Cleaning and Preparation
The dataset was labeled "dirty" for a reason. The financial columns were stored as strings containing '$' and ',' characters, making them unusable for calculations.
-   I iterated through the relevant columns (`USD_Production_Budget`, `USD_Worldwide_Gross`, `USD_Domestic_Gross`).
-   For each value, I removed the currency symbols and commas.
-   I converted the cleaned strings into numeric data types using `pd.to_numeric()`.
-   I also converted the `Release_Date` column to `datetime` objects to enable time-based analysis.

---

### 2. Visualizing Relationships with Seaborn
Seaborn is a data visualization library built on top of Matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics.
-   **`sns.scatterplot()`:** I started by creating a scatter plot to visualize the relationship between `USD_Production_Budget` (x-axis) and `USD_Worldwide_Gross` (y-axis).
-   **`sns.regplot()`:** To take it a step further, I used Seaborn's regression plot function. This function not only creates the scatter plot but also automatically estimates and plots a linear regression model, complete with a confidence interval. This provided the first visual clue that a positive correlation exists.



---

### 3. Building a Linear Regression Model
While Seaborn can plot a regression line, Scikit-Learn allows me to build and analyze the model itself.
-   **Import `LinearRegression`:** I imported the linear regression model from `sklearn.linear_model`.
-   **Prepare Data:** I defined my feature (X) as the `USD_Production_Budget` and my target (y) as the `USD_Worldwide_Gross`. I reshaped the feature data into a 2D array, as required by Scikit-Learn.
-   **Fit the Model:** I created an instance of the `LinearRegression` class and used the `.fit(X, y)` method to train the model on my data.

---

### 4. Evaluating the Model and Making Predictions
After fitting the model, I could extract valuable information:
-   **Intercept and Slope (Coefficient):** I accessed `regression.intercept_` and `regression.coef_` to get the parameters of the regression line. The slope tells me how much revenue is expected to increase for every one-dollar increase in budget.
-   **R-Squared:** I used `regression.score(X, y)` to calculate the R-squared value. This metric tells me what percentage of the variation in movie revenue can be explained by the production budget. For this dataset, the R-squared value was around 0.55, indicating a moderate positive relationship.
-   **Making Predictions:** I used the trained model to predict the revenue for a hypothetical movie with a budget of $350 million.

---

### 5. Key Learnings
-   Real-world data is often messy and requires careful cleaning before analysis.
-   Seaborn simplifies the creation of complex statistical plots like regression plots.
-   Scikit-Learn provides a straightforward workflow for building, training, and evaluating machine learning models like linear regression.
-   R-squared is a key metric for understanding how well a linear model fits the data.

---

### 6. Day 78 Project: Jupyter Notebook Code Summary
Here are the key code snippets from the notebook, demonstrating data cleaning, Seaborn visualization, and linear regression with Scikit-Learn.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# --- Data Cleaning ---
data = pd.read_csv('cost_revenue_dirty.csv')
chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget', 'USD_Worldwide_Gross', 'USD_Domestic_Gross']

for col in columns_to_clean:
    for char in chars_to_remove:
        data[col] = data[col].astype(str).str.replace(char, "")
    data[col] = pd.to_numeric(data[col])

# --- Seaborn Visualization ---
plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style("whitegrid"):
    sns.regplot(data=data,
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross',
                scatter_kws={'alpha': 0.3},
                line_kws={'color': 'red'})
plt.show()

# --- Scikit-Learn Linear Regression ---
regression = LinearRegression()

# Prepare data
X = pd.DataFrame(data, columns=['USD_Production_Budget'])
y = pd.DataFrame(data, columns=['USD_Worldwide_Gross'])

# Fit the model
regression.fit(X, y)

# Get R-squared
r_squared = regression.score(X, y)
print(f"R-squared: {r_squared:.2f}")

# Get intercept and coefficient
intercept = regression.intercept_[0]
slope = regression.coef_[0, 0]
print(f"Intercept: {intercept}")
print(f"Slope: {slope}")
```