from fastapi import APIRouter

router = APIRouter()

clientes_db = []

@router.get("/")
def listar_clientes():
    return clientes_db

@router.post("/")
def criar_cliente(nome: str, email: str):
    cliente = {"nome": nome, "email": email}
    clientes_db.append(cliente)
    return cliente