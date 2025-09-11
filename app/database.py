from .models import Evento

# Banco de dados em memória (lista simples)
eventos = []

def adicionar_evento(evento: Evento):
    eventos.append(evento)
    return evento

def listar_eventos():
    return eventos

def remover_evento(nome: str):
    global eventos
    eventos = [e for e in eventos if e.nome != nome]
    return {"mensagem": f"Evento '{nome}' removido."}

def buscar_evento(nome: str):
    for e in eventos:
        if e.nome == nome:
            return e
    return None