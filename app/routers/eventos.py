@router.post("/")
def criar_evento(nome: str, cliente: str, data: str, orcamento: float):
    """Cria um novo evento"""
    evento = {
        "nome": nome,
        "cliente": cliente,
        "data": data,
        "orcamento": orcamento,
    }
    eventos_db.append(evento)
    return evento
