from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_criar_evento():
    response = client.post("/eventos", json={
        "nome": "Casamento",
        "cliente": "Ana",
        "data": "20/10/2025",
        "orcamento": 5000
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "Casamento"

def test_listar_eventos():
    response = client.get("/eventos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)