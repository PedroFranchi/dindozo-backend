from fastapi import APIRouter, Depends
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.repositories.rules import create_rule, delete_rule_by_id, get_all_rules
from app.schemas.rules import RuleCreate

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

router = APIRouter()

@router.get('/rules', tags=['Rules'])
async def list_rules(db: Session = Depends(get_db)):
    return get_all_rules(db)

@router.post('/rules', tags=['Rules'])
async def add_rule(request: RuleCreate, db: Session = Depends(get_db)):
    try:
        response = create_rule(request, db)
        return response
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Dados inválidos ou duplicados")
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro interno no servidor")

@router.delete('/rules/{id}', tags=['Rules'])
async def remove_rule(id: int, db: Session = Depends(get_db)) -> None:
    response = delete_rule_by_id(db, id)
    return None