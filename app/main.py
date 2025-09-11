

from fastapi import FastAPI # Importa a classe FastAPI para criar a aplicação web
from app.routers import clientes, eventos, agendas # Importa os módulos de roteamento (routers) de clientes, eventos e agendas


# Cria a instância da aplicação FastAPI
# Define o título, descrição e versão da API, que aparecerão na documentação automática
app = FastAPI(
    title="🎉 FESTIVA",
    description="Seu evento sob controle, sua criatividade em destaque!",
    version="1.0.0"
)


# Define a rota principal (endpoint "/") usando o método GET
# Quando o usuário acessar a raiz da API, ele receberá um dicionário com a mensagem de boas-vindas
@app.get("/")
def home():
    return {"Bem-vindos ao FESTIVA 🎉"}


# Incluindo routers na aplicação
# Cada router organiza endpoints relacionados a uma funcionalidade específica
# - clientes.router: endpoints relacionados a clientes, acessíveis com prefixo /clientes
# - eventos.router: endpoints relacionados a eventos, acessíveis com prefixo /eventos
# - agendas.router: endpoints relacionados a agendas, acessíveis com prefixo /agenda
# O parâmetro 'tags' ajuda a agrupar os endpoints na documentação automática do Swagger
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(eventos.router, prefix="/eventos", tags=["Eventos"])
app.include_router(agendas.router, prefix="/agenda", tags=["Agendas"])
