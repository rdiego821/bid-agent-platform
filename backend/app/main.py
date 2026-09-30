from fastapi import FastAPI
from app.interfaces.bid_router import router as bid_router

app = FastAPI(
    title="BidAgent Enterprise API",
    version="1.0.0",
    description="API basada en agentes de IA y Clean Architecture para análisis de licitaciones."
)

# Incluimos las rutas de la API
app.include_router(bid_router)

@app.get("/")
def root():
    return {"message": "Bienvenido a BidAgent API. El servidor está activo y operando correctamente."}