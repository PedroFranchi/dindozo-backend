from app.core.database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    color = Column(String, default="#888780")
    icon = Column(String, default="ti ti-ghost-3")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    