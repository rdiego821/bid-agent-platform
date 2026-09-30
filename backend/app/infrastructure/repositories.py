from sqlalchemy.orm import Session
from app.infrastructure.models import BidAnalysisModel

class BidRepository:
    def __init__(self, db: Session):
        self.db = db

    def save_analysis(self, status: str, score: int, summary: str, action: str) -> BidAnalysisModel:
        """Guarda un nuevo análisis de licitación en PostgreSQL."""
        db_record = BidAnalysisModel(
            status=status,
            viability_score=score,
            summary=summary,
            recommended_action=action
        )
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record