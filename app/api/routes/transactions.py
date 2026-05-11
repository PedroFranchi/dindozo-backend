from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.transaction import create_transaction, get_all_transactions, get_transaction, get_transaction_by_categoty
from app.schemas.transaction import TransactionCreate
from typing import Optional

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

router = APIRouter()

@router.get("/transactions", tags=["Transactions"])
async def list_transactions(db: Session = Depends(get_db), skip: int = 0, limit: int = 10, month: Optional[int] = None, year: Optional[int] = None):
    response = get_all_transactions(db, skip, limit, month, year)
    return response

@router.get("/transactions/{id}", tags=["Transactions"])
async def fetch_transaction(transaction_id: int, db: Session = Depends(get_db)):
    response = get_transaction(db, transaction_id)
    return response

@router.post("/transactions", tags=["Transactions"])
async def add_transaction(request: TransactionCreate, db: Session = Depends(get_db)):
    try:
        transaction = create_transaction(db, request)
        return transaction
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Dados inválidos ou duplicados")
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno no servidor")