import bs4
import os, sys, time

old_prefix = 'unconverted_recipes/'
new_prefix = 'recipes/'

def convert(path, id):
    with open(path, 'r') as source:
        soup = bs4.BeautifulSoup(source.read(), features = 'html.parser')
        new_path = new_prefix + str(id) + '_dirty.txt'
        with open(new_path, 'wt', encoding = 'utf-8') as destination:
            destination.write(soup.get_text())

def clean(id):
    with os.scandir(new_prefix) as dir:
        start_time = time.time()
        for entry in dir:
            with open(entry.path, 'r') as dirty:
                with open(new_prefix + str(id) + '.txt', 'wt') as clean:
                    print("Cleaning " + str(entry.path))
                    try:
                        dirty.readline()
                    except UnicodeDecodeError:
                        clean.write('DELETE')
                        continue
                    dirty.readline()

                    # get title
                    title = dirty.readline()
                    if title.isspace():
                        clean.write('DELETE')
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

                    loop_start = time.time()
                    while 'Serves' not in dirty.readline():
                        if round(time.time() - loop_start) > 5:
                            break
                        continue

                    # get servings
                    servings = dirty.readline()
                    if 'Serves' not in servings:
                        clean.write('DELETE')
                        continue
                    try:
                        clean.write("Serves: " + servings[7] + '\n')
                    except IndexError:
                        clean.write('DELETE')
                        continue

                    author = dirty.readline()
                    bad_recipe = 0
                    while 'By' not in author:
                        author = dirty.readline()
                        if 'Ingredients' in author or 'Dietary' in author:
                            clean.write('DELETE')
                            bad_recipe = 1
                            break
                    if bad_recipe == 1:
                        continue
                    clean.write("Author: " + author[3:] + '\n')

                    while 'Ingredients' not in dirty.readline():
                        continue
                    
                    # get ingredients
                    clean.write("Ingredients:\n")
                    line = dirty.readline()
                    add_list = open('ingredients_list.txt', 'a')
                    while 'Method' not in line: # this is about to get really stupid
                        if line.isspace():
                            line = dirty.readline()
                        elif line[:3] == 'For':
                            clean.write('\n'+ line + '\n')
                            line = dirty.readline()
                        elif line[:2] == 'To':
                            clean.write(line + '\n')
                            line = dirty.readline()
                        elif bad_recipe == 0:
                            with open('ingredients_list.txt', 'r') as read_list:
                                found = 0
                                edit_line = line.replace(',', '')
                                if 'chicken or vegetable stock' in edit_line:
                                    clean.write(line)
                                    line = dirty.readline()
                                    continue
                                for ingredient in read_list:
                                    if ingredient.strip() in edit_line:
                                        found = 1
                                        clean.write(line)
                                        line = dirty.readline()
                                        break
                                if found == 0:
                                    print(line)
                                    choice = input("Enter ingredient or type 'delete' if there is no ingredient or 'skip' to skip: ")
                                    if choice == 'delete':
                                        clean.write('DELETE')
                                        bad_recipe = 1
                                        break
                                    elif choice == 'skip':
                                        line = dirty.readline()
                                    else:
                                        add_list.write(choice + '\n')
                                        clean.write(line)
                                        line = dirty.readline()
                    add_list.close()
                    if bad_recipe == 1:
                        continue

                    dirty.readline()
                    dirty.readline()

                    # get instructions
                    clean.write("\nInstructions:\n")
                    instruction = dirty.readline()
                    while not instruction.isspace():
                        clean.write(instruction)
                        dirty.readline()
                        dirty.readline()
                        instruction = dirty.readline()

            with open(new_prefix + str(id) + '.txt', 'r') as check:
                if 'DELETE' in check:
                    os.remove(new_prefix + str(id) + '.txt')
                    os.remove(entry.path)
                    continue
            os.remove(entry.path)
            id += 1
        print(str(id - start_id) + " files cleaned in " + str(round(time.time() - start_time)) + " seconds!")

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
    print(str(id - start_id) + " files converted in " + str(round(time.time() - start_time)) + " seconds!")

clean(start_id)
