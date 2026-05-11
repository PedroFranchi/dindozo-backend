from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.category import get_all_category, get_category, create_category, delete_category_by_id
from app.schemas.category import CategoryCreate

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


router = APIRouter()

@router.get("/categories", tags=["Categories"])
async def list_categories(db: Session = Depends(get_db)):
    response = get_all_category(db)
    return response

@router.get("/categories/{id}", tags=["Categories"])
async def fetch_category(category_id: int, db: Session = Depends(get_db)):
    response = get_category(db, category_id)
    return response

@router.post("/categories", tags=["Categories"])
async def add_category(request: CategoryCreate, db: Session = Depends(get_db)):
    try:
        category = create_category(db, request)
        return category
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Category with this name already exists")
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/categories/{id}", tags=["Categories"])
async def remove_category(category_id: int, db: Session = Depends(get_db)):
    response = delete_category_by_id(db, category_id)
    return None
