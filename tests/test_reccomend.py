import json
import pytest
from backend.db import get_db
from backend.auth import init_bin_str

def test_update(client, auth, app):
    with app.app_context():
        db = get_db()
        string = init_bin_str()
        string = '1' + string[1:]
        db.execute(
                'INSERT INTO recipe (ingredients) VALUES (?)',
                (string,)
            )
        db.commit()
        string2 = init_bin_str()
        string2 = string2[:2] + '1' + string2[3:]
        db.execute(
                'INSERT INTO recipe (ingredients) VALUES (?)',
                (string,)
            )
        db.commit()

    auth.register()
    auth.login()

    payload = {
        'input': 'salt'
    }

    json_payload = json.dumps(payload)
    client.post('/user/add', data = json_payload.encode('utf-8'), content_type = 'application/json')
    response = client.get('/rec/update')

    assert response.status_code == 200
    message = response.get_json()
    assert 'Matched' in message['message']
    assert message['recipes'] == '0 1'
