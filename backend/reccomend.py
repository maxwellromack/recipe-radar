from flask import Blueprint, jsonify, session
from backend.auth import login_required, get_db
from user import get_max_length
import numpy as np
import sys

def build_user_arr(string, length):
    arr = np.zeros(length, dtype = 'int')
    ind = 0
    for c in string:
        arr[ind] = c
        ind += 1
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
        user_arr = np.fromstring(user_ing, dtype = 'int', sep = '')
