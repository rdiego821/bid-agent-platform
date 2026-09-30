from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.domain.bid import BidAnalysisRequest, BidAnalysisResponse
from app.application.agent_workflow import create_bid_workflow
from app.infrastructure.database import get_db, engine, Base
from app.infrastructure.repositories import BidRepository

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/api/v1", tags=["Bids"])

@router.post("/analyze-bid", response_model=BidAnalysisResponse)
async def analyze_bid_endpoint(request: BidAnalysisRequest, db: Session = Depends(get_db)):
    try:
        # Inicializamos el grafo compilado de LangGraph
        app_workflow = create_bid_workflow()
        
        # Estado inicial que alimenta al agente
        initial_state = {
            "document_text": request.document_text,
            "client_budget": request.client_budget,
            "viability_score": 0,
            "summary": "",
            "recommended_action": "",
            "status": "pending"
        }
        
        # Ejecutamos el flujo del agente
        result = app_workflow.invoke(initial_state)

        # 2. Guardar el resultado en PostgreSQL usando el Patrón Repository
        repository = BidRepository(db)
        repository.save_analysis(
            status=result["status"],
            score=result["viability_score"],
            summary=result["summary"],
            action=result["recommended_action"]
        )
        
        return BidAnalysisResponse(
            status=result["status"],
            viability_score=result["viability_score"],
            summary=result["summary"],
            recommended_action=result["recommended_action"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error ejecutando el agente: {str(e)}")