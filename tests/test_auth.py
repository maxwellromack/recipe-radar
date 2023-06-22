import json
import pytest
from flask import g, session
from backend.db import get_db
from werkzeug.security import check_password_hash, generate_password_hash


def test_register(client):
    payload = {
        'username': 'freeman',
        'password': 'blackMesa1998'
    }

    json_payload = json.dumps(payload)
    response = client.post('/auth/register', data = json_payload.encode('utf8'), content_type = 'application/json')
    
    assert response.status_code == 201
    assert response.get_json() == {'message': 'Registration success'}

def test_register_frontend_sim(client):
    payload = {"username":"a","password":"a"}

    json_payload = json.dumps(payload)
    response = client.post('/auth/register', data = json_payload.encode('utf8'), content_type = 'application/json')
    
    assert response.status_code == 201
    assert response.get_json() == {'message': 'Registration success'}

@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', 'Username is required'),
    ('robert', '', 'Password is required'),
    ('test', 'test', 'already registered'),
))
def test_register_validate_input(client, username, password, message):
    payload = {
        'username': username,
        'password': password
    }

    json_payload = json.dumps(payload)
    response = client.post('/auth/register', data = json_payload.encode('utf8'), content_type = 'application/json')

    assert response.status_code == 400
    recieved_message = response.get_json()
    assert message in recieved_message['error']

@pytest.mark.parametrize(('username', 'password', 'message'), (
        ('user spaces', 'test', 'Username cannot contain spaces'),
        ('user', 'pass spaces', 'Password cannot contain spaces')
))
def test_register_spaces(client, username, password, message):
    payload = {
        'username': username,
        'password': password
    }

    json_payload = json.dumps(payload)
    response = client.post('/auth/register', data = json_payload.encode('utf8'), content_type = 'application/json')

    assert response.status_code == 400
    recieved_message = response.get_json()
    assert message in recieved_message['error']

def test_register_ingredients(client, auth, app):
    auth.register()

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

    assert user_ingredients == bin_str

def test_login(client, auth):
    auth.register()

    with client:
        response = auth.login()
        assert response.status_code == 200
        assert 'user_id' in session
        assert session['user_id'] == 3

@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', 'Incorrect username'),
    ('test', 'a', 'Incorrect password'),
))
def test_login_validate_input(client, username, password, message):
    payload = {
        'username': username,
        'password': password
    }

    json_payload = json.dumps(payload)
    response = client.post('/auth/login', data = json_payload.encode('utf8'), content_type = 'application/json')

    assert response.status_code == 400
    recieved_message = response.get_json()
    assert message in recieved_message['error']

def test_logout(client, auth):
    auth.login()

    with client:
        client.get('/auth/logout')
        assert 'user_id' not in session


