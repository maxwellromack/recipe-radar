import json
import pytest
from flask import g, session
from backend.db import get_db

def test_register(client):
    payload = {
        'username': 'freeman',
        'password': 'blackMesa1998'
    }

    json_payload = json.dumps(payload)
    response = client.post('/auth/register', data = json_payload, content_type = 'application/json')
    
    assert response.status_code == 201
    assert response.get_json() == {'message': 'Registation success'}

@pytest.mark.parametrize(('username', 'password', 'message'),(
    ('', '', b'Username is required'),
    ('robert', '', b'Password is required'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    payload = {
        'username': username,
        'password': password
    }

    json_payload = json.dumps(payload)
    response = client.post('/auth/register', data = json_payload, content_type = 'application/json')

    assert response.status_code == 400
    recieved_message = json.loads(response.get_json())
    assert message in recieved_message['error']

def test_login(client):
    payload = {
        'username': 'test',
        'password': 'test'
    }

    json_payload = json.dumps(payload)
    response = client.post('auth/login', data = json_payload, content_type = 'application/json')

    assert response.status_code == 200
    assert session['user_id'] == 1
    assert g.user['username'] == 'test'

@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username'),
    ('test', 'a', b'Incorrect password'),
))
def test_login_validate_input(client, username, password, message):
    payload = {
        'username': username,
        'password': password
    }

    json_payload = json.dumps(payload)
    response = client.post('/auth/login', data = json_payload, content_type = 'application/json')

    assert response.status_code == 400
    recieved_message = json.loads(response.get_json())
    assert message in recieved_message['error']

def test_logout(client, auth):
    auth.login()

    with client:
        client.get('/auth/logout')
        assert 'user_id' not in session
