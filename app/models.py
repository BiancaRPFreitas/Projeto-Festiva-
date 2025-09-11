from pydantic import BaseModel

class Evento(BaseModel):
    nome: str
    cliente: str
    data: str
    orcamento: float