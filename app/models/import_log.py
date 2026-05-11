from app.core.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

class ImportLog(Base):
    __tablename__ = 'import_log'
    
    id = Column(Integer, primary_key=True)
    filename = Column(String, nullable=False)
    imported_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    transaction_count = Column(Integer)
    uncategorized_count = Column(Integer)
