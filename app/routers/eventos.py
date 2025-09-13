from fastapi import APIRouter

router = APIRouter()

eventos_db = []


@router.get("/")
def listar_eventos():
    """Retorna todos os eventos"""
    return eventos_db


@router.post("/")
def criar_evento(nome: str, cliente: str, data: str, orcamento: float):
    """Cria um novo evento"""
    evento = {"nome": nome, "cliente": cliente, "data": data, "orcamento": orcamento}
    eventos_db.append(evento)
    return evento
