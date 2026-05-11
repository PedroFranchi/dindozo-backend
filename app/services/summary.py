from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from sqlalchemy import extract, func
from typing import Optional


def get_summary(db: Session, month: Optional[int] = None, year: Optional[int] = None):

    if year and month:
        total_income = (db.query(func.sum(Transaction.amount)).filter(Transaction.type == 'income', 
                                        extract('year', Transaction.date) == year,
                                        extract('month', Transaction.date) == month).scalar() or 0)
        total_expenses = (db.query(func.sum(Transaction.amount)).filter(Transaction.type == 'expense', 
                                        extract('year', Transaction.date) == year,
                                        extract('month', Transaction.date) == month).scalar() or 0)
    else:
        total_income = (db.query(func.sum(Transaction.amount)).filter(Transaction.type == 'income').scalar() or 0)
        total_expenses = (db.query(func.sum(Transaction.amount)).filter(Transaction.type == 'expense').scalar() or 0)
    
    total_balance = total_income - total_expenses
    return  {
    "total_income": total_income,
    "total_expenses": total_expenses,
    "total_balance": total_balance,
    "month": month,
    "year": year
}