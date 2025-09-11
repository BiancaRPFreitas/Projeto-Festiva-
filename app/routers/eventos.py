from fastapi import APIRouter

router = APIRouter()

eventos_db = []

@router.get("/")
def listar_eventos():
    return eventos_db

@router.post("/")
def criar_evento(nome: str, data: str, local: str):
    evento = {"nome": nome, "data": data, "local": local}
    eventos_db.append(evento)
    return evento