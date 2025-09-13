from pydantic import BaseModel

class Cliente:
    """Representa um cliente do sistema FESTIVA."""

    def __init__(self, nome: str, email: str):
        """
        Inicializa um cliente.

        Args:
            nome (str): Nome do cliente.
            email (str): Email do cliente.
        """
        self.nome = nome
        self.email = email


class Evento:
    """Representa um evento cadastrado no sistema FESTIVA."""

    def __init__(self, titulo: str, data: str):
        """
        Inicializa um evento.

        Args:
            titulo (str): Nome ou título do evento.
            data (str): Data em que o evento ocorrerá.
        """
        self.titulo = titulo
        self.data = data
