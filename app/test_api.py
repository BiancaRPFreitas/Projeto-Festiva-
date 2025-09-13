from fastapi.testclient import TestClient
from app.main import app

# Cria o cliente de teste para simular requisições HTTP
client = TestClient(app)


def test_criar_evento():
    """Testa a criação de um evento através da rota POST /eventos."""
    response = client.post(
        "/eventos",
        json={
            "nome": "Casamento",
            "cliente": "Ana",
            "data": "2025-10-20",
            "orcamento": 5000,
        },
    )
    assert response.status_code == 200
    assert response.json()["nome"] == "Casamento"


def test_listar_eventos():
    """Testa a listagem de eventos através da rota GET /eventos."""
    response = client.get("/eventos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)