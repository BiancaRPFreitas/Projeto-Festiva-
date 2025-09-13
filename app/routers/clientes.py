from fastapi import APIRouter

router = APIRouter()

clientes_db = []


@router.get("/")
def listar_clientes():
    """Retorna todos os clientes"""
    return clientes_db


@router.post("/")
def criar_cliente(nome: str, email: str):
    """Cria um novo cliente"""
    cliente = {"nome": nome, "email": email}
    clientes_db.append(cliente)
    return cliente
