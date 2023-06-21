from flask import Blueprint, request, jsonify, session, make_response
from backend.auth import get_db
import numpy as np
import sys

def get_max_length():
    max = 0
    with open('backend/ingredients_list.txt', 'r') as f:
        while line := f.readline():
            if max < len(line):
                max = len(line)
    
    return max

def get_num_ingredients():
    size = 0
    with open('backend/ingredients_list.txt', 'r') as file:
        for size, _ in enumerate(file):
            pass
    
    return size

def build_cors_preflight():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
    response.headers.add("Access-Control-Allow-Headers", 'content-type')   # insecure!
    response.headers.add("Access-Control-Allow-Methods", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    return response

def corsify_response(response):
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    return response

bp = Blueprint('user', __name__, url_prefix = '/user')

@bp.route('/add', methods = ['POST', 'OPTIONS'])
#@login_required
def add():
    if request.method == 'OPTIONS':
        return build_cors_preflight()
    else:
        data = request.get_json()
        input = data.get('input')
        #user_id = request.cookies.get('user_id')
        with open('cookie.txt', 'r') as f:
            user_id = int(f.readline())
        length = get_max_length()
        size = get_num_ingredients()
        error = None
        db = get_db()

        input = input.replace('\'', '')
        input = input.replace('-', ' ')

        stripped = input.replace(' ', '')
        if user_id is None:
            error = 'User is not logged in'
        elif len(stripped) == 0:
            error = 'Input is required'
        elif not stripped.isalpha():
            error = 'Input must contain only letters and spaces'
        
        if error is None:
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
            with open('backend/ingredients_list.txt', 'r') as f:
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
            if neighbors[min] == 0: # perfect match found
                user_ing = (db.execute(
                    'SELECT ingredients FROM user WHERE id = ?',
                    (user_id,),
                )).fetchone()[0]
                updated = user_ing[:min] + '1' + user_ing[min + 1:]
                db.execute(
                    'UPDATE user SET ingredients = ? WHERE id = ?',
                    (updated, user_id,),
                )
                db.commit()
                res = corsify_response(jsonify({'message': 'Ingredient added'}))
                res.status_code = 201
                return res
            elif neighbors[min] == 1 and input[-1] == 's':  # match found for singluar form of input
                user_ing = (db.execute(
                    'SELECT ingredients FROM user WHERE id = ?',
                    (user_id,),
                )).fetchone()[0]
                updated = user_ing[:min] + '1' + user_ing[min + 1:]
                db.execute(
                    'UPDATE user SET ingredients = ? WHERE id = ?',
                    (updated, user_id,),
                )
                db.commit()
                res = corsify_response(jsonify({'message': 'Singular ingredient added'}))
                res.status_code = 201
                return res
            elif neighbors[min] < 2:    # possible spelling mistake, suggest similar ingredient to user
                ingredient = ''
                with open('backend/ingredients_list.txt', 'r') as f:
                    for i, ingredient in enumerate(f):
                        if i == min:
                            break
                res = corsify_response(jsonify({
                    'message': 'Similar match found',
                    'ingredient': ingredient
                }))
                res.status_code = 400
                return res
            else:
                res = corsify_response(jsonify({'message': 'No match found'}))
                res.status_code = 400
                return res
        else:
            res = corsify_response(jsonify({'error': error}))
            res.status_code = 400
            return res
