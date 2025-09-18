from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Agenda
from app.database import agendas_db
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=Agenda)
def criar_agenda(agenda: Agenda):
    agendas_db.append(agenda)
    return agenda

@router.get("/", response_model=List[Agenda])
def listar_agendas():
    return agendas_db

@router.get("/{agenda_id}", response_model=Agenda)
def buscar_agenda(agenda_id: UUID):
    for a in agendas_db:
        if a.id == agenda_id:
            return a
    raise HTTPException(status_code=404, detail="Agenda não encontrada")

@router.put("/{agenda_id}", response_model=Agenda)
def atualizar_agenda(agenda_id: UUID, agenda_atualizada: Agenda):
    for i, a in enumerate(agendas_db):
        if a.id == agenda_id:
            agendas_db[i] = agenda_atualizada
            return agenda_atualizada
    raise HTTPException(status_code=404, detail="Agenda não encontrada")

@router.delete("/{agenda_id}")
def deletar_agenda(agenda_id: UUID):
    for i, a in enumerate(agendas_db):
        if a.id == agenda_id:
            agendas_db.pop(i)
            return {"detail": "Agenda deletada com sucesso"}
    raise HTTPException(status_code=404, detail="Agenda não encontrada")
