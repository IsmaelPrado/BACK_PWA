# app/main.py
from fastapi import FastAPI
from .routes import usuarios
from .database import Base, engine

# Crear tablas al iniciar la app
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Usuarios")

# Incluir rutas
app.include_router(usuarios.router)
