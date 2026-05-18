from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from sqlalchemy import extract, func
from typing import Optional
from sqlalchemy import case


def get_summary(db: Session, month: Optional[int] = None, year: Optional[int] = None):

    if year and month:
        total_income = (db.query(func.sum(Transaction.amount)).filter(Transaction.type == 'income', 
                                        extract('year', Transaction.date) == year,
                                        extract('month', Transaction.date) == month).scalar() or 0)
        total_expenses = abs(db.query(func.sum(Transaction.amount)).filter(Transaction.type == 'expense', 
                                        extract('year', Transaction.date) == year,
                                        extract('month', Transaction.date) == month).scalar() or 0)
    else:
        total_income = (db.query(func.sum(Transaction.amount)).filter(Transaction.type == 'income').scalar() or 0)
        total_expenses = abs(db.query(func.sum(Transaction.amount)).filter(Transaction.type == 'expense').scalar() or 0)
    
    total_balance = total_income - total_expenses
    return  {
    "total_income": total_income,
    "total_expenses": total_expenses,
    "total_balance": total_balance,
    "month": month,
    "year": year
}

def get_monthly_summary(db: Session):
    results = (
        db.query(
            extract('year', Transaction.date).label('year'),
            extract('month', Transaction.date).label('month'),
            func.sum(
                case((Transaction.type == 'income', Transaction.amount), else_=0)
            ).label('income'),
            func.abs(func.sum(
                case((Transaction.type == 'expense', Transaction.amount), else_=0)
            )).label('expenses')
        )
        .group_by(
            extract('year', Transaction.date),
            extract('month', Transaction.date)
        )
        .order_by(
            extract('year', Transaction.date),
            extract('month', Transaction.date)
        )
        .all()
    )

    return [
        {
            "year": int(r.year),
            "month": int(r.month),
            "income": r.income or 0,
            "expenses": r.expenses or 0
        }
        for r in results
    ]