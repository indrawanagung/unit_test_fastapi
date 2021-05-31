from fastapi.testclient import TestClient 

from main import app 

client = TestClient(app)

data = {
    "name": "Makhacev",
    "email": "email@google.com",
    "password": "123",
    "phone": "089"
    }

#TEST CREATE
def test_create_todo():
    response = client.post("/todo/", json=data)
    assert response.status_code == 200
    assert response.json() == data

#TEST READ ALL DATA
def test_get_all_todo():
    response = client.get("/todo/", json=data)
    assert response.status_code == 200
    assert data in response.json()

#TEST READ BY ID
def test_get_todo():
    response = client.get("/todo/0")
    assert response.status_code == 200
    assert response.json() == data

#TEST UPDATE
def test_update_todo():
    response = client.put("/todo/0", json = {
        "name": "Javascipt",
        "email": "yahoo@google.com",
        "password": "345",
        "phone": "08219"
    })
    assert response.status_code == 200
    assert response.json() == {   
        "name": "Javascipt",
        "email": "yahoo@google.com",
        "password": "345",
        "phone": "08219"
    }

#TEST DELETE
def test_delete_todo():
    response = client.delete("/todo/0")
    assert response.status_code == 200
    assert response.json() == {   
        "name": "Javascipt",
        "email": "yahoo@google.com",
        "password": "345",
        "phone": "08219"
    }