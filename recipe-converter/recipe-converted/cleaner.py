# Assists with cleaning up the converted recipes so I can be more lazy
# Run as 'cleaner.py [messy file].txt [cleaned file].txt'
# Author: Maxwell Romack

import sys

messy = open(sys.argv[1], 'r')
clean = open(sys.argv[2], 'at')

messy.readline()
messy.readline()

# get title
title = messy.readline()
clean.write("Title: " + title + '\n')

while ("time" not in messy.readline()): # this is stupid
    continue

# get prep time
print(messy.readline())
prep = input("Enter prep time: ")
clean.write("Prep time: " + prep + '\n')

while ("time" not in messy.readline()):
    continue

# get cook time
print(messy.readline())
cook = input("Enter cook time: ")
clean.write("Cook time: " + cook + '\n')

while ("Serves" not in messy.readline()):
    continue

# get servings
print(messy.readline())
serve = input("Enter servings: ")
clean.write("Serves: " + serve + '\n')

# get author
author = messy.readline()
while ("By" not in author):
    author = messy.readline()
clean.write("Author: " + author[3:] + '\n')

while ("Ingredients" not in messy.readline()):
    continue

# get ingredients

# TODO: uhhh the rest of the script lol
