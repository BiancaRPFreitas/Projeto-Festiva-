from pydantic import BaseModel, EmailStr
from uuid import UUID

class Cliente(BaseModel):
    id: UUID
    nome: str
    email: EmailStr

class Evento(BaseModel):
    id: UUID
    nome: str
    cliente: str
    data: str
    orcamento: int

class Agenda(BaseModel):
    id: UUID
    evento: str
    data: str
    local: str
