import json
import pytest

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
    assert response.get_json() == {'error': message}
