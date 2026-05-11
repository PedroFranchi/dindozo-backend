from fastapi import APIRouter, Depends
from app.services.summary import get_summary
from app.core.database import get_db
from sqlalchemy.orm import Session
from typing import Optional


router = APIRouter()

@router.get("/summary/", tags=['Summary'])
def fetch_summary(year: Optional[int] = None, month: Optional[int] = None, db: Session = Depends(get_db)):
    return get_summary(db, month, year)









