# app/routes/usuarios.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=schemas.UsuarioResponse)
def crear(usuario: schemas.UsuarioCreate, db: Session = Depends(database.get_db)):
    return crud.crear_usuario(db, usuario)

@router.get("/", response_model=list[schemas.UsuarioResponse])
def listar(db: Session = Depends(database.get_db)):
    return crud.obtener_usuarios(db)

@router.get("/{usuario_id}", response_model=schemas.UsuarioResponse)
def obtener(usuario_id: int, db: Session = Depends(database.get_db)):
    return crud.obtener_usuario(db, usuario_id)

@router.put("/{usuario_id}", response_model=schemas.UsuarioResponse)
def actualizar(usuario_id: int, datos: schemas.UsuarioCreate, db: Session = Depends(database.get_db)):
    return crud.actualizar_usuario(db, usuario_id, datos)

@router.delete("/{usuario_id}")
def eliminar(usuario_id: int, db: Session = Depends(database.get_db)):
    return crud.eliminar_usuario(db, usuario_id)
