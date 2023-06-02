import bs4
import os, sys, time

old_prefix = 'unconverted_recipes/'
new_prefix = 'recipes/'

def convert(path, id):
    with open(path, 'r') as source:
        soup = bs4.BeautifulSoup(source.read(), features = 'html.parser')
        new_path = new_prefix + str(id) + '.txt'
        with open(new_path, 'wt', encoding = 'utf-8') as destination:
            destination.write(soup.get_text())

def clean(id):
    with os.scandir(new_prefix) as dir:
        start_time = time.time()
        for entry in dir:
            with open(entry.path, 'r') as dirty:
                with open(new_prefix + str(id) + '.txt', 'wt') as clean:
                    dirty.readline()
                    dirty.readline()

                    # get title
                    title = dirty.readline()
                    if title.isspace():
                        os.remove(entry.path)
                        os.remove(new_prefix + str(id) + '.txt')
                        continue
                    clean.write("Title: " + title)

                    while "time" not in dirty.readline():
                        continue
                    
                    # get prep time
                    prep_time = dirty.readline()
                    if prep_time[0].isalpha():
                        prep_time = prep_time.capitalize()
                    clean.write("Prep time: " + prep_time)

                    while 'time' not in dirty.readline():
                        continue

                    # get cook time
                    cook_time = dirty.readline()
                    if cook_time[0].isalpha():
                        cook_time = cook_time.capitalize()
                    clean.write("Cook time: " + cook_time)

                    while 'Serves' not in dirty.readline():
                        continue

                    # get servings
                    servings = dirty.readline()
                    if 'Serves' not in servings:
                        os.remove(new_prefix + str(id) + '.txt')
                        os.remove(entry.path)
                        continue
                    clean.write("Serves: " + servings[7] + '\n')

                    author = dirty.readline()
                    while 'By' not in author:
                        author = dirty.readline()
                        if 'Ingredients' in author:
                            os.remove(new_prefix + str(id) + '.txt')
                            os.remove(entry.path)
                            continue
                    clean.write("Author: " + author[3:] + '\n')

                    while 'Ingredients' not in dirty.readline():
                        continue
                    
                    # get ingredients
                    clean.write("Ingredients:\n")
                    line = dirty.readline()
                    add_list = open('ingredients_list.txt', 'a')
                    choice = ''
                    while 'Method' not in line: # this is about to get really stupid
                        if line.isspace():
                            line = dirty.readline()
                        elif line[:3] == 'For':
                            clean.write(line + '\n')
                            line = dirty.readline()
                        elif line[:2] == 'To':
                            clean.write(line + '\n')
                            line = dirty.readline()
                        with open('ingredients_list.txt', 'r') as read_list:
                            found = 0
                            for ingredient in read_list:
                                if ingredient in line:
                                    found = 1
                                    clean.write(line)
                            if found == 0:
                                choice = input("Enter ingredient or type 'delete' if there is no ingredient: ")
                                if choice == 'delete':
                                    break
                                else:
                                    add_list.write(choice + '\n')
                                    clean.write(line)
                                    line = dirty.readline()
                    add_list.close()
                    if choice == 'delete':
                        os.remove(new_prefix + str(id) + '.txt')
                        os.remove(entry.path)
                        continue

                    dirty.readline()
                    dirty.readline()

                    # get instructions
                    instruction = dirty.readline()
                    while not instruction.isspace():
                        clean.write(instruction)
                        dirty.readline()
                        dirty.readline()
                        instruction = dirty.readline()
            os.remove(entry.path)
            id += 1

start_id = 1
with os.scandir(new_prefix) as dir:
    for entry in dir:
        if entry.is_file():
            start_id += 1

with os.scandir(old_prefix) as dir:
    start_time = time.time()
    id = start_id
    for entry in dir:
        try:
            convert(entry.path, id)
        except:
            os.remove(entry.path)   # removes files that raise errors when trying to convert
            os.remove(new_prefix + str(id) + '_dirty.txt')
        else:
            id += 1
    print(str(id - (start_id)) + " files converted in " + str(round(time.time() - start_time)) + " seconds!")
