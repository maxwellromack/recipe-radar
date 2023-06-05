from flask import Blueprint, jsonify, session
from backend.auth import login_required, get_db
from backend.user import get_num_ingredients
import numpy as np
import sys, os

def get_num_recipes(db):
    return db.execute('SELECT COUNT(*) FROM recipe').fetchone()[0]

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

@bp.route('/update', methods = ['GET'])
@login_required
def update():
    user_id = session.get('user_id')
    db = get_db()
    error = None
    length = get_num_recipes(db)
    user_ing = ''

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
        srt_str = np.array2string(sorted)

        return jsonify({'message': 'Matched user ingredients with recipes', 'recipes': srt_str}), 200
    else:
        return jsonify({'error': error}), 400
