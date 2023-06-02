# Gets the number of times each ingredient occurs in a recipe in the recipes folder.
# Using the counts, creates a file listing the 32 most common ingredients.

from collections import Counter
import os

prefix = 'recipes/'
num_recipes = 0
ingredients = []    # empty list for storing the ingredients

def clean(string):  # removes any numbers from the string as well as units of measurement
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

ingredients_list = Counter(ingredients).most_common(33)

file = open('common_ingredients.txt', 'w')    # creates a file storing the most common ingredients.

for ingredient in ingredients_list:
    if ingredient[0]:   # gets rid of that annoying empty string
        file.write(ingredient[0] + '\n')

file.close()

for id in range(num_recipes):
    path = prefix + str(id) + '.txt'
    ingredients_string = str(get_ingredients(path))
    with open(path, 'r') as check:
        if 'METADATA:' not in check:    # writes metadata if not already written
            with open(path, 'a') as file:
                file.write('\nMETADATA: ' + ingredients_string + '\n')
        else:
            check.seek(0)
            last_num = -1    # stop yelling at me vs code i know what i'm doing
            for num, line in enumerate(check, 0):
                if 'METADATA:' in line and ingredients_string not in line:
                    last_num = num

            if last_num != -1:  # block only runs if the new ingredients are different from exisiting ones
                check.seek(0)
                recipe = check.readlines()
                recipe[last_num] = ('METADATA: ' + ingredients_string + '\n')
                with open(path, 'w') as new_file:
                    new_file.writelines(recipe)
                
