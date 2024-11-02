from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():
    new_sheep_data = {
        "id": 4,
        "name": "Spice4",
        "breed": "Gotland4",
        "sex": "ewe4"
    }

    response = client.post("/sheep", json=new_sheep_data)
    assert response.status_code == 201

    response_data = response.json()
    assert response_data["name"] == new_sheep_data["name"]
    assert response_data["age"] == new_sheep_data["age"]
    assert response_data["color"] == new_sheep_data["color"]
    assert response_data["breed"] == new_sheep_data["breed"]

    new_sheep_id = response_data["id"]
    get_response = client.get(f"/sheep/{new_sheep_id}")

    assert get_response.status_code == 200
    retrieved_sheep_data = get_response.json()
    assert retrieved_sheep_data["name"] == new_sheep_data["name"]
    assert retrieved_sheep_data["age"] == new_sheep_data["age"]
    assert retrieved_sheep_data["color"] == new_sheep_data["color"]
    assert retrieved_sheep_data["breed"] == new_sheep_data["breed"]
