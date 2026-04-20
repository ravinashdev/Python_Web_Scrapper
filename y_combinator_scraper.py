# ---------------------------- IMPORTS ------------------------------- #
from bs4 import BeautifulSoup
import requests
# --------------.env file access flat string--------------#
# Allows you to read the .env file
# from dotenv import load_dotenv
# import os
# variable = os.getenv("<ENV VARIABLE>")
# load_dotenv()
# --------.env.json file access for JSON structure--------#
# .env.json file
# import json
# with open('.env.json') as f:
#     config = json.load(f)
# value = config.get('YOUR_KEY')
# --------DYNACONF Config Prod & Dev--------#
# ---------------------------- CONSTANTS ------------------------------- #

# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
y_combinator_response = requests.get("https://news.ycombinator.com/news")
# print(response.text)
soup = BeautifulSoup(y_combinator_response.text, "html.parser")
# print(soup.prettify())
# title_row_1 = soup.find(name="tr", class_="athing submission").find_all("a")[1]
# title_row_2 = soup.find(name="td", class_="subtext").find("span", class_="score")
title_row_1 = soup.find_all(name="tr", class_="athing submission")
title_row_2 = soup.find_all(name="td", class_="subtext")


# print(title_row_1)
# print(title_row_2)
articles = []
# Use a zip sort to iterate over two list since there is a relation
for anchor_row, score_row in zip(title_row_1, title_row_2):
    # print(anchor_row.find_all("a")[1].get_text(strip=True))
    # print(anchor_row.find_all("a")[1].get("href"))
    # print(score_row.find("span", class_="score").get_text(strip=True))
    # print("\n")
    new_entry= {
        # Target 2nd element since we get 2 anchor tags
        "title": anchor_row.find_all("a")[1].get_text(strip=True),
        "link": anchor_row.find_all("a")[1].get("href"),
        # Split string into elements and convert it to an into to later sort the dict,
        "score": int(score_row.find_all("span")[1].get_text(strip=True).split()[0]),
    }
    articles.append(new_entry)
# print(articles)
# List to sort, key to sort by with an anonymous function, and the direction of the sort
# from collections import OrderedDict
# sorted_ordered = OrderedDict(sorted(d.items(), key=lambda item: item[1]))
sorted_articles_descending_by_score = sorted(articles, key=lambda k: k["score"], reverse=True)
sorted_articles_ascending_by_score = sorted(articles, key=lambda k: k["score"], reverse=False)

print("Articles Descending")
for article in sorted_articles_descending_by_score:
    title = article["title"]
    link = article["link"]
    score = article["score"]
    print(f"Title: {title} \nLink: {link} \nScore: {score}")
    print("\n")

print("Articles Ascending")
for article in sorted_articles_ascending_by_score:
    title = article["title"]
    link = article["link"]
    score = article["score"]
    print(f"Title: {title} \nLink: {link} \nScore: {score}")
    print("\n")









