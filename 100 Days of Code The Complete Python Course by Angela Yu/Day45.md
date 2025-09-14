# Day 45: Web Scraping with Beautiful Soup

Welcome to my log for Day 45! Today, I shifted from using structured APIs to a more direct method of data extraction: **Web Scraping**. I learned how to use the `requests` library to fetch the raw HTML of a website and then use the powerful **BeautifulSoup** library to parse that HTML and pull out the specific pieces of information I need. The day culminated in a practical project where I scraped Empire's list of the 100 greatest movies of all time.


## Table of Contents
- [1. Web Scraping: When APIs Aren't Enough](#1-web-scraping-when-apis-arent-enough)
- [2. Introduction to BeautifulSoup](#2-introduction-to-beautifulsoup)
- [3. The Scraping Process](#3-the-scraping-process)
- [4. Finding Elements in the Soup](#4-finding-elements-in-the-soup)
- [5. Ethics and Legality of Web Scraping](#5-ethics-and-legality-of-web-scraping)
- [6. Day 45 Project: Top 100 Movies Scraper](#6-day-45-project-top-100-movies-scraper)

---

### 1. Web Scraping: When APIs Aren't Enough
While APIs are the preferred way to get data from a service, not all websites offer them. Web scraping is the process of programmatically downloading and parsing the HTML content of a webpage to extract data. It allows me to access information from almost any public website, even without a formal API.

---

### 2. Introduction to BeautifulSoup
Manually sifting through a website's messy HTML source code would be a nightmare. **BeautifulSoup** is a Python library that makes this process incredibly easy. It takes the raw HTML text and turns it into a structured Python object that I can navigate and search through.

To use it, I first need to install it: `pip install beautifulsoup4`. It's also common to install a specific parser like `lxml` for better performance.

---

### 3. The Scraping Process
The typical workflow for scraping a website involves two main steps:

1.  **Get the HTML:** Use the `requests` library to send a GET request to the website's URL and retrieve the page content as text.
    ```python
    import requests
    
    response = requests.get("[https://www.example.com](https://www.example.com)")
    website_html = response.text
    ```
2.  **Make the Soup:** Create a `BeautifulSoup` object by passing in the HTML content and specifying a parser.
    ```python
    from bs4 import BeautifulSoup
    
    soup = BeautifulSoup(website_html, "html.parser")
    ```
This `soup` object is now my gateway to all the data on the page.

---

### 4. Finding Elements in the Soup
BeautifulSoup provides several methods to find and extract HTML elements:

-   **Accessing tags directly:** `soup.title` gets the title tag, `soup.h1` gets the first h1 tag.
-   **`find_all(name, class_)`:** This is one of the most useful methods. It returns a *list* of all tags that match the specified criteria (e.g., all `<a>` tags with a certain class).
-   **`find(name, class_)`:** Similar to `find_all`, but it only returns the *first* matching element it finds.
-   **`select(css_selector)` and `select_one(css_selector)`:** These methods allow me to use CSS selectors to find elements, which is incredibly powerful for targeting nested or specific elements.
-   **Extracting Data:** Once I have an element, I can get its content:
    -   `.getText()`: Extracts just the text content from within the tags.
    -   `.get('attribute_name')`: Extracts the value of a specific attribute, like the `href` from an anchor tag.

---

### 5. Ethics and Legality of Web Scraping
This was an important part of the lesson. Just because I *can* scrape a website doesn't always mean I *should*.
-   **Check for an API first:** It's always better to use an official API if one is available.
-   **Check `robots.txt`:** Most websites have a `yourwebsite.com/robots.txt` file that outlines which parts of the site they don't want bots to access. It's important to respect these rules.
-   **Don't Overload Servers:** Scraping too frequently can put a heavy load on a website's server. It's good practice to add delays between requests.
-   **Copyright:** I cannot scrape copyrighted content (like articles or videos) and republish it as my own. Scraping publicly available, non-copyrighted data is generally considered legal, but it can be a gray area.

---

### 6. Day 45 Project: Top 100 Movies Scraper
The final project was to create a Python script that scrapes Empire's "100 Greatest Movies" list and saves the titles to a text file.

The process was as follows:
1.  **Inspect the Website:** I used Chrome Developer Tools to inspect the webpage and identify the HTML tag (`<h3>`) and class (`title`) used for every movie title.
2.  **Fetch and Parse:** I used `requests` to get the website's HTML and `BeautifulSoup` to create a soup object.
3.  **Find All Movies:** I used `soup.find_all(name="h3", class_="title")` to get a list of all the HTML elements containing the movie titles.
4.  **Extract Titles:** I used a list comprehension to loop through the list of movie elements and extract the text from each one using `.getText()`.
5.  **Reverse the List:** The website listed movies from 100 to 1, so I reversed my list of titles to get the correct order (1 to 100) using list slicing (`[::-1]`).
6.  **Write to File:** I opened a new file, `movies.txt`, in write mode and looped through my reversed list, writing each movie title on a new line.

Here is the final code for the project:

```python
# main.py
import requests
from bs4 import BeautifulSoup

URL = "[https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/)"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
```