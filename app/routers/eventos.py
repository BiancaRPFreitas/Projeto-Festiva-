from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Modelo de dados para representar um evento
class Evento(BaseModel):
    nome: str
    data: str   # pode ser trocado para datetime se quiser validar datas automaticamente
    local: str

# "Banco de dados" em memória
eventos_db = []

# Endpoint para listar eventos
@router.get("/")
def listar_eventos():
    """Retorna todos os eventos"""
    return eventos_db


@router.post("/")
def criar_evento(nome: str, data: str, local: str):
    """Cria um novo evento e adiciona ao banco"""
    evento = {"nome": nome, "data": data, "local": local}
    eventos_db.append(evento)
    return evento