# Gets the number of times each ingredient occurs in a recipe in the recipes folder.
# Using the counts, creates a file listing the 32 most common ingredients.

from collections import Counter
import os

prefix = 'recipes/'
num_recipes = 0
ingredients = []    # Empty list for storing the ingredients

def clean(string):  # Removes any numbers from the string as well as units of measurement
    string = string.replace('1', '')
    string = string.replace('2', '')
    string = string.replace('3', '')
    string = string.replace('4', '')
    string = string.replace('5', '')
    string = string.replace('6', '')
    string = string.replace('7', '')
    string = string.replace('8', '')
    string = string.replace('9', '')
    string = string.replace('0', '')
    string = string.replace('tsp', '')
    string = string.replace('tbsp', '')
    string = string.replace('ml', '')
    string = string.replace('/', '')
    string = string.replace('handful', '')
    if string.startswith('-'):
        string = string[1:]
    if string.startswith('g'):
        string = string[1:]
    if string.startswith('L'):
        string = string[1:]
    string = string.strip()
    return string

def get_ingredients(path):
    ingredients_list = []
    with open('common_ingredients.txt') as common:
        for ingredient in common:
            file = open(path, 'r')
            if ingredient in file.read():
                ingredients_list.append(1)
            else:
                ingredients_list.append(0)
            file.close()

    bin_string = ''
    for digit in ingredients_list:
        bin_string += str(digit)
    return int(bin_string, 2)   # Converts the binary string to an int

for id in range(num_recipes):
    path = prefix + str(id) + '.txt'
    with open(path, 'r') as check:
        if 'METADATA:' not in check:    # Prevents adding the ingredients metadata to file if it already exists
            with open(path, 'a') as file:
                file.write('\nMETADATA: ' + str(get_ingredients(path)) + '\n')

list = os.listdir(prefix)

for f in list:
    #check if current path is a file
    if os.path.isfile(os.path.join(prefix,f)):
        num_recipes +=1

for id in range(num_recipes):
    path = prefix + str(id) + '.txt'
    file = open(path, 'r')

    line = file.readline()
    while 'Ingredients:' not in line:
        line = file.readline()
    line = file.readline()
    
    while 'Instructions:' not in line:
        ingredients.append(clean(line))
        line = file.readline()
    
    file.close()

ingredients_list = Counter(ingredients).most_common(33) # For some reason empty lines are counted as an ingredient, so we take the 33 most common to account for that

file = open('common_ingredients.txt', 'w')    # Creates a file storing the most common ingredients.

for ingredient in ingredients_list:
    if ingredient[0]:   # Gets rid of that annoying empty string
        file.write(ingredient[0] + '\n')

file.close()




