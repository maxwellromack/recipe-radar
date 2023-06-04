import json
import pytest
from flask import g
from backend.db import get_db

# def test_update(client, auth, app):
#     auth.register()
#     auth.login()

#     payload = {
#         'ingredients': 6
#     }

#     json_payload = json.dumps(payload)
#     response = client.post('/user/update', data = json_payload.encode('utf8'), content_type = 'application/json')

#     assert response.status_code == 201
#     assert response.get_json() == {'message': 'Ingredients updated'}

#     with app.app_context():
#         db = get_db()
#         user_ingredients = (db.execute(
#             'SELECT ingredients FROM user WHERE id = 3'
#         )).fetchone()[0]
#         assert user_ingredients == 6

# @pytest.mark.parametrize(('ingredients', 'message'), (
#   ('', 'Ingredients are required'),
#   ('six', 'Ingredients must be of type integer'),
#   (7.2, 'Ingredients must be of type integer')
# ))
# def test_update_validate_input(client, auth, ingredients, message):
#     auth.register()
#     auth.login()

#     payload = {
#         'ingredients': ingredients
#     }

#     json_payload = json.dumps(payload)
#     response = client.post('/user/update', data = json_payload.encode('utf8'), content_type = 'application/json')

#     assert response.status_code == 400
#     recieved_message = response.get_json()
#     assert message in recieved_message['error']

def test_add(client):
    payload = {
        'input': 'salt'
    }

    json_payload = json.dumps(payload)
    response = client.post('/user/add', data = json_payload.encode('utf-8'), content_type = 'application/json')

    assert response.status_code == 201
    assert response.get_json() == {'message': 'Ingredient added'}

