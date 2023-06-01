import json
import pytest
from flask import g
from backend.db import get_db

def test_update(client, auth):
    auth.register()
    auth.login()

    payload = {
        'ingredients': 6
    }

    json_payload = json.dumps(payload)
    response = client.post('/user/update', data = json_payload.encode('utf8'), content_type = 'application/json')

    assert response.status_code == 201
    assert response.get_json() == {'message': 'Ingredients updated'}

    db = get_db()
    user_ingredients = ((db.execute(
        'SELECT ingredients FROM user WHERE id = 3'
    ))).fetchone[0]

    assert user_ingredients == 6

# TODO: add test for when no ingredients are sent in the payload
