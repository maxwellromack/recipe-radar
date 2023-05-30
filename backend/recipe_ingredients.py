# Using the most common ingredients found in ingredient_counts.py, finds occurances of those ingredients in the recipies.
# Author: Maxwell Romack

prefix = 'recipes/'
num_recipes = 100

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

