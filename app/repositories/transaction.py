from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate
from sqlalchemy import extract

def get_all_transactions(db: Session, skip: int, limit: int, month: int, year: int) -> list[Transaction]:
    if year and month:
        transactions = db.query(Transaction).filter(
                                        extract('year', Transaction.date) == year,
                                        extract('month', Transaction.date) == month
                                        ).offset(skip).limit(limit).all()
    else:
        transactions = db.query(Transaction).offset(skip).limit(limit).all()
    return transactions

def get_transaction(db: Session, transaction_id: int):
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

def create_transaction(db: Session, transaction: TransactionCreate):
    db_transaction = Transaction(
        date=transaction.date,
        description=transaction.description,
        amount=transaction.amount,
        type=transaction.type,
        category_id=transaction.category_id,
        origin=transaction.origin,
        import_log_id=transaction.import_log_id
        )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transaction_by_categoty(db: Session, transaction_category: int):
    return db.query(Transaction).filter(Transaction.category_id == transaction_category).all()

def count_transactions(db: Session) -> int:
    return db.query(Transaction).count()