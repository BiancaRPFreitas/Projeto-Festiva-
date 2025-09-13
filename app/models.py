from pydantic import BaseModel


class Cliente(BaseModel):
    nome: str
    email: str


class Evento(BaseModel):
    nome: str
    cliente: str
    data: str
    orcamento: float
