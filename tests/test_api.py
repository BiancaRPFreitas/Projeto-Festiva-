from fastapi.testclient import TestClient
from app.main import app
from uuid import uuid4

client = TestClient(app)

# -------------------------
# TESTES DE EVENTOS
# -------------------------
def test_criar_evento():
    response = client.post(
        "/eventos/",
        json={
            "id": str(uuid4()),
            "nome": "Casamento",
            "cliente": "Mariana",
            "data": "2025-10-20",
            "orcamento": 5000
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Casamento"
    assert data["cliente"] == "Mariana"
    assert data["orcamento"] == 5000

def test_listar_eventos():
    response = client.get("/eventos/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_atualizar_evento():
    # Pega o primeiro evento da lista
    evento = client.get("/eventos/").json()[0]
    response = client.put(
        f"/eventos/{evento['nome']}",
        json={
            "id": evento["id"],
            "nome": "Casamento Atualizado",
            "cliente": "Mariana",
            "data": "2025-10-21",
            "orcamento": 7000
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Casamento Atualizado"
    assert data["orcamento"] == 7000

def test_deletar_evento():
    evento = client.get("/eventos/").json()[0]
    response = client.delete(f"/eventos/{evento['nome']}")
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Evento deletado com sucesso"

# -------------------------
# TESTES DE CLIENTES
# -------------------------
def test_criar_cliente():
    response = client.post(
        "/clientes/",
        json={
            "id": str(uuid4()),
            "nome": "Carlos",
            "email": "carlos@email.com"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Carlos"
    assert data["email"] == "carlos@email.com"

def test_listar_clientes():
    response = client.get("/clientes/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_atualizar_cliente():
    cliente = client.get("/clientes/").json()[0]
    response = client.put(
        f"/clientes/{cliente['id']}",
        json={
            "id": cliente["id"],
            "nome": "Carlos Silva",
            "email": "carlos.silva@email.com"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Carlos Silva"
    assert data["email"] == "carlos.silva@email.com"

def test_deletar_cliente():
    cliente = client.get("/clientes/").json()[0]
    response = client.delete(f"/clientes/{cliente['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Cliente deletado com sucesso"

# -------------------------
# TESTES DE AGENDAS
# -------------------------
def test_criar_agenda():
    response = client.post(
        "/agenda/",
        json={
            "id": str(uuid4()),
            "evento": "Festa de Aniversário",
            "data": "2025-11-10",
            "local": "Salão Azul"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["evento"] == "Festa de Aniversário"
    assert data["local"] == "Salão Azul"

def test_listar_agendas():
    response = client.get("/agenda/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_atualizar_agenda():
    agenda = client.get("/agenda/").json()[0]
    response = client.put(
        f"/agenda/{agenda['id']}",
        json={
            "id": agenda["id"],
            "evento": "Festa Atualizada",
            "data": "2025-11-11",
            "local": "Salão Vermelho"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["evento"] == "Festa Atualizada"
    assert data["local"] == "Salão Vermelho"

def test_deletar_agenda():
    agenda = client.get("/agenda/").json()[0]
    response = client.delete(f"/agenda/{agenda['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Agenda deletada com sucesso"
