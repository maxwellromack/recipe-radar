# Gets the number of times each ingredient occurs in a recipe in the recipes folder.
# Author: Maxwell Romack

from collections import Counter

prefix = 'recipes/'
num_recipes = 100   # Change based on how many recipes are in the /recipes folder
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

print(Counter(ingredients).most_common(33)) # For some reason empty lines are counted as an ingredient, so we take the 33 most common to account for that
