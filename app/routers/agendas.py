from fastapi import APIRouter

router = APIRouter()

agendas_db = []

@router.get("/")
def listar_agendas():
    return agendas_db

@router.post("/")
def criar_agenda(evento_nome: str, horario: str):
    agenda = {"evento_nome": evento_nome, "horario": horario}
    agendas_db.append(agenda)
    return agenda