# Assists with cleaning up the converted recipes so I can be more lazy
# Run as 'cleaner.py [messy file].txt [cleaned file].txt'
# Author: Maxwell Romack

import sys

messy = open(sys.argv[1], 'r')
clean = open(sys.argv[2], 'wt')

messy.readline()
messy.readline()

# get title
title = messy.readline()
clean.write("Title: " + title)

while "time" not in messy.readline(): # this is stupid
    continue

# get prep time
print(messy.readline())
prep = input("Enter prep time: ")
clean.write("Prep time: " + prep + '\n')

while "time" not in messy.readline():
    continue

# get cook time
print(messy.readline())
cook = input("Enter cook time: ")
clean.write("Cook time: " + cook + '\n')

while "Serves" not in messy.readline():
    continue

# get servings
print(messy.readline())
serve = input("Enter servings: ")
clean.write("Serves: " + serve + '\n')

# get author
author = messy.readline()
while "By" not in author:
    author = messy.readline()
clean.write("Author: " + author[3:] + '\n')

while ("Ingredients" not in messy.readline()):
    continue

# get ingredients
clean.write("Ingredients:" + '\n')
ingredient = messy.readline()
while "Method" not in ingredient:
    print(ingredient)
    choice = input("edit(1), write(2), or delete(3): ")
    if choice == '1':
        edit = input("Enter edited line: ")
        clean.write(edit + '\n')
    elif choice == '2':
        clean.write(ingredient)
    ingredient = messy.readline()
clean.write('\n')

messy.readline()
messy.readline()

# get instructions
clean.write("Instructions:" + '\n')
instruction = messy.readline()
while len(instruction.strip()) != 0:
    clean.write(instruction)
    messy.readline()
    messy.readline()
    instruction = messy.readline()
