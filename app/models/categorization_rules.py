from app.core.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime, timezone

class CategorizationRule(Base):
    __tablename__ = 'categorization_rules'
    
    id = Column(Integer, primary_key=True)
    keyword = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
