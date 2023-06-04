import json
import pytest
from flask import g
from backend.db import get_db

def test_add(client, auth):
    auth.register()
    auth.login()

    payload = {
        'input': 'salt'
    }

    json_payload = json.dumps(payload)
    response = client.post('/user/add', data = json_payload.encode('utf-8'), content_type = 'application/json')

    assert response.status_code == 201
    assert response.get_json() == {'message': 'Ingredient added'}

def test_add_plural(client, auth):
    auth.register()
    auth.login()

    payload = {
        'input': 'salts'
    }

    json_payload = json.dumps(payload)
    response = client.post('/user/add', data = json_payload.encode('utf-8'), content_type = 'application/json')

    assert response.status_code == 201
    assert response.get_json() == {'message': 'Singular ingredient added'}

def test_add_no_match(client, auth):
    auth.register()
    auth.login()

    payload = { # i really hope that no recipe will ever use concrete as an ingredent
        'input': 'concrete'
    }

    json_payload = json.dumps(payload)
    response = client.post('/user/add', data = json_payload.encode('utf-8'), content_type = 'application/json')

    assert response.status_code == 400
    assert response.get_json() == {'message': 'No match found'}

@pytest.mark.parametrize(('input'), (
    ('goat\'s cheese'),
    ('t-bone steak')
))
def test_add_cleaning(client, auth, input):
    auth.register()
    auth.login()

    payload = {
        'input': input
    }

    json_payload = json.dumps(payload)
    response = client.post('/user/add', data = json_payload.encode('utf-8'), content_type = 'application/json')

    assert response.status_code == 201
    assert response.get_json() == {'message': 'Ingredient added'}

@pytest.mark.parametrize(('input', 'message'), (
    ('', 'Input is required'),
    ('9 apples', 'Input must contain only letters and spaces'),
    ('salt!!!', 'Input must contain only letters and spaces')
))
def test_add_validation(client, auth, input, message):
    auth.register()
    auth.login()

    payload = {
        'input': input
    }

    json_payload = json.dumps(payload)
    response = client.post('/user/add', data = json_payload.encode('utf-8'), content_type = 'application/json')

    assert response.status_code == 400
    assert message in response.get_json()['error']

def test_add_db(client, auth, app):
    auth.register()
    auth.login()

    payload = {
        'input': 'salt'
    }

    json_payload = json.dumps(payload)
    client.post('user/add', data = json_payload.encode('utf-8'), content_type = 'application/json')

    with app.app_context():
        db = get_db()
        user_ingredients = (db.execute(
            'SELECT ingredients FROM user WHERE id = 3'
        )).fetchone()[0]

    size = 0
    with open('backend/ingredients_list.txt', 'r') as file:
        for size, _ in enumerate(file):
            pass

    bin_str = ''
    for i in range(size):
        bin_str += '0'
    bin_str = '1' + bin_str[1:]
    
    assert user_ingredients == bin_str

def test_add_similar(client, auth):
    auth.register()
    auth.login()

    payload = {
        'input': 'sslt'
    }

    json_payload = json.dumps(payload)
    response = client.post('user/add', data = json_payload.encode('utf-8'), content_type = 'application/json')

    assert response.status_code == 400
    assert 'Similar' in response.get_json()['message']
    assert 'salt' in response.get_json()['ingredient']
