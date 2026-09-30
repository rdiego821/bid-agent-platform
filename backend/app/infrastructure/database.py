import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# Carga las variables definidas en el archivo .env
load_dotenv()

# Lee la URL de la base de datos desde el entorno; si no existe, lanza un error claro
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("No se encontró la variable de entorno DATABASE_URL en el archivo .env")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Dependencia de FastAPI para obtener la sesión de base de datos por cada petición."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()