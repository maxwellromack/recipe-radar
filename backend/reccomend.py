from flask import Blueprint, jsonify, session
from backend.auth import login_required, get_db
from backend.user import get_max_length, get_num_ingredients    # type: ignore
import numpy as np
import sys

def build_user_arr(string, length):
    arr = np.zeros(length, dtype = 'int')
    ind = 0

    for c in string:
        arr[ind] = c
        ind += 1

    return arr

def build_recipe_arr(db, length):
    arr = np.zeros((get_num_ingredients, length), dtype = 'int')
    arr_r = 0
    cursor = db.execute('SELECT ingredients FROM recipe')

    for row in cursor:
        string = row.fetchone()
        arr_c = 0
        for c in string:
            arr[arr_r, arr_c]
            arr_c += 1
    
    return arr

bp = Blueprint('reccomend', __name__, url_prefix = '/rec')

@bp.route('/update', methods = ['GET']) # type: ignore
@login_required
def update():
    user_id = session.get('user_id')
    db = get_db
    error = None
    length = get_max_length() * 27
    user_ing = ''

    try:
        user_ing = (db.execute(
                'SELECT ingredients FROM user WHERE id = ?',
                (user_id,),
            )).fetchone()[0]
    except:
        error = 'User ingredients not set'
    if len(user_ing) != length:
        error = 'Ingredients length mismatch'

    if error is None:
        user_arr = build_user_arr(user_ing, length)

