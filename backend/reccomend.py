from flask import Blueprint, jsonify, session, make_response, request
from backend.auth import login_required, get_db
import numpy as np
import sys, os

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

def get_num_recipes(db):
    return db.execute('SELECT COUNT(*) FROM recipe').fetchone()[0]

def get_num_ingredients():
    size = 0
    with open('backend/ingredients_list.txt', 'r') as file:
        for size, _ in enumerate(file):
            pass
    
    return size

def build_user_arr(string):
    arr = np.zeros(get_num_ingredients(), dtype = 'int')
    ind = 0

    for c in string:
        arr[ind] = c
        ind += 1

    return arr

def build_recipe_arr(db, length):
    arr = np.zeros((length, get_num_ingredients()), dtype = 'int')
    arr_r = 0
    cursor = db.execute('SELECT ingredients FROM recipe')

    for row in cursor:
        string = row
        arr_c = 0
        for c in string:
            arr[arr_r, arr_c]
            arr_c += 1
    
    return arr

bp = Blueprint('reccomend', __name__, url_prefix = '/rec')

@bp.route('/update', methods = ['GET', 'OPTIONS'])
def update():
    if request.method == 'OPTIONS':
        return build_cors_preflight()
    else:
        with open('cookie.txt', 'r') as f:
                user_id = int(f.readline())
        db = get_db()
        error = None
        length = get_num_recipes(db)
        user_ing = ''

        if user_id is None:
            error = 'User not logged in'
        try:
            user_ing = (db.execute(
                    'SELECT ingredients FROM user WHERE id = ?',
                    (user_id,),
                )).fetchone()[0]
        except:
            error = 'User ingredients not set'

        if error is None:
            user_arr = build_user_arr(user_ing)
            recipe_arr = build_recipe_arr(db, length)

            neighbors = np.empty(length)
            for row in range(length):
                neighbors[row] = np.linalg.norm(user_arr - recipe_arr[row])
            
            sorted = np.argsort(neighbors)

            print(str(sorted[1:6]))

            first = (db.execute(
                'SELECT title FROM recipe WHERE id = ?',
                (int(sorted[1]),),
            )).fetchone()[0]
            second = (db.execute(
                'SELECT title FROM recipe WHERE id = ?',
                (int(sorted[2]),),
            )).fetchone()[0]
            third = (db.execute(
                'SELECT title FROM recipe WHERE id = ?',
                (int(sorted[3]),),
            )).fetchone()[0]
            fourth = (db.execute(
                'SELECT title FROM recipe WHERE id = ?',
                (int(sorted[4]),),
            )).fetchone()[0]
            fifth = (db.execute(
                'SELECT title FROM recipe WHERE id = ?',
                (int(sorted[5]),),
            )).fetchone()[0]

            res = corsify_response(jsonify({
                'message': 'Matched user ingredients with recipes',
                'first': first,
                'second': second,
                'third': third,
                'fourth': fourth,
                'fifth': fifth
                }))
            res.status_code = 200
            return res
        else:
            res = corsify_response(jsonify({'error': error}))
            res.status_code = 400
            return res
