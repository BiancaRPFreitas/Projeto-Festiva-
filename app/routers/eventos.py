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
    return eventos_db

# Endpoint para criar evento
@router.post("/")
def criar_evento(evento: Evento):
    evento_dict = evento.dict()
    eventos_db.append(evento_dict)
    return evento_dict
