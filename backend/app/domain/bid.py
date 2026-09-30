from pydantic import BaseModel, Field
from typing import Optional, List

class BidAnalysisRequest(BaseModel):
    document_text: str = Field(..., description="Texto extraído del pliego de licitación o RFP.")
    client_budget: float = Field(..., gt=0, description="Presupuesto máximo ofrecido por el cliente.")

class BidAnalysisResponse(BaseModel):
    status: str = Field(..., description="Estado del análisis (success, rejected, review_needed).")
    viability_score: int = Field(..., ge=0, le=100, description="Puntuación de viabilidad técnica de 0 a 100.")
    summary: str = Field(..., description="Resumen ejecutivo del análisis del agente.")
    recommended_action: str = Field(..., description="Acción sugerida para la empresa.")