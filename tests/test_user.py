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

