from pydantic import BaseModel
from typing import Optional


class Tecnicos(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str

    # Transformar automaticamente em Schema
    class Config:
        orm_mode = True


class Patrimonio(BaseModel):
    id: Optional[int] = None
    patrimonio: str
    depto: str
    serivcetag: str
    garantia: str
    status: str

    # Transformar automaticamente em Schema
    class Config:
        orm_mode = True


class Licenca(BaseModel):
    id: Optional[int] = None
    produto: str
    chave: str
    nota: str
    solcompra: str
    pedcompra: str

   # Transformar automaticamente em Schema
    class Config:
        orm_mode = True
