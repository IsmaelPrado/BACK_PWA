# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:post123@localhost:5432/seguridad"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependencia para inyectar sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
