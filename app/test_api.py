from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_criar_evento():
    response = client.post("/eventos/", json={
        "nome": "Casamento",
        "data": "2025-10-20",
        "local": "Salão"
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "Casamento"

def test_listar_eventos():
    response = client.get("/eventos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

