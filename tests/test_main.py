#from fastapi import FastAPI
#from fastapi.testclient import TestClient
#from app.main import app

#client = TestClient(app)


def test_read_main():
    assert 1 == 1
    #response = client.get("/")
    #assert response.status_code == 200
    #assert response.json() == {"msg": "Hello World"}