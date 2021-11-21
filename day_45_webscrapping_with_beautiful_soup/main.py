"""
Webscrapping using beautiful soup.

100 must watch movies list.
"""

import lxml
import requests

from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "lxml")
movie_title_tags = soup.find_all("h3", class_="title")
movie_titles = [movie_title.get_text() for movie_title in movie_title_tags]

with open("movies.txt", "a") as file:
    for i in range(len(movie_titles) - 1, -1, -1):
        file.write(f"{movie_titles[i]}\n")
