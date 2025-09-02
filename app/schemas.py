# app/schemas.py
from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nombre: str
    email: str
    password: str
    rol: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        from_attributes = True
