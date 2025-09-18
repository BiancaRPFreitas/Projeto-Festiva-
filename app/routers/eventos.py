from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Evento
from app.database import eventos_db

router = APIRouter()

@router.post("/", response_model=Evento)
def criar_evento(evento: Evento):
    eventos_db.append(evento)
    return evento

@router.get("/", response_model=List[Evento])
def listar_eventos():
    return eventos_db

@router.get("/{nome_evento}")
def buscar_evento(nome_evento: str):
    for e in eventos_db:
        if e.nome == nome_evento:
            return e
    raise HTTPException(status_code=404, detail="Evento não encontrado")

@router.put("/{nome_evento}")
def atualizar_evento(nome_evento: str, evento_atualizado: Evento):
    for i, e in enumerate(eventos_db):
        if e.nome == nome_evento:
            eventos_db[i] = evento_atualizado
            return evento_atualizado
    raise HTTPException(status_code=404, detail="Evento não encontrado")

@router.delete("/{nome_evento}")
def deletar_evento(nome_evento: str):
    for i, e in enumerate(eventos_db):
        if e.nome == nome_evento:
            eventos_db.pop(i)
            return {"detail": "Evento deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Evento não encontrado")