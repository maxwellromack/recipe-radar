import numpy as np

def encode(path):
    size = 0
    with open('ingredients_list.txt') as file:
        for size, _ in enumerate(file):
            pass
    
    arr = np.zeros(size, dtype = 'int')
    index = 0
    with open('ingredients_list.txt', 'r') as list:
        while ingredient := list.readline():
            with open(path, 'r') as recipe:
                if ingredient in recipe.read():
                    arr[index] = 1
    bin_str = np.array2string(arr)
    bin_str = bin_str.replace(' ','')
    bin_str = bin_str.replace(']','')
    bin_str = bin_str.replace('[','')
    return bin_str
