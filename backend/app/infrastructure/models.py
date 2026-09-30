from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from datetime import datetime
from app.infrastructure.database import Base

class BidAnalysisModel(Base):
    __tablename__ = "bid_analyses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status = Column(String(50), nullable=False)
    viability_score = Column(Integer, nullable=False)
    summary = Column(Text, nullable=False)
    recommended_action = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)