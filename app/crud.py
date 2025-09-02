# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    try:
        db.commit()
        db.refresh(db_usuario)
    except:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email ya registrado o error en la base de datos")
    return db_usuario

def obtener_usuarios(db: Session):
    return db.query(models.Usuario).all()

def obtener_usuario(db: Session, usuario_id: int):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

def actualizar_usuario(db: Session, usuario_id: int, datos: schemas.UsuarioCreate):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in datos.dict().items():
        setattr(usuario, key, value)
    db.commit()
    db.refresh(usuario)
    return usuario

def eliminar_usuario(db: Session, usuario_id: int):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()
    return {"detail": "Usuario eliminado"}

