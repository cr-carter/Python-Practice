'''
The purpose of this project was to be introducted to BeautifulSoup and web scrapping.
I learned the basics of scraping HTML data, using find and select. This scraped an article
of the 100 best movies, then created a .txt file with the list of movies.
'''

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, 'html.parser')
movies = soup.select('h3.title')
movies.reverse()
watch_list = [movie.getText() for movie in movies]

print(watch_list)
with open('./movies.txt', "w", encoding='utf-8') as file:
    file.writelines(f'{title}\n' for title in watch_list)
