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
url_response = requests.get("https://news.ycombinator.com/news")
# print(response.text)
soup = BeautifulSoup(url_response.text, "html.parser")
# print(soup.prettify())
titles = soup.find_all("td", class_="title")
title_text = titles
for element in titles:
    # print(element)
    anchor = element.find("a")
    # print(anchor)
    if anchor:
        anchor_text = anchor.get_text(strip=True)
        anchor_link = anchor["href"]
        print(anchor_text)
        print(anchor_link)

