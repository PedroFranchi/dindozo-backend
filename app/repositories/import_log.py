from sqlalchemy.orm import Session
from app.models.import_log import ImportLog
from app.schemas.import_log import ImportLogCreate

def get_all_import_logs(db: Session) -> list[ImportLog]:
    return db.query(ImportLog).all()

def create_import_log (import_log: ImportLogCreate, db: Session):
    db_import_log = ImportLog(
        filename=import_log.filename,
        transaction_count=import_log.transaction_count,
        uncategorized_count=import_log.uncategorized_count
    )
    db.add(db_import_log)
    db.commit()
    db.refresh(db_import_log)
    return db_import_log