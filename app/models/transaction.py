from app.core.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from datetime import datetime, timezone

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    description = Column(String, nullable=False)
    amount = Column(Float)
    type = Column(String, default="expense")
    category_id = Column(Integer, ForeignKey("categories.id"))
    origin = Column(String)
    import_log_id = Column(Integer, ForeignKey("import_log.id"), nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
