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
empire_response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
# print(empire_response.text)
soup = BeautifulSoup(empire_response.text, "html.parser")
# print(soup.prettify())

movie_title_elements = soup.find_all("h3", class_="title")
top_100_movies_to_watch_list =[]
for info_block in movie_title_elements:
    info = info_block.get_text(strip=True).split(")")
    if len(info) == 2:
        new_item ={
            "rank": int(info[0]),
            "title": info[1].strip(),
        }
        top_100_movies_to_watch_list.append(new_item)
sorted_ascending_top_100_movies_to_watch_list = sorted(top_100_movies_to_watch_list, key=lambda x: x["rank"], reverse=True)
sorted_descending_top_100_movies_to_watch_list = sorted(top_100_movies_to_watch_list, key=lambda x: x["rank"], reverse=False)
print(sorted_descending_top_100_movies_to_watch_list)
print(sorted_ascending_top_100_movies_to_watch_list)


