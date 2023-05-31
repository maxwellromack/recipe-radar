# Gets the number of times each ingredient occurs in a recipe in the recipes folder.
# Using the counts, creates a file listing the 32 most common ingredients.
# Author: Maxwell Romack

from collections import Counter

import os

prefix = 'recipes/'
num_recipes = 0   # Change based on how many recipes are in the /recipes folder
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

#Check the function to count the number of files
dir_path = r"backend/recipes/"
list = os.listdir(dir_path)

#print(list)
for f in list:
    #check if current path is a file
    if os.path.isfile(os.path.join(dir_path,f)):
        num_recipes +=1
        
print('File count:', num_recipes)



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
