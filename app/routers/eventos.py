from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Modelo de dados para o evento
class Evento(BaseModel):
    nome: str
    cliente: str
    data: str
    orcamento: int

# Banco de dados em memória
eventos_db: List[Evento] = []

@router.get("/")
def listar_eventos():
    """Retorna todos os eventos cadastrados."""
    return eventos_db

@router.post("/", response_model=Evento)
def criar_evento(evento: Evento):
    """Cria um novo evento e adiciona no banco de dados."""
    eventos_db.append(evento)
    return evento
