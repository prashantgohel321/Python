# Day 75: Google Trends and Time-Series Data Visualisation

Welcome to Day 75! Today, I explored several datasets from Google Trends to see if search popularity can reveal insights into financial markets and economic indicators. This project combined all the data analysis and visualization skills from the past few days and introduced new, powerful techniques for working with time-series data.

The main challenge was to combine datasets with different time granularities (e.g., daily vs. monthly) to create meaningful comparisons and visualizations.

## Table of Contents
- [1. Data Exploration and Initial Analysis](#1-data-exploration-and-initial-analysis)
- [2. Resampling Time-Series Data with `.resample()`](#2-resampling-time-series-data-with-resample)
- [3. Advanced Charting with Matplotlib](#3-advanced-charting-with-matplotlib)
- [4. Case Study 1: Tesla Stock Price vs. Search Trend](#4-case-study-1-tesla-stock-price-vs-search-trend)
- [5. Case Study 2: Bitcoin Price vs. Search Trend](#5-case-study-2-bitcoin-price-vs-search-trend)
- [6. Case Study 3: Unemployment Benefits vs. Unemployment Rate](#6-case-study-3-unemployment-benefits-vs-unemployment-rate)
- [7. Day 75 Project: Jupyter Notebook Code Summary](#7-day-75-project-jupyter-notebook-code-summary)

---

### 1. Data Exploration and Initial Analysis
I worked with several CSV files, each containing time-series data:
-   `TESLA Search Trend vs Price.csv`
-   `Daily Bitcoin Price.csv` & `Bitcoin Search Trend.csv`
-   `UE Benefits Search vs UE Rate 2004-19.csv`

For each dataset, I started by:
-   Loading the data into a Pandas DataFrame.
-   Using `.describe()` to get a quick statistical summary.
-   Checking for and handling missing (`NaN`) values.
-   Converting date strings into `datetime` objects using `pd.to_datetime()` to enable time-series analysis.

---

### 2. Resampling Time-Series Data with `.resample()`
A key challenge was that the Bitcoin price data was daily, while the search trend data was monthly. To compare them, they needed to have the same time interval.

-   **`.resample('M')`:** I used this powerful Pandas method on the `datetime` index to downsample the daily Bitcoin price data. It groups the daily data into monthly bins.
-   **Aggregation:** After resampling, an aggregation function like `.last()` or `.mean()` is needed to decide which daily value should represent the entire month. I chose `.last()` to get the closing price at the end of the month.

```python
# df_btc_price has daily data
# Resample to get the last price of each month
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
```

---

### 3. Advanced Charting with Matplotlib
This project required more sophisticated plotting techniques to make the charts clear and readable.

-   **Date Formatting:** The x-axis on time-series plots can get very crowded. I used `matplotlib.dates` to control the formatting.
    -   `YearLocator` and `MonthLocator` were used to specify where the major and minor ticks on the x-axis should appear.
    -   `DateFormatter` allowed me to format the date labels (e.g., showing only the year).

-   **Dual Y-Axes with `twinx()`:** When plotting two datasets with vastly different scales (like a stock price in hundreds of dollars vs. a search trend index from 0-100), a second y-axis is essential. `ax2 = ax1.twinx()` creates a second axis that shares the same x-axis.



---

### 4. Case Study 1: Tesla Stock Price vs. Search Trend
I analyzed the relationship between the Tesla stock price and its Google search popularity. The dual-axis chart clearly showed how spikes in search interest often correlated with significant movements in the stock price.

---

### 5. Case Study 2: Bitcoin Price vs. Search Trend
After resampling the daily price data to a monthly frequency, I could plot it alongside the monthly search data. The visualization revealed a striking correlation, especially during Bitcoin's massive price bubbles, where search interest exploded in tandem with the price.

---

### 6. Case Study 3: Unemployment Benefits vs. Unemployment Rate
This analysis showed how Google searches for "Unemployment Benefits" mirrored the actual US unemployment rate, particularly during economic downturns like the 2008 financial crisis and the COVID-19 pandemic. The search data often acted as a leading indicator of the economic climate.

---

### 7. Day 75 Project: Jupyter Notebook Code Summary
Here is a highlight of the key code used to resample data and create a dual-axis plot with custom date formatting.

```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# --- Load and Prepare Data ---
df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)

df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)
df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)

# --- Resample Daily Bitcoin Data to Monthly ---
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()

# --- Visualization with Dual Axes and Date Formatting ---
plt.figure(figsize=(14,8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)

ax1 = plt.gca() # get current axis
ax2 = ax1.twinx()

# Format the x-axis for years and months
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

# Plotting the data
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)

plt.show()

```