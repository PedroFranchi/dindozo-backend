from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.csv_parser import parse_csv
from app.services.categorizer import categorize
from app.repositories.transaction import create_transaction
from app.schemas.transaction import TransactionCreate
from app.schemas.import_log import ImportLogCreate
from app.repositories.import_log import create_import_log, get_all_import_logs

import io


from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

router = APIRouter()

@router.get("/imports", tags=["Imports"])
async def list_imports(db: Session = Depends(get_db)):
    response = get_all_import_logs(db)
    return response

@router.post("/imports", tags=['Imports'])
async def add_csv(csv: UploadFile, db: Session = Depends(get_db)):

    if not csv.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Only .csv files are accepted")

    content = await csv.read()
    csv_init = parse_csv(io.BytesIO(content))
    csv_transactions = categorize(db, csv_init)
    try:
        for transaction in csv_transactions:
            create_transaction(db, TransactionCreate(**transaction))
        create_import_log(ImportLogCreate(
            filename = csv.filename,
            transaction_count = len(csv_transactions),
            uncategorized_count = sum(1 for t in csv_transactions if t['category_id'] is None)
        ),db)
        return {"imported": len(csv_transactions)}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invalid or duplicate data")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str("CSV format not recognized"))
    except Exception as e:
        print(e)
        db.rollback()
        raise HTTPException(status_code=500, detail=str('Internal server error'))
