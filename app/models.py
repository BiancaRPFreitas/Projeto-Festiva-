class Cliente:
    """Modelo que representa um cliente."""

    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email


class Evento:
    """Modelo que representa um evento."""

    def __init__(self, nome: str, data: str, local: str):
        self.nome = nome
        self.data = data
        self.local = local
        