from backend import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_example(client):
    response = client.get('/example')
    assert response.data == b"This is an example of a webpage!"
