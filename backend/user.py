from flask import Blueprint, request, jsonify, g
from backend.auth import login_required, get_db
import numpy as np
import sys, time

def get_max_length():
    max = 0
    with open('ingredients_list.txt', 'r') as f:
        while line := f.readline():
            if max < len(line):
                max = len(line)
    
    return max

def get_num_ingredients():
    size = 0
    with open('ingredients_list.txt', 'r') as file:
        for size, _ in enumerate(file):
            pass
    
    return size

bp = Blueprint('user', __name__, url_prefix = '/user')

@bp.route('/add', methods = ['POST'])   # type: ignore
@login_required
def add():
    start_time = time.time()
    data = request.get_json()
    input = data.get('input')
    user_id = g.user
    length = get_max_length()
    size = get_num_ingredients()

    # TODO: input validation
    
    # one-hot encode the input
    input_arr = np.zeros(length * 27, dtype = 'int').T
    for i in range(len(input)):
        ins = ord(input[i])
        if ins == 32:
            input_arr[i * 27] = 1
        else:
            ins = (ins - 96) + (i * 27)
            input_arr[ins] = 1
    
    # one-hot encode the ingredients list
    ing_arr = np.zeros((size, length * 27), dtype = 'int')
    with open('ingredients_list.txt', 'r') as f:
        for row in range(size):
            line = f.readline().rstrip()
            for i in range(len(line)):
                ins = ord(line[i])
                if ins == 32:
                    ing_arr[row, i * 27] = 1
                else:
                    ins = (ins - 96) + (i * 27)
                    ing_arr[row, ins] = 1

    neighbors = np.empty(size)
    for row in range(size):
        neighbors[row] = np.linalg.norm(input_arr - ing_arr[row])
    
    min = np.argmin(neighbors)
    if neighbors[min] == 0:   # perfect match found
        # TODO: add ingredient to db
        pass
    else:
        # TODO: similar ingredient suggestion
        pass
    
    print("Ingredient add function completed in " + str(time.time() - start_time) + " seconds.")

if len(sys.argv) == 2:
    if sys.argv[1] == 'debug':
        print(get_max_length())
        print(get_num_ingredients())

        