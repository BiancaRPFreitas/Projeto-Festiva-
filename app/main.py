from fastapi import FastAPI  # Importa a classe FastAPI
from app.routers import (
    clientes,
    eventos,
    agendas,
)  # Importa os módulos de roteamento


app = FastAPI(
    title="🎉 FESTIVA",
    description=("Seu evento sob controle, sua criatividade em destaque!"),
    version="1.0.0",
)


@app.get("/")
def home():
    """Rota principal de boas-vindas"""
    return {"Bem-vindos ao FESTIVA 🎉"}


# Incluindo routers
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(eventos.router, prefix="/eventos", tags=["Eventos"])
app.include_router(agendas.router, prefix="/agenda", tags=["Agendas"])
