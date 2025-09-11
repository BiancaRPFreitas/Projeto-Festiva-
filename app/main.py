from fastapi import FastAPI
from app.routers import clientes, eventos, agendas

app = FastAPI(
    title="🎉 FESTIVA",
    description="Seu evento sob controle, sua criatividade em destaque!",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"Bem-vindo ao FESTIVA 🎉"}

# Incluindo routers
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(eventos.router, prefix="/eventos", tags=["Eventos"])
app.include_router(agendas.router, prefix="/agenda", tags=["Agendas"])
