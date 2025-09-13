from fastapi import APIRouter

router = APIRouter()

agendas_db = []


@router.get("/")
def listar_agendas():
    """Retorna todas as agendas"""
    return agendas_db


@router.post("/")
def criar_agenda(evento: str, data: str, local: str):
    """Cria uma nova agenda"""
    agenda = {"evento": evento, "data": data, "local": local}
    agendas_db.append(agenda)
    return agenda
