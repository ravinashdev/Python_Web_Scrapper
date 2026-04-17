# ---------------------------- IMPORTS ------------------------------- #
from bs4 import BeautifulSoup
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
# ---------------------------- CONSTANTS ------------------------------- #
# Parse the html file and parse its contents to set equal to a variable
with open("website.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")
# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


print(soup.prettify())
# Dictionary key:value notation to read a webpage
print(soup.title)
print(soup.html.head.meta)
print(soup.h3["class"])

# Grab all URLS on a website
for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.get_text())