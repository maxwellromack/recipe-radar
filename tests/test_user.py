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

@pytest.mark.parameterize(('input', 'message'), (
    ('', 'Input is required'),
    ('goat\'s cheese', 'Ingredient added')
))
def test_add_validation
