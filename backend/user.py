from flask import Blueprint, request, jsonify, g
from backend.auth import login_required, get_db

bp = Blueprint('user', __name__, url_prefix = '/user')

@bp.route('/update', methods = ['POST'])
@login_required
def update():
    data = request.get_json()
    ingredients = data.get('ingredients')
    db = get_db()
    error = None

    if not type(ingredients) is int:
        error = 'Ingredients must be of type integer'

    if not ingredients: # if this ever happens then something is really broken
        error = 'Ingredients are required'

    if error is None:
        user_id = g.user['id']

        db.execute(
            'UPDATE user SET ingredients = ? WHERE id = ?',
            (ingredients, user_id,)
        )
        db.commit()

        return jsonify({'message': 'Ingredients updated'}), 201
    return jsonify({'error': error}), 400
