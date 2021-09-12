import pytest 
from fastapi.testclient import TestClient

from main import api

@pytest.fixture
def client():
    yield TestClient(api)

class TestItems:
    def test_create_item(self, client):
        data = {
            "item_name": "name",
            "item_description": "description"
        }
        response = client.post(
            "/items/", json=data
        )
        assert response.status_code == 200

    def test_get_items(self, client):
        data = {
            "item_name": "name",
            "item_description": "description"
        }
        response = client.post(
            "/items/", json=data
        )
        assert response.status_code == 200

        response = client.get("/items/")
        assert response.status_code == 200

    def test_update_item(self, client):
        data = {
            "item_name": "name",
            "item_description": "description"
        }
        response = client.post(
            "/items/", json=data
        )
        assert response.status_code == 200

        id = response.json()["id"]
        print(id)
        response = client.patch("/items/", json={
            "id": id,
            "item_name": "new_name",
            "item_description": "new_description"
        })
        assert response.status_code == 200

    def test_delete_item(self, client):
        data = {
            "item_name": "name",
            "item_description": "description"
        }
        response = client.post(
            "/items/", json=data
        )
        assert response.status_code == 200

        id = response.json()["id"]
        print(id)
        response = client.delete("/items/", json={
            "id": id
        })
        assert response.status_code == 200
