# Converts html recipe files into text files
# Author: Maxwell Romack

import bs4
import os

path = R'C:\Users\Max\Documents\GitHub\recipe-radar\recipe-converter\recipe-source'
id = 0
with os.scandir(path) as dir:
    for entry in dir:
        if entry.name.endswith('.html') and entry.is_file():
            source = open(entry.path, 'r')
            soup = bs4.BeautifulSoup(source.read())
            file_name = str(id) + '.txt'
            destination = open(file_name, 'wt', encoding="utf-8")   # puts output files in the folder where the script is run, which is not ideal
            destination.write(soup.get_text())                      # but this is a 'run once' script, not fixing it
            source.close()
            destination.close
            id += 1

