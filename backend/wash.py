import bs4
import os, sys

old_prefix = 'unconverted_recipes/'
new_prefix = 'recipes/'

def convert(path, id):
    with open(path, 'r') as source:
        soup = bs4.BeautifulSoup(source.read())
        new_path = new_prefix + str(id) + '.txt'
        with open(new_path, 'wt', encoding = 'utf-8') as destination:
            destination.write(soup.get_text())

id = 0
with os.scandir(new_prefix) as dir:
    for entry in dir:
        if entry.is_file():
            id += 1

with os.scandir(old_prefix) as dir:
    
