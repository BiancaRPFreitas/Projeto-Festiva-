from fastapi import APIRouter, HTTPException
from uuid import UUID
from typing import List
from app.models import Cliente
from app.database import clientes_db

router = APIRouter()

@router.post("/", response_model=Cliente)
def criar_cliente(cliente: Cliente):
    clientes_db.append(cliente)
    return cliente

@router.get("/", response_model=List[Cliente])
def listar_clientes():
    return clientes_db

@router.get("/{cliente_id}", response_model=Cliente)
def buscar_cliente(cliente_id: UUID):
    for c in clientes_db:
        if c.id == cliente_id:
            return c
    raise HTTPException(status_code=404, detail="Cliente não encontrado")

@router.put("/{cliente_id}", response_model=Cliente)
def atualizar_cliente(cliente_id: UUID, cliente_atualizado: Cliente):
    for i, c in enumerate(clientes_db):
        if c.id == cliente_id:
            clientes_db[i] = cliente_atualizado
            return cliente_atualizado
    raise HTTPException(status_code=404, detail="Cliente não encontrado")

@router.delete("/{cliente_id}")
def deletar_cliente(cliente_id: UUID):
    for i, c in enumerate(clientes_db):
        if c.id == cliente_id:
            clientes_db.pop(i)
            return {"detail": "Cliente deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Cliente não encontrado")
